"use client";

import { useForm, useFieldArray } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
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
import { Trash2 } from "lucide-react";
import { useMiNegocioApi, CreateFacturaVentaDTO } from "../../../../../(authenticated)/prestador/mi-negocio/hooks/useMiNegocioApi";
// Mock data - en una app real, esto vendría de la API
const clientesMock = [{ id: 1, nombre: "Cliente de Prueba" }];
const productosMock = [{ id: 1, nombre: "Producto A", precio: "100.00" }, { id: 2, nombre: "Producto B", precio: "50.00" }];


const itemSchema = z.object({
  producto: z.string().min(1, "Seleccione un producto."),
  cantidad: z.coerce.number().min(0.01, "La cantidad debe ser positiva."),
  precio_unitario: z.coerce.number().min(0, "El precio no puede ser negativo."),
});

const facturaSchema = z.object({
  cliente: z.string().min(1, "Seleccione un cliente."),
  fecha_emision: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Fecha inválida."),
  fecha_vencimiento: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Fecha inválida."),
  items: z.array(itemSchema).min(1, "Debe añadir al menos un ítem."),
});

type FacturaFormData = z.infer<typeof facturaSchema>;

export default function NuevaFacturaPage() {
  const router = useRouter();
  const { createFacturaVenta } = useMiNegocioApi();
  // En una app real, usarías hooks para obtener clientes y productos de la API
  // const { data: clientes } = useGetClientes();
  // const { data: productos } = useGetProductos();

  const form = useForm<FacturaFormData>({
    resolver: zodResolver(facturaSchema),
    defaultValues: {
      fecha_emision: new Date().toISOString().split("T")[0],
      items: [{ producto: "", cantidad: 1, precio_unitario: 0 }],
    },
  });

  const { fields, append, remove } = useFieldArray({
    control: form.control,
    name: "items",
  });

  const onSubmit = async (data: FacturaFormData) => {
    const payload: CreateFacturaVentaDTO = {
      ...data,
      cliente: parseInt(data.cliente),
      estado: "BORRADOR",
      items: data.items.map(item => ({
        ...item,
        producto: parseInt(item.producto),
        precio_unitario: item.precio_unitario.toString(),
      })),
    };
    const nuevaFactura = await createFacturaVenta(payload);
    if (nuevaFactura) {
      router.push("/dashboard/prestador/mi-negocio/gestion-comercial/ventas");
    }
  };

  return (
    <div className="p-4 md:p-6">
      <h1 className="text-2xl font-bold mb-4">Nueva Factura de Venta</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          {/* Cabecera de la factura */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <FormField control={form.control} name="cliente" render={({ field }) => (
              <FormItem>
                <FormLabel>Cliente</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger><SelectValue placeholder="Seleccione un cliente" /></SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    {clientesMock.map(c => <SelectItem key={c.id} value={c.id.toString()}>{c.nombre}</SelectItem>)}
                  </SelectContent>
                </Select>
                <FormMessage />
              </FormItem>
            )} />
            <FormField control={form.control} name="fecha_emision" render={({ field }) => (
              <FormItem>
                <FormLabel>Fecha de Emisión</FormLabel>
                <FormControl><Input type="date" {...field} /></FormControl>
                <FormMessage />
              </FormItem>
            )} />
            <FormField control={form.control} name="fecha_vencimiento" render={({ field }) => (
              <FormItem>
                <FormLabel>Fecha de Vencimiento</FormLabel>
                <FormControl><Input type="date" {...field} /></FormControl>
                <FormMessage />
              </FormItem>
            )} />
          </div>

          {/* Items de la factura */}
          <div>
            <h2 className="text-xl font-semibold mb-2">Ítems</h2>
            <div className="space-y-4">
              {fields.map((field, index) => (
                <div key={field.id} className="flex items-end gap-2 p-2 border rounded-md">
                  <FormField control={form.control} name={`items.${index}.producto`} render={({ field }) => (
                    <FormItem className="flex-1">
                      <FormLabel>Producto</FormLabel>
                      <Select onValueChange={field.onChange} defaultValue={field.value}>
                        <FormControl><SelectTrigger><SelectValue placeholder="Producto" /></SelectTrigger></FormControl>
                        <SelectContent>
                          {productosMock.map(p => <SelectItem key={p.id} value={p.id.toString()}>{p.nombre}</SelectItem>)}
                        </SelectContent>
                      </Select>
                    </FormItem>
                  )} />
                  <FormField control={form.control} name={`items.${index}.cantidad`} render={({ field }) => (
                    <FormItem><FormLabel>Cantidad</FormLabel><FormControl><Input type="number" {...field} /></FormControl></FormItem>
                  )} />
                  <FormField control={form.control} name={`items.${index}.precio_unitario`} render={({ field }) => (
                    <FormItem><FormLabel>Precio Unit.</FormLabel><FormControl><Input type="number" step="0.01" {...field} /></FormControl></FormItem>
                  )} />
                  <Button type="button" variant="destructive" size="icon" onClick={() => remove(index)}>
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              ))}
            </div>
            <Button type="button" variant="outline" size="sm" className="mt-4" onClick={() => append({ producto: "", cantidad: 1, precio_unitario: 0 })}>
              Añadir Ítem
            </Button>
          </div>

          <Button type="submit">Guardar Factura</Button>
        </form>
      </Form>
    </div>
  );
}
