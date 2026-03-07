import React, { useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';
import { registerForPushNotificationsAsync } from './src/services/pushNotificationService';
import { initGeofenceMonitoring } from './src/services/geofenceService';
import { initDatabase } from './src/storage/database';

/**
 * SARITA Mobile App Entry Point (Fase 9: Realidad del Sistema)
 *
 * Esta aplicación funciona exclusivamente como cliente del API de SARITA.
 * No contiene lógica de negocio central, solo captura de datos en campo
 * y visualización para el Prestador (Vía 2).
 */

export default function App() {
  useEffect(() => {
    // Inicialización de servicios nativos de clase mundial
    const initServices = async () => {
      console.log('SARITA: Iniciando servicios móviles...');

      // 1. Registro para Notificaciones Push (Hallazgo 10)
      await registerForPushNotificationsAsync();

      // 2. Monitoreo de Geofencing (Hallazgo 11)
      await initGeofenceMonitoring();

      // 3. Inicialización de DB Offline (Fase 9)
      await initDatabase();
    };

    initServices();
  }, []);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>SARITA Mobile</Text>
        <Text style={styles.subtitle}>Gestión para Prestadores de Servicios Turísticos</Text>
      </View>

      <View style={styles.content}>
        <Text style={styles.statusText}>Estado del Sistema: Conectado al API Gateway</Text>
        <Text style={styles.infoText}>Versión 1.0.0 (Production-Ready Infrastructure)</Text>
      </View>

      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    padding: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1a1a1a',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
  },
  content: {
    marginTop: 40,
    padding: 20,
    backgroundColor: '#f8f9fa',
    borderRadius: 10,
    width: '90%',
    alignItems: 'center',
  },
  statusText: {
    fontSize: 14,
    color: '#28a745',
    fontWeight: '600',
  },
  infoText: {
    fontSize: 12,
    color: '#999',
    marginTop: 10,
  }
});
