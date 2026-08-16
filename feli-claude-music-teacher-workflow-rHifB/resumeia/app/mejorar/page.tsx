"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function MejorarPage() {
  const router = useRouter();
  const [cv, setCv] = useState("");
  const [puesto, setPuesto] = useState("");
  const [idioma, setIdioma] = useState("español");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handlePagar() {
    if (!cv.trim() || cv.trim().length < 100) {
      setError("Por favor pegá tu CV completo (mínimo 100 caracteres).");
      return;
    }
    if (!puesto.trim()) {
      setError("Ingresá el puesto que buscás.");
      return;
    }
    setError("");
    setLoading(true);
    try {
      const res = await fetch("/api/crear-pago", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cv, puesto, idioma }),
      });
      const data = await res.json();
      if (data.init_point) {
        window.location.href = data.init_point;
      } else {
        setError("Error al crear el pago. Intentá de nuevo.");
      }
    } catch {
      setError("Error de conexión. Intentá de nuevo.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white px-6 py-12">
      <div className="max-w-2xl mx-auto">
        <div className="mb-8">
          <a href="/" className="text-purple-400 text-sm hover:underline">← Volver</a>
          <h1 className="text-4xl font-extrabold mt-4 mb-2">Mejorá tu CV</h1>
          <p className="text-slate-400">Pegá tu CV, decinos qué puesto buscás y la IA hace el resto.</p>
        </div>

        <div className="bg-white/5 border border-white/10 rounded-2xl p-6 space-y-6">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Tu CV actual <span className="text-red-400">*</span>
            </label>
            <textarea
              value={cv}
              onChange={(e) => setCv(e.target.value)}
              placeholder="Pegá aquí el texto completo de tu CV..."
              rows={10}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white placeholder-slate-500 focus:outline-none focus:border-purple-500 resize-none"
            />
            <p className="text-xs text-slate-500 mt-1">{cv.length} caracteres</p>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              ¿Qué puesto buscás? <span className="text-red-400">*</span>
            </label>
            <input
              value={puesto}
              onChange={(e) => setPuesto(e.target.value)}
              placeholder="Ej: Desarrollador Frontend, Diseñador UX, Gerente de Ventas..."
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white placeholder-slate-500 focus:outline-none focus:border-purple-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Idioma del resultado
            </label>
            <select
              value={idioma}
              onChange={(e) => setIdioma(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500"
            >
              <option value="español">Español</option>
              <option value="inglés">Inglés</option>
              <option value="portugués">Portugués</option>
            </select>
          </div>

          {error && (
            <p className="text-red-400 text-sm bg-red-900/20 border border-red-800 rounded-xl px-4 py-3">
              {error}
            </p>
          )}

          <div className="bg-purple-900/30 border border-purple-700/50 rounded-xl p-4 text-sm text-slate-300">
            <p className="font-semibold text-white mb-1">Vas a recibir:</p>
            <ul className="space-y-1 text-slate-400">
              <li>✅ 3 versiones mejoradas de tu CV</li>
              <li>✅ Cover letter personalizada</li>
              <li>✅ Tips para la entrevista</li>
            </ul>
          </div>

          <button
            onClick={handlePagar}
            disabled={loading}
            className="w-full bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 disabled:opacity-50 disabled:cursor-not-allowed text-white font-bold text-lg py-4 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-[1.02]"
          >
            {loading ? "Redirigiendo a Mercado Pago..." : "Pagar $7 USD con Mercado Pago →"}
          </button>

          <p className="text-center text-xs text-slate-500">
            Pago seguro con Mercado Pago. Tu CV no se guarda en nuestros servidores.
          </p>
        </div>
      </div>
    </main>
  );
}
