import { apiClient } from '@/lib/auth';
import type { LoginRequest, RegisterRequest, TokenResponse } from '@/types/auth';

export const authService = {
  async login(credentials: LoginRequest): Promise<TokenResponse> {
    return apiClient.post<TokenResponse>('/api/v1/auth/login', credentials);
  },

  async register(data: RegisterRequest): Promise<TokenResponse> {
    return apiClient.post<TokenResponse>('/api/v1/auth/register', data);
  },

  async getCurrentUser() {
    return apiClient.get('/api/v1/auth/me');
  },
};
