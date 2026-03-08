export * from './HomeScreen';
export * from './explore/ExploreScreen';
export * from './bookings/BookingsScreen';
export * from './profile/ProfileScreen';
export * from './favorites/FavoritesScreen';
export * from './search/SearchScreen';
export * from './ai/AISearchScreen';
export * from './loyalty/LoyaltyScreen';
export * from './planner/TripPlannerScreen';
export * from './feed/TravelFeedScreen';
export * from './passport/PassportScreen';
export * from './live/LiveTourScreen';
export * from './operator/OperatorDashboard';
export * from './admin/AdminDashboard';
export * from './creator/CreatorDashboard';
export * from './community/CommunityScreen';
export * from './education/EducationScreen';
export * from './operator/ReputationScreen';
export * from './destination/DestinationDashboard';
export * from './orchestration/TravelOrchestratorScreen';
export * from './orchestration/ContextualExperiencesScreen';
export * from './orchestration/LiveExperiencesScreen';
export * from './urban/UrbanServicesScreen';
export * from './sustainability/SustainabilityDashboard';
export * from './economy/EconomyDashboard';
export * from './global_network/GlobalNetworkScreen';
export * from './monitoring/SystemObservabilityScreen';

import React from 'react';
import { View, Text } from 'react-native';

export const MessagesScreen = () => (
  <View style={{flex:1, justifyContent:'center', alignItems:'center'}}><Text>Messages Screen</Text></View>
);
