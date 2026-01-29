import api from './api';

export interface StrategyProposal {
    id: string;
    domain: string;
    status: string;
    contexto_detectado: string;
    riesgo_actual: string;
    oportunidad_detectada: string;
    accion_sugerida: any;
    impacto_estimado: string;
    nivel_confianza: number;
    nivel_urgencia: string;
    nivel_riesgo: string;
    decision_level: number;
    created_at: string;
}

export const getStrategyProposals = async (): Promise<StrategyProposal[]> => {
    const response = await api.get('/admin/intelligence/proposals/');
    return response.data;
};

export const approveStrategyProposal = async (id: string, justification?: string) => {
    const response = await api.post(`/admin/intelligence/proposals/${id}/approve/`, {
        justificacion_humana: justification
    });
    return response.data;
};

export const executeStrategyProposal = async (id: string) => {
    const response = await api.post(`/admin/intelligence/proposals/${id}/execute/`);
    return response.data;
};

export const rejectStrategyProposal = async (id: string) => {
    const response = await api.post(`/admin/intelligence/proposals/${id}/reject/`);
    return response.data;
};
