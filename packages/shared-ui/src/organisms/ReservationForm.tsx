import React from 'react';
import { Card } from '../molecules/Card';
import { Text } from '../atoms/Text';
import { Input } from '../atoms/Input';
import { Button } from '../atoms/Button';
import { View, StyleSheet } from 'react-native';

export const ReservationForm: React.FC<{ onSubmit: (data: any) => void; initialData?: any }> = ({ onSubmit, initialData }) => {
  const [form, setForm] = React.useState(initialData || {
    client: '',
    service: '',
    date: '',
    notes: ''
  });

  return (
    <Card>
      <View style={styles.container}>
        <Text variant="headingS">Nueva Reserva</Text>
        <Input
          placeholder="Nombre del Cliente"
          value={form.client}
          onChange={(v) => setForm({...form, client: v})}
        />
        <Input
          placeholder="Servicio / Experiencia"
          value={form.service}
          onChange={(v) => setForm({...form, service: v})}
        />
        <Input
          placeholder="Fecha (AAAA-MM-DD)"
          value={form.date}
          onChange={(v) => setForm({...form, date: v})}
        />
        <Button label="Guardar Reserva" onPress={() => onSubmit(form)} />
      </View>
    </Card>
  );
};

const styles = StyleSheet.create({
  container: { gap: 16 }
});
