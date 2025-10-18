'use client';

import React, { useState, useEffect } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { useForm, useFieldArray, SubmitHandler, Controller } from 'react-hook-form';
import { FiPlusCircle, FiTrash2, FiArrowUp, FiArrowDown } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';

// --- Tipos ---
interface Opcion {
    id?: number;
    texto_opcion: string;
}

interface Pregunta {
    id?: number;
    texto_pregunta: string;
    tipo_pregunta: string;
    es_requerida: boolean;
    opciones: Opcion[];
}

interface FormularioData {
    titulo: string;
    descripcion: string;
    es_publico: boolean;
    preguntas: Pregunta[];
}

const FormBuilder = () => {
    const searchParams = useSearchParams();
    const router = useRouter();
    const formId = searchParams.get('id');
    const [isLoading, setIsLoading] = useState(!!formId);

    const { register, control, handleSubmit, reset, watch } = useForm<FormularioData>({
        defaultValues: {
            titulo: '',
            descripcion: '',
            es_publico: false,
            preguntas: [],
        },
    });

    const { fields, append, remove, swap } = useFieldArray({
        control,
        name: "preguntas",
    });

    useEffect(() => {
        if (formId) {
            const fetchFormulario = async () => {
                try {
                    const data = await api.get(`/api/formularios/${formId}/`);
                    reset(data);
                } catch (error) {
                    toast.error('No se pudo cargar el formulario para editar.');
                    router.push('/dashboard/admin/formularios');
                } finally {
                    setIsLoading(false);
                }
            };
            fetchFormulario();
        }
    }, [formId, reset, router]);

    const onSubmit: SubmitHandler<FormularioData> = async (data) => {
        try {
            if (formId) {
                await api.put(`/api/formularios/${formId}/`, data);
                toast.success('Formulario actualizado con éxito.');
            } else {
                await api.post('/api/formularios/', data);
                toast.success('Formulario creado con éxito.');
            }
            router.push('/dashboard/admin/formularios');
        } catch (error: any) {
            const errorMsg = error.response?.data?.detail || 'Ocurrió un error al guardar el formulario.';
            toast.error(errorMsg);
        }
    };

    if (isLoading) return <div>Cargando constructor...</div>;

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <h1 className="text-3xl font-bold text-gray-800 mb-6">
                {formId ? 'Editar Formulario' : 'Crear Nuevo Formulario'}
            </h1>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                <div className="p-4 border rounded-lg">
                    <input {...register('titulo', { required: true })} placeholder="Título del Formulario" className="text-2xl font-bold w-full border-b pb-2 mb-2"/>
                    <textarea {...register('descripcion')} placeholder="Descripción del formulario..." rows={2} className="w-full mt-1 p-2 border rounded"/>
                    <div className="flex items-center mt-2">
                        <input type="checkbox" {...register('es_publico')} className="h-4 w-4" />
                        <label className="ml-2">Hacer público para los prestadores</label>
                    </div>
                </div>

                <div className="space-y-4">
                    {fields.map((field, index) => (
                        <PreguntaBuilder key={field.id} control={control} index={index} remove={remove} swap={swap} watch={watch} />
                    ))}
                </div>

                <button type="button" onClick={() => append({ texto_pregunta: '', tipo_pregunta: 'TEXTO_CORTO', es_requerida: false, opciones: [] })} className="inline-flex items-center px-4 py-2 border border-dashed rounded-md">
                    <FiPlusCircle className="mr-2"/>Añadir Pregunta
                </button>

                <div className="text-right border-t pt-4">
                    <button type="submit" className="px-6 py-2 bg-green-600 text-white rounded-md hover:bg-green-700">
                        Guardar Formulario
                    </button>
                </div>
            </form>
        </div>
    );
};

const PreguntaBuilder = ({ control, index, remove, swap, watch }: any) => {
    const { fields, append, remove: removeOpcion } = useFieldArray({
        control,
        name: `preguntas.${index}.opciones`
    });

    const tipoPregunta = watch(`preguntas.${index}.tipo_pregunta`);
    const showOpciones = tipoPregunta === 'SELECCION_UNICA' || tipoPregunta === 'SELECCION_MULTIPLE';

    return (
        <div className="p-4 border rounded-lg bg-gray-50">
            <div className="flex justify-between items-center">
                <h3 className="font-semibold">Pregunta {index + 1}</h3>
                <div>
                    <button type="button" onClick={() => index > 0 && swap(index, index - 1)} disabled={index === 0}><FiArrowUp/></button>
                    <button type="button" onClick={() => remove(index)} className="ml-4 text-red-500"><FiTrash2/></button>
                </div>
            </div>
            <input {...control.register(`preguntas.${index}.texto_pregunta`, { required: true })} placeholder="Texto de la pregunta" className="w-full mt-2 p-2 border rounded"/>
            <select {...control.register(`preguntas.${index}.tipo_pregunta`)} className="w-full mt-2 p-2 border rounded">
                <option value="TEXTO_CORTO">Texto Corto</option>
                <option value="TEXTO_LARGO">Texto Largo</option>
                <option value="NUMERO">Número</option>
                <option value="FECHA">Fecha</option>
                <option value="SELECCION_UNICA">Selección Única</option>
                <option value="SELECCION_MULTIPLE">Selección Múltiple</option>
            </select>
            {showOpciones && (
                <div className="mt-2 pl-4">
                    <h4 className="font-medium text-sm">Opciones</h4>
                    {fields.map((opcion, opcionIndex) => (
                        <div key={opcion.id} className="flex items-center gap-2 mt-1">
                            <input {...control.register(`preguntas.${index}.opciones.${opcionIndex}.texto_opcion`)} placeholder={`Opción ${opcionIndex + 1}`} className="flex-grow p-1 border rounded" />
                            <button type="button" onClick={() => removeOpcion(opcionIndex)}><FiTrash2 className="text-red-400"/></button>
                        </div>
                    ))}
                    <button type="button" onClick={() => append({ texto_opcion: '' })} className="text-xs text-blue-500 mt-1">
                        Añadir Opción
                    </button>
                </div>
            )}
        </div>
    );
};

const FormBuilderPage = () => {
    return (
      <AuthGuard allowedRoles={['ADMIN', 'FUNCIONARIO_DIRECTIVO']}>
        <FormBuilder />
      </AuthGuard>
    );
};

export default FormBuilderPage;