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
  SearchScreen,
  AISearchScreen,
  CreatorDashboard,
  CommunityScreen,
  EducationScreen,
  ReputationScreen,
  DestinationDashboard
} from '../screens';
import { TravelFeedScreen } from '../screens/feed/TravelFeedScreen';
import { PassportScreen } from '../screens/passport/PassportScreen';
import { LiveTourScreen } from '../screens/live/LiveTourScreen';
import { SmartMapScreen } from '../screens/map/SmartMapScreen';
import { TourDetailScreen } from '../screens/tour/TourDetailScreen';
import { MapScreen } from '../screens/map/MapScreen';
import { BookingScreen } from '../screens/booking/BookingScreen';
import { ChatScreen } from '../screens/chat/ChatScreen';
import { VirtualGuideScreen } from '../screens/ai/VirtualGuideScreen';
import { TransportScreen } from '../screens/transport/TransportScreen';
import { ExtensionsMarketplaceScreen } from '../screens/extensions/ExtensionsMarketplaceScreen';
import { ARDiscoveryScreen } from '../screens/ar/ARDiscoveryScreen';
import { TourTrackingScreen } from '../screens/tracking/TourTrackingScreen';
import { ReviewScreen } from '../screens/review/ReviewScreen';
import { HistoryScreen } from '../screens/history/HistoryScreen';
import { SupportScreen } from '../screens/support/SupportScreen';
import { OperatorDashboard } from '../screens/operator/OperatorDashboard';
import { LoyaltyScreen } from '../screens/loyalty/LoyaltyScreen';
import { TripPlannerScreen } from '../screens/planner/TripPlannerScreen';
import { AdminDashboard } from '../screens/admin/AdminDashboard';
import { ResearchPortalScreen } from '../screens/research/ResearchPortalScreen';
import { GlobalControlCenterScreen } from '../screens/control_center/GlobalControlCenterScreen';
import { GlobalNetworkScreen } from '../screens/global_network/GlobalNetworkScreen';
import { SystemObservabilityScreen } from '../screens/monitoring/SystemObservabilityScreen';
import { DigitalTwinScreen } from '../screens/digital_twin/DigitalTwinScreen';
import { SimulationEngineScreen } from '../screens/simulation/SimulationEngineScreen';
import { CountryDashboard } from '../screens/country_management/CountryDashboard';
import { HyperPersonalizedScreen } from '../screens/personalization/HyperPersonalizedScreen';
import { OpenDataPortalScreen } from '../screens/open_data/OpenDataPortalScreen';
import { TravelOrchestratorScreen } from '../screens/orchestration/TravelOrchestratorScreen';
import { ContextualExperiencesScreen } from '../screens/orchestration/ContextualExperiencesScreen';
import { UrbanServicesScreen } from '../screens/urban/UrbanServicesScreen';
import { SustainabilityDashboard } from '../screens/sustainability/SustainabilityDashboard';
import { EconomyDashboard } from '../screens/economy/EconomyDashboard';
import { LiveExperiencesScreen } from '../screens/orchestration/LiveExperiencesScreen';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

const ExploreStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="ExploreList" component={ExploreScreen} options={{ title: 'Explorar' }} />
    <Stack.Screen name="TourDetail" component={TourDetailScreen} options={{ title: 'Detalle del Tour' }} />
    <Stack.Screen name="Booking" component={BookingScreen} options={{ title: 'Reservar' }} />
    <Stack.Screen name="Map" component={MapScreen} options={{ title: 'Mapa' }} />
    <Stack.Screen name="SmartMap" component={SmartMapScreen} options={{ title: 'Explora tu entorno' }} />
    <Stack.Screen name="VirtualGuide" component={VirtualGuideScreen} options={{ title: 'Guía Virtual IA' }} />
    <Stack.Screen name="Transport" component={TransportScreen} options={{ title: 'Transporte Regional' }} />
    <Stack.Screen name="Extensions" component={ExtensionsMarketplaceScreen} options={{ title: 'Extensiones' }} />
    <Stack.Screen name="ARDiscovery" component={ARDiscoveryScreen} options={{ title: 'Descubrimiento AR' }} />
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

import { PaymentScreen } from '../screens/payment/PaymentScreen';
import { TicketScreen } from '../screens/ticket/TicketScreen';

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
    <Tab.Screen name="Feed" component={TravelFeedScreen} options={{ title: 'Experiencias', headerShown: false }} />
    <Tab.Screen name="Passport" component={PassportScreen} options={{ title: 'Pasaporte', headerShown: true }} />
    <Tab.Screen name="Live" component={LiveTourScreen} options={{ title: 'En Vivo', headerShown: false }} />
    <Tab.Screen name="Creator" component={CreatorDashboard} options={{ title: 'Creador', headerShown: true }} />
    <Tab.Screen name="Destination" component={DestinationDashboard} options={{ title: 'Destino', headerShown: true }} />
    <Tab.Screen name="Orchestrator" component={TravelOrchestratorScreen} options={{ title: 'Orquestador', headerShown: true }} />
    <Tab.Screen name="Contextual" component={ContextualExperiencesScreen} options={{ title: 'Cerca de mí', headerShown: true }} />
    <Tab.Screen name="Urban" component={UrbanServicesScreen} options={{ title: 'Ciudad', headerShown: true }} />
    <Tab.Screen name="Sustainability" component={SustainabilityDashboard} options={{ title: 'Impacto', headerShown: true }} />
    <Tab.Screen name="Economy" component={EconomyDashboard} options={{ title: 'Monedero', headerShown: true }} />
    <Tab.Screen name="LiveNow" component={LiveExperiencesScreen} options={{ title: 'En Vivo!', headerShown: true }} />
    <Tab.Screen name="GlobalIntel" component={GlobalAnalyticsDashboard} options={{ title: 'Global', headerShown: true }} />
    <Tab.Screen name="Country" component={CountryDashboard} options={{ title: 'País', headerShown: true }} />
    <Tab.Screen name="Personalized" component={HyperPersonalizedScreen} options={{ title: 'Para ti', headerShown: true }} />
    <Tab.Screen name="OpenData" component={OpenDataPortalScreen} options={{ title: 'Datos', headerShown: true }} />
    <Tab.Screen name="Community" component={CommunityScreen} options={{ title: 'Comunidad', headerShown: true }} />
    <Tab.Screen name="Education" component={EducationScreen} options={{ title: 'Aula', headerShown: true }} />
    <Tab.Screen name="Reputation" component={ReputationScreen} options={{ title: 'Confianza', headerShown: true }} />
    <Tab.Screen name="GlobalNet" component={GlobalNetworkScreen} options={{ title: 'Red', headerShown: true }} />
    <Tab.Screen name="Observability" component={SystemObservabilityScreen} options={{ title: 'Monitor', headerShown: true }} />
    <Tab.Screen name="Twin" component={DigitalTwinScreen} options={{ title: 'Twin', headerShown: true }} />
    <Tab.Screen name="Sim" component={SimulationEngineScreen} options={{ title: 'Sim', headerShown: true }} />
    <Tab.Screen name="Control" component={GlobalControlCenterScreen} options={{ title: 'Control', headerShown: true }} />
    <Tab.Screen name="Research" component={ResearchPortalScreen} options={{ title: 'I+D', headerShown: true }} />
    <Tab.Screen name="Admin" component={AdminDashboard} options={{ title: 'Torre', headerShown: true }} />
  </Tab.Navigator>
);
