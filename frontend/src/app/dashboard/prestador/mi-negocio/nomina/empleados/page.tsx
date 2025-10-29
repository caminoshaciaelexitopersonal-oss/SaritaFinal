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
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useMiNegocioApi, Empleado, CreateEmpleadoDTO } from "../../../../(authenticated)/prestador/mi-negocio/hooks/useMiNegocioApi";

// Esquema de validación para el formulario de empleado
const empleadoSchema = z.object({
  nombre: z.string().min(2, "El nombre es requerido."),
  apellido: z.string().min(2, "El apellido es requerido."),
  tipo_documento: z.enum(["CC", "CE", "PA"]),
  numero_documento: z.string().min(5, "El número de documento es requerido."),
  fecha_nacimiento: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Formato de fecha inválido (YYYY-MM-DD)."),
  fecha_contratacion: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Formato de fecha inválido (YYYY-MM-DD)."),
  salario_base: z.string().refine(val => !isNaN(parseFloat(val)) && parseFloat(val) > 0, {
    message: "El salario debe ser un número positivo.",
  }),
  activo: z.boolean().default(true),
});

export default function EmpleadosPage() {
  const { getEmpleados, createEmpleado } = useMiNegocioApi();
  const [empleados, setEmpleados] = useState<Empleado[]>([]);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const form = useForm<CreateEmpleadoDTO>({
    resolver: zodResolver(empleadoSchema),
    defaultValues: {
      nombre: "",
      apellido: "",
      tipo_documento: "CC",
      numero_documento: "",
      fecha_nacimiento: "",
      fecha_contratacion: "",
      salario_base: "0",
      activo: true,
    },
  });

  useEffect(() => {
    const fetchEmpleados = async () => {
      const data = await getEmpleados();
      if (data) setEmpleados(data);
    };
    fetchEmpleados();
  }, [getEmpleados]);

  const onSubmit = async (values: CreateEmpleadoDTO) => {
    const nuevoEmpleado = await createEmpleado(values);
    if (nuevoEmpleado) {
      setEmpleados([...empleados, nuevoEmpleado]);
      setIsDialogOpen(false);
      form.reset();
    }
  };

  return (
    <div className="p-4 md:p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Gestión de Empleados</h1>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button>Añadir Empleado</Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Nuevo Empleado</DialogTitle>
            </DialogHeader>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                {/* Campos del formulario */}
                <FormField name="nombre" render={({ field }) => (
                  <FormItem>
                    <FormLabel>Nombre</FormLabel>
                    <FormControl><Input {...field} /></FormControl>
                    <FormMessage />
                  </FormItem>
                )} />
                <FormField name="apellido" render={({ field }) => (
                  <FormItem>
                    <FormLabel>Apellido</FormLabel>
                    <FormControl><Input {...field} /></FormControl>
                    <FormMessage />
                  </FormItem>
                )} />
                 <FormField
                  control={form.control}
                  name="tipo_documento"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Tipo de Documento</FormLabel>
                      <Select onValueChange={field.onChange} defaultValue={field.value}>
                        <FormControl>
                          <SelectTrigger>
                            <SelectValue placeholder="Seleccione un tipo" />
                          </SelectTrigger>
                        </FormControl>
                        <SelectContent>
                          <SelectItem value="CC">Cédula de Ciudadanía</SelectItem>
                          <SelectItem value="CE">Cédula de Extranjería</SelectItem>
                          <SelectItem value="PA">Pasaporte</SelectItem>
                        </SelectContent>
                      </Select>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <FormField name="numero_documento" render={({ field }) => (
                    <FormItem>
                        <FormLabel>Número de Documento</FormLabel>
                        <FormControl><Input {...field} /></FormControl>
                        <FormMessage />
                    </FormItem>
                )} />
                <FormField name="fecha_nacimiento" render={({ field }) => (
                    <FormItem>
                        <FormLabel>Fecha de Nacimiento</FormLabel>
                        <FormControl><Input type="date" {...field} /></FormControl>
                        <FormMessage />
                    </FormItem>
                )} />
                <FormField name="fecha_contratacion" render={({ field }) => (
                    <FormItem>
                        <FormLabel>Fecha de Contratación</FormLabel>
                        <FormControl><Input type="date" {...field} /></FormControl>
                        <FormMessage />
                    </FormItem>
                )} />
                <FormField name="salario_base" render={({ field }) => (
                    <FormItem>
                        <FormLabel>Salario Base</FormLabel>
                        <FormControl><Input type="number" {...field} /></FormControl>
                        <FormMessage />
                    </FormItem>
                )} />

                <Button type="submit">Guardar</Button>
              </form>
            </Form>
          </DialogContent>
        </Dialog>
      </div>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Nombre Completo</TableHead>
            <TableHead>Documento</TableHead>
            <TableHead>Salario Base</TableHead>
            <TableHead>Estado</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {empleados.map((empleado) => (
            <TableRow key={empleado.id}>
              <TableCell>{empleado.nombre} {empleado.apellido}</TableCell>
              <TableCell>{empleado.tipo_documento} {empleado.numero_documento}</TableCell>
              <TableCell>{empleado.salario_base}</TableCell>
              <TableCell>{empleado.activo ? "Activo" : "Inactivo"}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
