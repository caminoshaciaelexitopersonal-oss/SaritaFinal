'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { FiPhone, FiUser, FiCheckCircle, FiAlertTriangle, FiCamera } from 'react-icons/fi';
import { useRouter } from 'next/navigation';
import { toast } from 'react-toastify';

export default function IdentityProtectionPage() {
  const router = useRouter();
  const [status, setStatus] = useState<any>(null);
  const [step, setStep] = useState<'status' | 'phone' | 'face'>('status');
  const [phone, setPhone] = useState('');
  const [otp, setOtp] = useState('');
  const [loading, setLoading] = useState(false);

  const loadStatus = async () => {
    try {
      const { data } = await api.get('/social/protection/status/');
      setStatus(data);
      if (data.is_protected) {
          toast.success("Identidad Verificada. Acceso concedido.");
          router.push('/dashboard/social');
      }
    } catch (e) {}
  };

  useEffect(() => { loadStatus(); }, []);

  const handleVerifyPhone = async () => {
    setLoading(true);
    try {
      await api.post('/social/protection/verify-phone/', { phone, otp });
      toast.success("Teléfono verificado.");
      await loadStatus();
      setStep('status');
    } catch (e: any) {
      toast.error(e.response?.data?.error || "Error al verificar OTP.");
    } finally { setLoading(false); }
  };

  const handleVerifyFace = async () => {
    setLoading(true);
    try {
      // Simulando captura de imagen base64
      const mockImage = "data:image/jpeg;base64,...(long_string)...";
      await api.post('/social/protection/verify-face/', { image: mockImage });
      toast.success("Rostro verificado biométricamente.");
      await loadStatus();
      setStep('status');
    } catch (e: any) {
      toast.error(e.response?.data?.error || "Error en validación biométrica.");
    } finally { setLoading(false); }
  };

  if (!status) return <div className="p-10 text-center animate-pulse">Iniciando SADI-PROTECT...</div>;

  return (
    <div className="max-w-2xl mx-auto py-12 px-6 space-y-8 animate-in fade-in duration-500">
      <div className="text-center space-y-2">
        <h1 className="text-4xl font-black text-slate-900 tracking-tight uppercase">Protección de Identidad</h1>
        <p className="text-slate-500 font-medium italic">Garantizando un ecosistema social seguro y libre de suplantaciones.</p>
      </div>

      {step === 'status' && (
        <Card className="border-none shadow-2xl rounded-[3rem] overflow-hidden bg-white">
          <CardHeader className="p-10 bg-slate-900 text-white">
            <CardTitle className="text-2xl font-bold flex items-center gap-3">
               <FiUser className="text-indigo-400" /> Estado de Verificación
            </CardTitle>
          </CardHeader>
          <CardContent className="p-10 space-y-8">
            <div className="flex items-center justify-between p-6 bg-slate-50 rounded-3xl">
              <div className="flex items-center gap-4">
                <div className={`p-3 rounded-2xl ${status.phone_verified ? 'bg-emerald-100 text-emerald-600' : 'bg-amber-100 text-amber-600'}`}>
                  <FiPhone size={24} />
                </div>
                <div>
                  <p className="font-bold text-slate-800">Validación Telefónica (OTP)</p>
                  <p className="text-xs text-slate-500">{status.phone_verified ? 'Sincronizado' : 'Pendiente de validación'}</p>
                </div>
              </div>
              {status.phone_verified ? <FiCheckCircle className="text-emerald-500" size={24} /> : (
                <Button size="sm" onClick={() => setStep('phone')} className="bg-slate-900 text-white font-bold rounded-xl">Validar</Button>
              )}
            </div>

            <div className="flex items-center justify-between p-6 bg-slate-50 rounded-3xl">
              <div className="flex items-center gap-4">
                <div className={`p-3 rounded-2xl ${status.face_verified ? 'bg-emerald-100 text-emerald-600' : 'bg-amber-100 text-amber-600'}`}>
                  <FiCamera size={24} />
                </div>
                <div>
                  <p className="font-bold text-slate-800">Reconocimiento Facial Biométrico</p>
                  <p className="text-xs text-slate-500">{status.face_verified ? 'Verificado' : 'Requiere escaneo activo'}</p>
                </div>
              </div>
              {status.face_verified ? <FiCheckCircle className="text-emerald-500" size={24} /> : (
                <Button size="sm" onClick={() => setStep('face')} className="bg-slate-900 text-white font-bold rounded-xl">Escanear</Button>
              )}
            </div>

            {!status.is_protected && (
              <div className="p-6 bg-amber-50 border border-amber-100 rounded-3xl flex gap-4 text-amber-800">
                <FiAlertTriangle className="shrink-0" size={24} />
                <p className="text-sm font-medium">Debes completar ambos pasos para habilitar las funciones de chat y video citas en la Super App Social.</p>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {step === 'phone' && (
        <Card className="border-none shadow-xl rounded-[2.5rem] bg-white">
          <CardContent className="p-10 space-y-6">
            <h3 className="text-xl font-bold text-slate-900">Validación de Número</h3>
            <div className="space-y-4">
               <input
                 type="text" placeholder="Número Telefónico" value={phone}
                 onChange={e => setPhone(e.target.value)}
                 className="w-full p-4 bg-slate-50 rounded-2xl border-none outline-none focus:ring-2 ring-indigo-500/20 font-bold"
               />
               <input
                 type="text" placeholder="Código OTP (Prueba: 123456)" value={otp}
                 onChange={e => setOtp(e.target.value)}
                 className="w-full p-4 bg-slate-50 rounded-2xl border-none outline-none focus:ring-2 ring-indigo-500/20 font-bold tracking-[1em] text-center"
               />
               <Button onClick={handleVerifyPhone} disabled={loading} className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-black py-4 rounded-2xl shadow-lg shadow-indigo-100 transition-all">
                 {loading ? 'Validando...' : 'Confirmar Código'}
               </Button>
               <Button variant="ghost" onClick={() => setStep('status')} className="w-full font-bold text-slate-400">Volver</Button>
            </div>
          </CardContent>
        </Card>
      )}

      {step === 'face' && (
        <Card className="border-none shadow-xl rounded-[2.5rem] bg-white">
          <CardContent className="p-10 space-y-8 text-center">
            <div className="w-48 h-48 bg-slate-100 rounded-full mx-auto flex items-center justify-center border-4 border-dashed border-slate-200">
               <FiCamera size={64} className="text-slate-300" />
            </div>
            <div className="space-y-2">
               <h3 className="text-xl font-bold text-slate-900">Escaneo Biométrico</h3>
               <p className="text-sm text-slate-500">Posicione su rostro frente a la cámara y asegure buena iluminación para la validación de identidad SADI.</p>
            </div>
            <Button onClick={handleVerifyFace} disabled={loading} className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-black py-4 rounded-2xl shadow-lg shadow-emerald-100 transition-all">
               {loading ? 'Procesando Biometría...' : 'Iniciar Captura'}
            </Button>
            <Button variant="ghost" onClick={() => setStep('status')} className="w-full font-bold text-slate-400">Volver</Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
