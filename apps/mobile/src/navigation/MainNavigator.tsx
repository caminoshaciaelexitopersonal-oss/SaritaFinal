import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { HomeScreen, ExploreScreen, BookingsScreen, MessagesScreen, ProfileScreen } from '../screens';

const Tab = createBottomTabNavigator();

export const MainNavigator = () => (
  <Tab.Navigator>
    <Tab.Screen name="Home" component={HomeScreen} />
    <Tab.Screen name="Explore" component={ExploreScreen} />
    <Tab.Screen name="Bookings" component={BookingsScreen} />
    <Tab.Screen name="Messages" component={MessagesScreen} />
    <Tab.Screen name="Profile" component={ProfileScreen} />
  </Tab.Navigator>
);
