import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { useAuth } from '../context/AuthContext';
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
  DestinationDashboard,
  WalletHomeScreen,
  WalletBalanceScreen,
  WalletTransactionsScreen,
  WalletRewardsScreen,
  DeliveryHomeScreen,
  RestaurantListScreen,
  ProductListScreen,
  ProductDetailsScreen,
  CartScreen,
  OrderTrackingScreen,
  BusinessDashboard,
  BusinessServicesScreen,
  BusinessOrdersScreen,
  BusinessCustomersScreen,
  BusinessFinanceScreen,
  BusinessAccountingScreen,
  BusinessDocumentsScreen
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
import { GlobalAIDashboard } from '../screens/autonomous/GlobalAIDashboard';
import { AutonomousPlanningScreen } from '../screens/autonomous/AutonomousPlanningScreen';
import { GlobalAlertsScreen } from '../screens/alerts/GlobalAlertsScreen';
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
import { PaymentScreen } from '../screens/payment/PaymentScreen';
import { TicketScreen } from '../screens/ticket/TicketScreen';

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

const WalletStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="WalletHome" component={WalletHomeScreen} options={{ title: 'Mi Billetera' }} />
    <Stack.Screen name="WalletBalance" component={WalletBalanceScreen} options={{ title: 'Mi Saldo' }} />
    <Stack.Screen name="WalletTopUp" component={WalletTopUpScreen} options={{ title: 'Recargar' }} />
    <Stack.Screen name="WalletTransactions" component={WalletTransactionsScreen} options={{ title: 'Transacciones' }} />
    <Stack.Screen name="WalletRewards" component={WalletRewardsScreen} options={{ title: 'Recompensas' }} />
  </Stack.Navigator>
);

const DeliveryStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="DeliveryHome" component={DeliveryHomeScreen} options={{ title: 'Delivery' }} />
    <Stack.Screen name="RestaurantList" component={RestaurantListScreen} options={{ title: 'Restaurantes' }} />
    <Stack.Screen name="ProductList" component={ProductListScreen} options={{ title: 'Menú' }} />
    <Stack.Screen name="ProductDetails" component={ProductDetailsScreen} options={{ title: 'Plato' }} />
    <Stack.Screen name="Cart" component={CartScreen} options={{ title: 'Carrito' }} />
    <Stack.Screen name="OrderTracking" component={OrderTrackingScreen} options={{ title: 'Rastreo Pedido' }} />
  </Stack.Navigator>
);

const BusinessStack = () => (
  <Stack.Navigator>
    <Stack.Screen name="BusinessDashboard" component={BusinessDashboard} options={{ title: 'Dashboard ERP' }} />
    <Stack.Screen name="BusinessServices" component={BusinessServicesScreen} options={{ title: 'Mis Servicios' }} />
    <Stack.Screen name="BusinessOrders" component={BusinessOrdersScreen} options={{ title: 'Órdenes ERP' }} />
    <Stack.Screen name="BusinessCustomers" component={BusinessCustomersScreen} options={{ title: 'Mis Clientes' }} />
    <Stack.Screen name="BusinessFinance" component={BusinessFinanceScreen} options={{ title: 'Finanzas ERP' }} />
    <Stack.Screen name="BusinessAccounting" component={BusinessAccountingScreen} options={{ title: 'Contabilidad' }} />
    <Stack.Screen name="BusinessReports" component={BusinessReportsScreen} options={{ title: 'Reportes ERP' }} />
    <Stack.Screen name="BusinessDocuments" component={BusinessDocumentsScreen} options={{ title: 'Documentación' }} />
  </Stack.Navigator>
);

export const MainNavigator = () => {
  const { user } = useAuth();
  const isBusiness = user?.role === 'provider' || user?.role === 'operator';

  return (
    <Tab.Navigator screenOptions={{ headerShown: false }}>
      {/* VÍA 1: USUARIOS / VIAJEROS */}
      {!isBusiness && (
        <>
          <Tab.Screen name="Home" component={HomeScreen} options={{ title: 'Inicio' }} />
          <Tab.Screen name="ExploreTab" component={ExploreStack} options={{ title: 'Explorar' }} />
          <Tab.Screen name="BookingsTab" component={BookingsStack} options={{ title: 'Reservas' }} />
          <Tab.Screen name="WalletTab" component={WalletStack} options={{ title: 'Billetera' }} />
          <Tab.Screen name="DeliveryTab" component={DeliveryStack} options={{ title: 'Delivery' }} />
          <Tab.Screen name="Feed" component={TravelFeedScreen} options={{ title: 'Experiencias', headerShown: false }} />
          <Tab.Screen name="Passport" component={PassportScreen} options={{ title: 'Pasaporte', headerShown: true }} />
        </>
      )}

      {/* VÍA 2: EMPRESARIOS / PRESTADORES */}
      {isBusiness && (
        <>
          <Tab.Screen name="BusinessTab" component={BusinessStack} options={{ title: 'Mi Negocio' }} />
          <Tab.Screen name="Operator" component={OperatorDashboard} options={{ title: 'Mercado', headerShown: true }} />
          <Tab.Screen name="Reputation" component={ReputationScreen} options={{ title: 'Confianza', headerShown: true }} />
          <Tab.Screen name="Live" component={LiveTourScreen} options={{ title: 'Transmisión', headerShown: false }} />
        </>
      )}

      {/* VÍA COMÚN Y ADMIN */}
      <Tab.Screen name="Profile" component={ProfileScreen} options={{ title: 'Perfil', headerShown: true }} />

      {user?.role === 'admin' && (
        <>
          <Tab.Screen name="GlobalAI" component={GlobalAIDashboard} options={{ title: 'Cerebro', headerShown: true }} />
          <Tab.Screen name="Control" component={GlobalControlCenterScreen} options={{ title: 'Control', headerShown: true }} />
          <Tab.Screen name="Admin" component={AdminDashboard} options={{ title: 'Torre', headerShown: true }} />
        </>
      )}
    </Tab.Navigator>
  );
};
