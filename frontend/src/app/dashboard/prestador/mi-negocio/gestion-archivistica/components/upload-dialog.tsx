"use client";

import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { useDropzone } from "react-dropzone";
import apiClient from "@/services/api";

// --- Componentes de UI Reales ---
import { Dialog, DialogTrigger, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Button } from "@/components/ui/Button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/Form";
import { Input } from "@/components/ui/Input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/Select";
import { Spinner } from "@/components/shared/spinner";
import { UploadCloud, X, File as FileIcon } from "lucide-react";
import { useToast } from "@/components/ui/use-toast";

// Esquema de validación del formulario con Zod
const formSchema = z.object({
  title: z.string().min(3, "El título es requerido."),
  validity_year: z.coerce.number().min(2020, "El año es inválido."),
  process_id: z.string().uuid("Debes seleccionar un proceso."),
  document_type_id: z.string().uuid("Debes seleccionar un tipo."),
  file: z.instanceof(File, { message: "Debes adjuntar un archivo." }),
});
type FormValues = z.infer<typeof formSchema>;
type CatalogItem = { id: string; name: string };

export function UploadDialog({ children }) {
    const [isOpen, setIsOpen] = useState(false);
    const { toast } = useToast();
    const queryClient = useQueryClient();

    const form = useForm<FormValues>({ resolver: zodResolver(formSchema) });

    const { data: processes } = useQuery<CatalogItem[]>({
        queryKey: ['archivisticaProcesses'],
        queryFn: async () => (await apiClient.get('/mi-negocio/archivistica/processes/')).data.results,
    });
    const { data: documentTypes } = useQuery<CatalogItem[]>({
        queryKey: ['archivisticaDocumentTypes'],
        queryFn: async () => (await apiClient.get('/mi-negocio/archivistica/document-types/')).data.results,
    });

    const { mutate: uploadDocument, isPending } = useMutation({
        mutationFn: (values: FormValues) => {
            const formData = new FormData();
            Object.entries(values).forEach(([key, value]) => formData.append(key, value));
            return apiClient.post('/mi-negocio/archivistica/documents/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
        },
        onSuccess: () => {
            toast({ title: "Éxito", description: "El documento ha sido enviado para su procesamiento." });
            queryClient.invalidateQueries({ queryKey: ['archivisticaDocuments'] });
            handleClose();
        },
        onError: (error: any) => {
            const message = error.response?.data?.detail || "No se pudo subir el documento.";
            toast({ title: "Error", description: message, variant: 'destructive' });
        },
    });

    const onDrop = (acceptedFiles: File[]) => {
        if (acceptedFiles.length > 0) form.setValue("file", acceptedFiles[0], { shouldValidate: true });
    };
    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, multiple: false });

    function onSubmit(values: FormValues) {
        uploadDocument(values);
    }
    function handleClose() {
        form.reset();
        setIsOpen(false);
    }

    const currentFile = form.watch("file");

    return (
        <Dialog open={isOpen} onOpenChange={setIsOpen}>
            <DialogTrigger asChild>{children}</DialogTrigger>
            <DialogContent className="sm:max-w-[625px]">
                <DialogHeader><DialogTitle>Subir Nuevo Documento</DialogTitle></DialogHeader>
                <Form {...form}>
                    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                        <div className="grid grid-cols-2 gap-4">
                            <FormField name="title" control={form.control} render={({ field }) => (
                                <FormItem><FormLabel>Título</FormLabel><FormControl><Input {...field} /></FormControl><FormMessage /></FormItem>
                            )} />
                            <FormField name="validity_year" control={form.control} render={({ field }) => (
                                <FormItem><FormLabel>Año</FormLabel><FormControl><Input type="number" {...field} /></FormControl><FormMessage /></FormItem>
                            )} />
                        </div>
                        <div className="grid grid-cols-2 gap-4">
                             <FormField name="process_id" control={form.control} render={({ field }) => (
                                <FormItem><FormLabel>Proceso</FormLabel><Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccionar..." /></SelectTrigger></FormControl>
                                    <SelectContent>{processes?.map(p => <SelectItem key={p.id} value={p.id}>{p.name}</SelectItem>)}</SelectContent>
                                </Select><FormMessage /></FormItem>
                            )} />
                             <FormField name="document_type_id" control={form.control} render={({ field }) => (
                                <FormItem><FormLabel>Tipo</FormLabel><Select onValueChange={field.onChange} value={field.value}>
                                    <FormControl><SelectTrigger><SelectValue placeholder="Seleccionar..." /></SelectTrigger></FormControl>
                                    <SelectContent>{documentTypes?.map(dt => <SelectItem key={dt.id} value={dt.id}>{dt.name}</SelectItem>)}</SelectContent>
                                </Select><FormMessage /></FormItem>
                            )} />
                        </div>
                        <FormField control={form.control} name="file" render={() => (
                            <FormItem>
                                <FormLabel>Archivo</FormLabel>
                                {currentFile ? (
                                    <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                                        <div className="flex items-center gap-2"><FileIcon className="h-5 w-5" /><span className="font-medium text-sm">{currentFile.name}</span></div>
                                        <Button variant="ghost" size="icon" className="h-6 w-6" onClick={() => form.resetField("file")}><X className="h-4 w-4"/></Button>
                                    </div>
                                ) : (
                                    <div {...getRootProps()} className={`flex flex-col items-center justify-center p-8 border-2 border-dashed rounded-lg cursor-pointer transition-colors ${isDragActive ? 'border-primary bg-primary/10' : 'hover:bg-muted/50'}`}>
                                        <input {...getInputProps()} />
                                        <UploadCloud className="h-8 w-8 text-muted-foreground mb-2"/><p className="text-sm font-medium">Arrastra un archivo o haz clic</p>
                                    </div>
                                )}
                                <FormMessage />
                            </FormItem>
                        )}/>
                        <DialogFooter>
                            <Button type="button" variant="outline" onClick={handleClose}>Cancelar</Button>
                            <Button type="submit" disabled={isPending}>
                                {isPending && <Spinner className="mr-2"/>}
                                Subir y Securizar
                            </Button>
                        </DialogFooter>
                    </form>
                </Form>
            </DialogContent>
        </Dialog>
    );
}
