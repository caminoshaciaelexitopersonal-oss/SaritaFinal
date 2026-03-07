export * from './explore/ExploreScreen';
export * from './bookings/BookingsScreen';
export * from './profile/ProfileScreen';
export * from './favorites/FavoritesScreen';
export * from './search/SearchScreen';

// Pantallas simples placeholders
import React from 'react';
import { View, Text } from 'react-native';

export const HomeScreen = () => (
  <View style={{flex:1, justifyContent:'center', alignItems:'center'}}><Text>Home Screen</Text></View>
);

export const MessagesScreen = () => (
  <View style={{flex:1, justifyContent:'center', alignItems:'center'}}><Text>Messages Screen</Text></View>
);
