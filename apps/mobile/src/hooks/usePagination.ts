import { useState, useEffect } from 'react';
import { api } from '../services/api';
import { PaginationEngine } from '@sarita/shared-sdk';

export function usePagination(url: string, pageSize: number = 20) {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);

  const loadData = async (newPage: number) => {
    try {
      setLoading(true);
      const params = PaginationEngine.getPageParams(newPage, pageSize);
      const response = await api.get(url, { params });
      const paginated = PaginationEngine.transform<any>(response.data);

      if (newPage === 1) {
        setData(paginated.results);
      } else {
        setData(prev => [...prev, ...paginated.results]);
      }

      setHasMore(paginated.next !== null);
      setPage(newPage);
    } catch (error) {
      console.error('Error fetching paginated data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData(1);
  }, [url]);

  const loadMore = () => {
    if (!loading && hasMore) {
      loadData(page + 1);
    }
  };

  return { data, loading, loadMore, hasMore };
}
