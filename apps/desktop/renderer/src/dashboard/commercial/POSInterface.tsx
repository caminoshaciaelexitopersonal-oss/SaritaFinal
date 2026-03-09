import React, { useState, useEffect } from 'react';
import { ShoppingCart, Search, Trash2, CreditCard, Wallet, Banknote, Package, CheckCircle, Wifi, WifiOff } from 'lucide-react';
import clsx from 'clsx';

// Type definitions for the SARITA POS
interface Product {
  id: string;
  name: string;
  price: number;
  stock_actual: number;
}

interface CartItem extends Product {
  quantity: number;
}

export const POSInterface = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [cart, setCart] = useState<CartItem[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [paymentMethod, setPaymentMethod] = useState<'EFECTIVO' | 'WALLET' | 'TARJETA'>('EFECTIVO');
  const [syncStatus, setSyncStatus] = useState({ online: true, lastSync: '' });
  const [isProcessing, setIsProcessing] = useState(false);

  // Load products and sync status on mount
  useEffect(() => {
    const loadInitialData = async () => {
      const saritaAPI = (window as any).saritaAPI;
      if (saritaAPI) {
        const localProducts = await saritaAPI.pos.getProducts();
        setProducts(localProducts.length > 0 ? localProducts : [
          { id: '1', name: 'Café Especial', price: 15000, stock_actual: 50 },
          { id: '2', name: 'Artesanía Mochila', price: 85000, stock_actual: 12 },
          { id: '3', name: 'Tour Río Meta', price: 120000, stock_actual: 100 },
        ]);
        const status = await saritaAPI.sync.getStatus();
        setSyncStatus(status);
      }
    };
    loadInitialData();
  }, []);

  const addToCart = (product: Product) => {
    setCart(prev => {
      const existing = prev.find(item => item.id === product.id);
      if (existing) {
        return prev.map(item => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item);
      }
      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (id: string) => {
    setCart(prev => prev.filter(item => item.id !== id));
  };

  const calculateTotal = () => cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  const handleSale = async () => {
    if (cart.length === 0) return;
    setIsProcessing(true);

    const sale = {
      id: `SALE-${Date.now()}`,
      total: calculateTotal(),
      payment_method: paymentMethod,
      items: cart.map(item => ({ id: item.id, quantity: item.quantity, price: item.price })),
      timestamp: new Date().toISOString()
    };

    try {
      const saritaAPI = (window as any).saritaAPI;
      if (saritaAPI) {
        await saritaAPI.pos.saveSale(sale);
        await saritaAPI.hardware.printReceipt({ ...sale, company: 'SARITA POS' });
        setCart([]);
        alert('Venta registrada con éxito (Local/Sync)');
      }
    } catch (error) {
      console.error('POS: Error processing sale', error);
    } finally {
      setIsProcessing(false);
    }
  };

  const filteredProducts = products.filter(p =>
    p.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="grid grid-cols-12 gap-6 h-[calc(100vh-200px)]">
      {/* Left Column: Product Selection */}
      <div className="col-span-8 flex flex-col gap-4">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
          <input
            type="text"
            placeholder="Buscar producto o servicio..."
            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary outline-none"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        <div className="grid grid-cols-3 gap-4 overflow-y-auto pr-2">
          {filteredProducts.map(product => (
            <div
              key={product.id}
              onClick={() => addToCart(product)}
              className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm hover:border-primary cursor-pointer transition group"
            >
              <div className="w-12 h-12 bg-gray-50 rounded-lg flex items-center justify-center mb-3 group-hover:bg-primary/10 transition">
                <Package className="text-gray-400 group-hover:text-primary" size={24} />
              </div>
              <h3 className="font-bold text-gray-800 line-clamp-1">{product.name}</h3>
              <p className="text-primary font-bold mt-1">${product.price.toLocaleString()} COP</p>
              <p className="text-xs text-gray-400 mt-2">Stock: {product.stock_actual}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Right Column: Cart & Checkout */}
      <div className="col-span-4 bg-white rounded-2xl border border-gray-200 shadow-sm flex flex-col overflow-hidden">
        <div className="p-6 border-b border-gray-100 flex justify-between items-center">
          <h2 className="text-lg font-bold flex items-center gap-2">
            <ShoppingCart size={20} className="text-primary" /> Carrito
          </h2>
          <div className={clsx(
            "flex items-center gap-1 text-[10px] font-bold px-2 py-1 rounded-full",
            syncStatus.online ? "bg-green-100 text-green-700" : "bg-orange-100 text-orange-700"
          )}>
            {syncStatus.online ? <Wifi size={12} /> : <WifiOff size={12} />}
            {syncStatus.online ? 'EN LÍNEA' : 'MODO OFFLINE'}
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {cart.length === 0 ? (
            <div className="text-center py-10">
              <Package size={40} className="mx-auto text-gray-200 mb-2" />
              <p className="text-gray-400 text-sm">El carrito está vacío</p>
            </div>
          ) : (
            cart.map(item => (
              <div key={item.id} className="flex justify-between items-center gap-4">
                <div className="flex-1">
                  <p className="font-bold text-sm text-gray-800">{item.name}</p>
                  <p className="text-xs text-gray-400">{item.quantity} x ${item.price.toLocaleString()}</p>
                </div>
                <div className="flex items-center gap-3">
                  <p className="font-bold text-sm text-gray-800">${(item.price * item.quantity).toLocaleString()}</p>
                  <button onClick={() => removeFromCart(item.id)} className="text-gray-300 hover:text-red-500 transition">
                    <Trash2 size={16} />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        <div className="p-6 bg-gray-50 border-t border-gray-100 space-y-4">
          <div className="flex justify-between items-center">
            <span className="text-gray-500">Total</span>
            <span className="text-2xl font-black text-primary">${calculateTotal().toLocaleString()} COP</span>
          </div>

          <div className="grid grid-cols-3 gap-2">
            <button
              onClick={() => setPaymentMethod('EFECTIVO')}
              className={clsx(
                "flex flex-col items-center justify-center gap-1 p-2 rounded-lg border transition text-[10px] font-bold",
                paymentMethod === 'EFECTIVO' ? "bg-primary text-white border-primary" : "bg-white text-gray-400 border-gray-200 hover:border-primary"
              )}
            >
              <Banknote size={18} /> EFECTIVO
            </button>
            <button
              onClick={() => setPaymentMethod('WALLET')}
              className={clsx(
                "flex flex-col items-center justify-center gap-1 p-2 rounded-lg border transition text-[10px] font-bold",
                paymentMethod === 'WALLET' ? "bg-primary text-white border-primary" : "bg-white text-gray-400 border-gray-200 hover:border-primary"
              )}
            >
              <Wallet size={18} /> WALLET
            </button>
            <button
              onClick={() => setPaymentMethod('TARJETA')}
              className={clsx(
                "flex flex-col items-center justify-center gap-1 p-2 rounded-lg border transition text-[10px] font-bold",
                paymentMethod === 'TARJETA' ? "bg-primary text-white border-primary" : "bg-white text-gray-400 border-gray-200 hover:border-primary"
              )}
            >
              <CreditCard size={18} /> TARJETA
            </button>
          </div>

          <button
            disabled={cart.length === 0 || isProcessing}
            onClick={handleSale}
            className="w-full bg-green-600 hover:bg-green-700 disabled:bg-gray-300 text-white py-4 rounded-xl font-bold flex items-center justify-center gap-2 transition shadow-lg shadow-green-200"
          >
            <CheckCircle size={20} /> {isProcessing ? 'PROCESANDO...' : 'FINALIZAR VENTA'}
          </button>
        </div>
      </div>
    </div>
  );
};
