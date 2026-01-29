import useSWR from 'swr';
import api from '@/lib/api';

const fetcher = (url: string) => api.get(url).then((res) => res.data);

export const useGovernanceApi = () => {
  const { data: summary, error: summaryError, isLoading: summaryLoading } = useSWR(
    '/api/admin/plataforma/governance/summary/',
    fetcher
  );

  const { data: comparative, error: comparativeError, isLoading: comparativeLoading } = useSWR(
    '/api/admin/plataforma/governance/comparative/',
    fetcher
  );

  const { data: ranking, error: rankingError, isLoading: rankingLoading } = useSWR(
    '/api/admin/plataforma/governance/ranking/',
    fetcher
  );

  return {
    summary,
    comparative,
    ranking,
    isLoading: summaryLoading || comparativeLoading || rankingLoading,
    isError: summaryError || comparativeError || rankingError,
  };
};
