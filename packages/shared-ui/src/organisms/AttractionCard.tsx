import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { View, Platform, StyleSheet, Image } from 'react-native';

interface Attraction {
  id: string;
  name: string;
  description: string;
  imageUrl: string;
  category: string;
}

interface AttractionCardProps {
  attraction: Attraction;
  onPress?: () => void;
}

export const AttractionCard: React.FC<AttractionCardProps> = ({ attraction, onPress }) => {
  const isWeb = Platform.OS === 'web';

  if (isWeb) {
    return (
      <Card padding="none" style={{ overflow: 'hidden', cursor: 'pointer' }} onClick={onPress}>
        <img src={attraction.imageUrl} alt={attraction.name} style={{ width: '100%', height: '200px', objectFit: 'cover' }} />
        <div style={{ padding: '16px' }}>
          <Text variant="small" color="primary" style={{ textTransform: 'uppercase', fontWeight: 'bold' }}>{attraction.category}</Text>
          <div style={{ marginTop: '4px' }}>
            <Text variant="headingS">{attraction.name}</Text>
          </div>
          <Text variant="caption" style={{ marginTop: '8px', display: 'block' }}>{attraction.description}</Text>
        </div>
      </Card>
    );
  }

  return (
    <Card padding="none" style={styles.nativeCard}>
      <Image source={{ uri: attraction.imageUrl }} style={styles.nativeImage} />
      <View style={styles.nativeContent}>
        <Text variant="small" color="primary" style={{ fontWeight: 'bold' }}>{attraction.category.toUpperCase()}</Text>
        <Text variant="headingS" style={{ marginTop: 4 }}>{attraction.name}</Text>
        <Text variant="caption" style={{ marginTop: 4 }}>{attraction.description}</Text>
      </View>
    </Card>
  );
};

const styles = StyleSheet.create({
  nativeCard: { overflow: 'hidden', marginBottom: 16 },
  nativeImage: { width: '100%', height: 180 },
  nativeContent: { padding: 12 }
});
