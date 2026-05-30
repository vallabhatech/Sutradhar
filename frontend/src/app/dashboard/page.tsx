'use client';

import { useAuth } from '@/contexts/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function DashboardPage() {
  const { user, logout, isLoading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && !user) {
      router.push('/login');
    }
  }, [user, isLoading, router]);

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
        <div className="text-white">Loading...</div>
      </div>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <nav className="bg-slate-800/50 backdrop-blur-sm border-b border-slate-700">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-white">Sutradhar</h1>
          <div className="flex items-center gap-4">
            <span className="text-slate-300">{user.full_name}</span>
            <span className="px-3 py-1 bg-primary-600 text-white rounded-full text-sm">
              {user.role}
            </span>
            <button
              onClick={logout}
              className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-lg transition-colors"
            >
              Logout
            </button>
          </div>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-white mb-2">Welcome, {user.full_name}!</h2>
          <p className="text-slate-400">Dashboard placeholder - authentication successful</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
            <h3 className="text-xl font-semibold text-white mb-2">User Information</h3>
            <div className="space-y-2 text-slate-300">
              <p><span className="font-medium">Email:</span> {user.email}</p>
              <p><span className="font-medium">Role:</span> {user.role}</p>
              <p><span className="font-medium">Status:</span> {user.is_active ? 'Active' : 'Inactive'}</p>
              <p><span className="font-medium">Admin:</span> {user.is_admin ? 'Yes' : 'No'}</p>
            </div>
          </div>

          <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
            <h3 className="text-xl font-semibold text-white mb-2">Account Details</h3>
            <div className="space-y-2 text-slate-300">
              <p><span className="font-medium">UUID:</span> {user.uuid}</p>
              <p><span className="font-medium">ID:</span> {user.id}</p>
              <p><span className="font-medium">Created:</span> {new Date(user.created_at).toLocaleDateString()}</p>
            </div>
          </div>

          <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
            <h3 className="text-xl font-semibold text-white mb-2">Quick Actions</h3>
            <div className="space-y-2">
              <button className="w-full py-2 bg-primary-600 hover:bg-primary-700 text-white rounded-lg transition-colors">
                View Profile
              </button>
              <button className="w-full py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-lg transition-colors">
                Settings
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
