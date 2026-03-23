import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';
import Constants from 'expo-constants';

/**
 * Hallazgo 10: Sistema de Notificaciones Push.
 * Configura y gestiona el registro de tokens FCM en el dispositivo.
 */

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: false,
  }),
});

export async function registerForPushNotificationsAsync() {
  let token;

  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('default', {
      name: 'default',
      importance: Notifications.AndroidImportance.MAX,
      vibrationPattern: [0, 250, 250, 250],
      lightColor: '#FF231F7C',
    });
  }

  const { status: existingStatus } = await Notifications.getPermissionsAsync();
  let finalStatus = existingStatus;

  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync();
    finalStatus = status;
  }

  if (finalStatus !== 'granted') {
    console.error('SARITA: Error al obtener permisos para notificaciones push');
    return;
  }

  try {
    const projectId = Constants.expoConfig?.extra?.eas?.projectId || Constants.expoConfig?.owner;
    token = (await Notifications.getExpoPushTokenAsync({ projectId })).data;
    console.log('SARITA FCM Token:', token);
  } catch (e) {
    console.error('SARITA: Error obteniendo el token:', e);
  }

  return token;
}
