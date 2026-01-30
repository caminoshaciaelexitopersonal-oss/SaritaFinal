'use client';

import useSWR from 'swr';
import api from '@/services/api';

const fetcher = (url: string) => api.get(url).then(res => res.data);

export function useIntelligenceApi() {
  const { data, error, isLoading, mutate } = useSWR('/admin/intelligence/proposals/', fetcher);

  const runAnalysis = async () => {
    await api.post('/admin/intelligence/proposals/run_analysis/');
    mutate();
  };

  const approveProposal = async (id: string) => {
    await api.post(`/admin/intelligence/proposals/${id}/approve/`);
    mutate();
  };

  const executeProposal = async (id: string) => {
    await api.post(`/admin/intelligence/proposals/${id}/execute/`);
    mutate();
  };

  return {
    proposals: data?.results || [],
    isLoading,
    isError: error,
    runAnalysis,
    approveProposal,
    executeProposal
  };
}
