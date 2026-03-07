let token: string | null = null;

export const tokenManager = {
  setToken(newToken: string) {
    token = newToken;
  },
  getToken() {
    return token;
  },
  clear() {
    token = null;
  },
};
