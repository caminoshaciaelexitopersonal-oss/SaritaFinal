import React from 'react';
import { View, Text, Dimensions } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

export default function InstitutionalReports({ data }) {
  return (
    <View style={{ marginVertical: 16 }}>
      <Text style={{ fontSize: 20, fontWeight: 'bold', marginLeft: 16 }}>Reporte de Ingresos</Text>
      <LineChart
        data={{
          labels: ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
          datasets: [{ data: data || [20, 45, 28, 80, 99, 43] }]
        }}
        width={Dimensions.get("window").width - 32}
        height={220}
        chartConfig={{
          backgroundColor: "#e26a00",
          backgroundGradientFrom: "#fb8c00",
          backgroundGradientTo: "#ffa726",
          decimalPlaces: 2,
          color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
          style: { borderRadius: 16 }
        }}
        bezier
        style={{ marginVertical: 8, borderRadius: 16, alignSelf: 'center' }}
      />
    </View>
  );
}
