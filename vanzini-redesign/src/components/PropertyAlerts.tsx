"use client";
import { useState } from "react";

const tipos = ["Departamento", "Casa", "PH", "Oficina", "Terreno"];
const barrios = ["Centro", "Pichincha", "Fisherton", "Alberdi", "Echesortu"];

export default function PropertyAlerts() {
  const [email, setEmail] = useState("");
  const [sent, setSent] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) setSent(true);
  };

  return (
    <section className="bg-[#c9973a] py-20 relative overflow-hidden">
      {/* Decorative */}
      <div className="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full translate-x-32 -translate-y-32" />
      <div className="absolute bottom-0 left-0 w-64 h-64 bg-white/5 rounded-full -translate-x-20 translate-y-20" />

      <div className="max-w-4xl mx-auto px-6 relative z-10">
        <div className="text-center mb-10">
          {/* Bell icon */}
          <div className="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
            <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
                d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
            </svg>
          </div>

          <h2 className="text-4xl md:text-5xl font-black text-white leading-tight mb-4">
            Avisame cuando aparezca
            <br />mi propiedad ideal
          </h2>
          <p className="text-white/75 text-lg max-w-lg mx-auto">
            Configurá tus filtros y te notificamos en el momento en que ingresa una propiedad que coincida con lo que buscás.
          </p>
        </div>

        {!sent ? (
          <form onSubmit={handleSubmit} className="bg-white/15 backdrop-blur-sm border border-white/25 rounded-2xl p-6 sm:p-8">
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
              <select className="bg-white/20 border border-white/30 text-white rounded-xl px-4 py-3 text-sm placeholder-white/60 focus:outline-none focus:border-white appearance-none">
                <option className="text-[#0d1b3e]" value="">Tipo de propiedad</option>
                {tipos.map((t) => <option key={t} className="text-[#0d1b3e]" value={t}>{t}</option>)}
              </select>
              <select className="bg-white/20 border border-white/30 text-white rounded-xl px-4 py-3 text-sm placeholder-white/60 focus:outline-none focus:border-white appearance-none">
                <option className="text-[#0d1b3e]" value="">Barrio</option>
                {barrios.map((b) => <option key={b} className="text-[#0d1b3e]" value={b}>{b}</option>)}
              </select>
              <select className="bg-white/20 border border-white/30 text-white rounded-xl px-4 py-3 text-sm placeholder-white/60 focus:outline-none focus:border-white appearance-none">
                <option className="text-[#0d1b3e]" value="">Precio máximo</option>
                <option className="text-[#0d1b3e]" value="80000">USD 80.000</option>
                <option className="text-[#0d1b3e]" value="150000">USD 150.000</option>
                <option className="text-[#0d1b3e]" value="250000">USD 250.000</option>
              </select>
            </div>
            <div className="flex flex-col sm:flex-row gap-3">
              <input
                type="email"
                required
                placeholder="Tu email para recibir alertas"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="flex-1 bg-white border-0 text-[#0d1b3e] rounded-xl px-5 py-3.5 text-sm placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#0d1b3e]/20"
              />
              <button
                type="submit"
                className="bg-[#0d1b3e] hover:bg-[#162244] text-white font-bold px-7 py-3.5 rounded-xl tracking-wide transition-colors text-sm"
              >
                Activar alertas →
              </button>
            </div>
            <p className="text-white/50 text-xs text-center mt-4">
              Sin spam. Podés cancelar en cualquier momento.
            </p>
          </form>
        ) : (
          <div className="bg-white/15 border border-white/25 rounded-2xl p-10 text-center">
            <div className="w-16 h-16 bg-white/20 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h3 className="text-2xl font-black text-white mb-2">¡Alerta activada!</h3>
            <p className="text-white/70">Te avisamos en cuanto encontremos algo que coincida con tu búsqueda.</p>
          </div>
        )}
      </div>
    </section>
  );
}
