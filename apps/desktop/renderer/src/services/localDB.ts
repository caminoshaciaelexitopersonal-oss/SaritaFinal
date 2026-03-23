/**
 * LocalStorage Layer - SARITA Desktop
 * Proporciona una capa de persistencia para el ERP en modo offline.
 */
export const LocalDB = {
  save: (key: string, data: any) => {
    localStorage.setItem(`sarita_erp_${key}`, JSON.stringify(data));
  },

  get: (key: string) => {
    const data = localStorage.getItem(`sarita_erp_${key}`);
    return data ? JSON.parse(data) : null;
  },

  updateList: (key: string, item: any) => {
    const list = LocalDB.get(key) || [];
    const index = list.findIndex((i: any) => i.id === item.id);
    if (index > -1) {
      list[index] = item;
    } else {
      list.push(item);
    }
    LocalDB.save(key, list);
  },

  remove: (key: string) => {
    localStorage.removeItem(`sarita_erp_${key}`);
  }
};
