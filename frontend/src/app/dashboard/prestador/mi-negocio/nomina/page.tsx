"use client";

import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useMiNegocioApi, Nomina } from "../../hooks/useMiNegocioApi";

const procesarSchema = z.object({
  fecha_inicio: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Fecha inválida."),
  fecha_fin: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Fecha inválida."),
}).refine(data => new Date(data.fecha_inicio) <= new Date(data.fecha_fin), {
  message: "La fecha de inicio no puede ser posterior a la fecha de fin.",
  path: ["fecha_fin"],
});

export default function NominaPage() {
  const { getNominas, procesarNomina } = useMiNegocioApi();
  const [nominas, setNominas] = useState<Nomina[]>([]);

  const form = useForm<{ fecha_inicio: string, fecha_fin: string }>({
    resolver: zodResolver(procesarSchema),
  });

  useEffect(() => {
    const fetchNominas = async () => {
      const data = await getNominas();
      if (data) setNominas(data);
    };
    fetchNominas();
  }, [getNominas]);

  const onSubmit = async (values: { fecha_inicio: string, fecha_fin: string }) => {
    const nuevaNomina = await procesarNomina(values.fecha_inicio, values.fecha_fin);
    if (nuevaNomina) {
      setNominas([nuevaNomina, ...nominas]);
      form.reset();
    }
  };

  return (
    <div className="p-4 md:p-6 space-y-6">
      <h1 className="text-2xl font-bold">Módulo de Nómina</h1>

      <Card>
        <CardHeader><CardTitle>Procesar Nueva Nómina</CardTitle></CardHeader>
        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="flex items-end gap-4">
              <FormField name="fecha_inicio" render={({ field }) => (
                <FormItem><FormLabel>Fecha de Inicio</FormLabel><FormControl><Input type="date" {...field} /></FormControl><FormMessage /></FormItem>
              )} />
              <FormField name="fecha_fin" render={({ field }) => (
                <FormItem><FormLabel>Fecha de Fin</FormLabel><FormControl><Input type="date" {...field} /></FormControl><FormMessage /></FormItem>
              )} />
              <Button type="submit">Procesar</Button>
            </form>
          </Form>
        </CardContent>
      </Card>

      <Card>
        <CardHeader><CardTitle>Historial de Nóminas</CardTitle></CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Período</TableHead>
                <TableHead>Estado</TableHead>
                <TableHead className="text-right">Neto a Pagar</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {nominas.map((nomina) => (
                <TableRow key={nomina.id}>
                  <TableCell>{nomina.fecha_inicio} al {nomina.fecha_fin}</TableCell>
                  <TableCell>{nomina.estado}</TableCell>
                  <TableCell className="text-right">{new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(parseFloat(nomina.neto_a_pagar))}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
