import * as SecureStore from 'expo-secure-store';

export async function saveToken(token: string) {
  try {
    await SecureStore.setItemAsync('sarita_token', token);
  } catch (error) {
    console.error('Error saving token to SecureStore:', error);
  }
}

export async function getToken() {
  try {
    return await SecureStore.getItemAsync('sarita_token');
  } catch (error) {
    console.error('Error getting token from SecureStore:', error);
    return null;
  }
}

export async function deleteToken() {
  try {
    await SecureStore.deleteItemAsync('sarita_token');
  } catch (error) {
    console.error('Error deleting token from SecureStore:', error);
  }
}
