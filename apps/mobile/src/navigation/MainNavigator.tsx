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
import { ChatScreen } from '../screens/chat/ChatScreen';
import { TourTrackingScreen } from '../screens/tracking/TourTrackingScreen';
import { ReviewScreen } from '../screens/review/ReviewScreen';
import { HistoryScreen } from '../screens/history/HistoryScreen';
import { SupportScreen } from '../screens/support/SupportScreen';
import { OperatorDashboard } from '../screens/operator/OperatorDashboard';
import { LoyaltyScreen } from '../screens/loyalty/LoyaltyScreen';
import { TripPlannerScreen } from '../screens/planner/TripPlannerScreen';
import { AdminDashboard } from '../screens/admin/AdminDashboard';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

const ExploreStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="ExploreList" component={ExploreScreen} options={{ title: 'Explorar' }} />
    <Stack.Screen name="TourDetail" component={TourDetailScreen} options={{ title: 'Detalle del Tour' }} />
    <Stack.Screen name="Booking" component={BookingScreen} options={{ title: 'Reservar' }} />
    <Stack.Screen name="Map" component={MapScreen} options={{ title: 'Mapa' }} />
    <Stack.Screen name="Payment" component={PaymentScreen} options={{ title: 'Pago Seguro' }} />
    <Stack.Screen name="Ticket" component={TicketScreen} options={{ title: 'Mi Ticket' }} />
    <Stack.Screen name="Chat" component={ChatScreen} options={{ title: 'Chat con Operador' }} />
    <Stack.Screen name="Tracking" component={TourTrackingScreen} options={{ title: 'Seguimiento del Tour' }} />
    <Stack.Screen name="Review" component={ReviewScreen} options={{ title: 'Calificar Tour' }} />
    <Stack.Screen name="History" component={HistoryScreen} options={{ title: 'Historial de Viajes' }} />
    <Stack.Screen name="Support" component={SupportScreen} options={{ title: 'Soporte Técnico' }} />
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
    <Tab.Screen name="Operator" component={OperatorDashboard} options={{ title: 'Negocio', headerShown: true }} />
    <Tab.Screen name="Loyalty" component={LoyaltyScreen} options={{ title: 'Club', headerShown: true }} />
    <Tab.Screen name="Planner" component={TripPlannerScreen} options={{ title: 'Planes', headerShown: true }} />
    <Tab.Screen name="Admin" component={AdminDashboard} options={{ title: 'Torre', headerShown: true }} />
  </Tab.Navigator>
);
