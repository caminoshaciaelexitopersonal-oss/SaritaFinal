import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import axios from 'axios';

export default function InvoiceGenerator({ orderId }) {
  const [loading, setLoading] = useState(false);

  const generateInvoice = async () => {
    setLoading(true);
    try {
      // Reutiliza BillingService via API
      const response = await axios.post('/api/v1/mi-negocio/invoices/', { order_id: orderId });
      Alert.alert("Éxito", "Factura generada: " + response.data.invoice_number);
    } catch (error) {
      Alert.alert("Error", "No se pudo generar la factura");
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Generador de Facturas</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={generateInvoice}
        disabled={loading}
      >
        <Text style={styles.buttonText}>{loading ? 'Procesando...' : 'Generar Factura'}</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 16, backgroundColor: '#fff', borderRadius: 8 },
  title: { fontSize: 18, fontWeight: 'bold', marginBottom: 12 },
  button: { backgroundColor: '#007AFF', padding: 12, borderRadius: 6, alignItems: 'center' },
  buttonText: { color: '#fff', fontWeight: '600' }
});
