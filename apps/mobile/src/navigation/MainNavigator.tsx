import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import {
  HomeScreen,
  ExploreScreen,
  BookingsScreen,
  MessagesScreen,
  ProfileScreen,
  FavoritesScreen,
  SearchScreen
} from '../screens';
import { TourDetailScreen } from '../screens/tour/TourDetailScreen';
import { MapScreen } from '../screens/map/MapScreen';
import { BookingScreen } from '../screens/booking/BookingScreen';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

const ExploreStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="ExploreList" component={ExploreScreen} options={{ title: 'Explorar' }} />
    <Stack.Screen name="TourDetail" component={TourDetailScreen} options={{ title: 'Detalle del Tour' }} />
    <Stack.Screen name="Booking" component={BookingScreen} options={{ title: 'Reservar' }} />
    <Stack.Screen name="Map" component={MapScreen} options={{ title: 'Mapa' }} />
  </Stack.Navigator>
);

const BookingsStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="BookingsList" component={BookingsScreen} options={{ title: 'Mis Reservas' }} />
  </Stack.Navigator>
);

export const MainNavigator = () => (
  <Tab.Navigator screenOptions={{ headerShown: false }}>
    <Tab.Screen name="Home" component={HomeScreen} />
    <Tab.Screen name="ExploreTab" component={ExploreStack} options={{ title: 'Explorar' }} />
    <Tab.Screen name="BookingsTab" component={BookingsStack} options={{ title: 'Reservas' }} />
    <Tab.Screen name="Favorites" component={FavoritesScreen} options={{ title: 'Favoritos', headerShown: true }} />
    <Tab.Screen name="Profile" component={ProfileScreen} options={{ headerShown: true }} />
  </Tab.Navigator>
);
