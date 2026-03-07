import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const LoginScreen = () => (
  <View style={styles.container}><Text>Login Screen</Text></View>
);

export const HomeScreen = () => (
  <View style={styles.container}><Text>Home Screen</Text></View>
);

export const ExploreScreen = () => (
  <View style={styles.container}><Text>Explore Screen</Text></View>
);

export const BookingsScreen = () => (
  <View style={styles.container}><Text>Bookings Screen</Text></View>
);

export const MessagesScreen = () => (
  <View style={styles.container}><Text>Messages Screen</Text></View>
);

export const ProfileScreen = () => (
  <View style={styles.container}><Text>Profile Screen</Text></View>
);

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' }
});
