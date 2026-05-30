'use client';

import { useAuth } from '@/contexts/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function Home() {
  const { isAuthenticated, isLoading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && isAuthenticated) {
      router.push('/dashboard');
    }
  }, [isAuthenticated, isLoading, router]);

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
        <div className="text-white">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <div className="container mx-auto px-4 py-16">
        <div className="flex flex-col items-center justify-center min-h-[80vh]">
          <div className="text-center space-y-8">
            <h1 className="text-6xl font-bold text-white tracking-tight">
              Sutradhar
            </h1>
            <p className="text-2xl text-slate-300 font-light">
              Tracing the hidden flow of money
            </p>
            <div className="pt-8 space-x-4">
              <a
                href="/login"
                className="inline-block px-8 py-4 bg-primary-600 hover:bg-primary-700 text-white rounded-lg font-medium transition-colors"
              >
                Sign In
              </a>
              <a
                href="/register"
                className="inline-block px-8 py-4 bg-slate-700 hover:bg-slate-600 text-white rounded-lg font-medium transition-colors"
              >
                Sign Up
              </a>
            </div>
          </div>

          <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl">
            <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
              <h3 className="text-xl font-semibold text-white mb-2">Extract</h3>
              <p className="text-slate-400">
                Intelligent data extraction from bank statements
              </p>
            </div>
            <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
              <h3 className="text-xl font-semibold text-white mb-2">Analyze</h3>
              <p className="text-slate-400">
                Advanced transaction analysis and pattern detection
              </p>
            </div>
            <div className="bg-slate-800/50 backdrop-blur-sm p-6 rounded-lg border border-slate-700">
              <h3 className="text-xl font-semibold text-white mb-2">Investigate</h3>
              <p className="text-slate-400">
                Comprehensive fraud investigation and reporting
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
