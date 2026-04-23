"use client";
import { useState } from "react";

const tipos = ["Departamento", "Casa", "PH", "Oficina", "Local", "Terreno", "Cochera"];
const barrios = ["Centro", "Pichincha", "Fisherton", "Alberdi", "Echesortu", "Belgrano Norte", "Arroyito", "Las Delicias"];
const precios = [
  { label: "Hasta USD 50.000", value: "50000" },
  { label: "Hasta USD 100.000", value: "100000" },
  { label: "Hasta USD 150.000", value: "150000" },
  { label: "Hasta USD 200.000", value: "200000" },
  { label: "Hasta USD 300.000", value: "300000" },
  { label: "Sin límite", value: "" },
];
const quickTags = ["Departamentos en Centro", "Casas en Fisherton", "Emprendimientos", "Ver mapa"];

export default function Hero() {
  const [op, setOp] = useState<"Comprar" | "Alquilar">("Comprar");

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background layers */}
      <div className="absolute inset-0">
        <img
          src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=1920&q=80"
          alt="Rosario skyline"
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#0d1b3e]/85 via-[#0d1b3e]/75 to-[#0d1b3e]/90" />
      </div>

      {/* Decorative grid */}
      <div
        className="absolute inset-0 opacity-[0.04]"
        style={{
          backgroundImage:
            "linear-gradient(rgba(255,255,255,1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,1) 1px, transparent 1px)",
          backgroundSize: "60px 60px",
        }}
      />

      {/* Gold line accent top */}
      <div className="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-transparent via-[#c9973a] to-transparent" />

      <div className="relative z-10 w-full max-w-5xl mx-auto px-6 text-center pt-24 pb-16">
        {/* Badge */}
        <div className="inline-flex items-center gap-2.5 border border-[#c9973a]/40 bg-[#c9973a]/10 rounded-full px-5 py-2 mb-10">
          <span className="w-1.5 h-1.5 rounded-full bg-[#c9973a] animate-pulse" />
          <span className="text-[#c9973a] text-xs font-semibold tracking-[0.2em] uppercase">
            Líder en Rosario desde 1965
          </span>
        </div>

        {/* Headline */}
        <h1 className="text-5xl sm:text-6xl md:text-7xl font-black text-white leading-[1.05] mb-6 tracking-tight">
          Encontrá tu próxima
          <br />
          <span className="text-[#c9973a]">propiedad en Rosario</span>
        </h1>

        <p className="text-white/55 text-lg md:text-xl max-w-xl mx-auto mb-12 leading-relaxed">
          +3.000 propiedades disponibles. Comprá, alquilá o tasá con el equipo más experimentado del mercado rosarino.
        </p>

        {/* Search card */}
        <div className="bg-white/8 backdrop-blur-2xl border border-white/15 rounded-2xl p-5 sm:p-7 shadow-2xl">
          {/* Op tabs */}
          <div className="flex gap-1 mb-5 bg-white/5 rounded-xl p-1 w-fit">
            {(["Comprar", "Alquilar"] as const).map((o) => (
              <button
                key={o}
                onClick={() => setOp(o)}
                className={`px-6 py-2 rounded-lg text-sm font-semibold transition-all duration-200 ${
                  op === o
                    ? "bg-[#c9973a] text-white shadow-lg"
                    : "text-white/60 hover:text-white"
                }`}
              >
                {o}
              </button>
            ))}
          </div>

          {/* Filters */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            <select className="bg-white/8 border border-white/15 text-white rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-[#c9973a] transition-colors appearance-none cursor-pointer">
              <option className="text-[#0d1b3e]" value="">Tipo de propiedad</option>
              {tipos.map((t) => (
                <option key={t} className="text-[#0d1b3e]" value={t}>{t}</option>
              ))}
            </select>

            <select className="bg-white/8 border border-white/15 text-white rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-[#c9973a] transition-colors appearance-none cursor-pointer">
              <option className="text-[#0d1b3e]" value="">Barrio</option>
              {barrios.map((b) => (
                <option key={b} className="text-[#0d1b3e]" value={b}>{b}</option>
              ))}
            </select>

            <select className="bg-white/8 border border-white/15 text-white rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-[#c9973a] transition-colors appearance-none cursor-pointer">
              <option className="text-[#0d1b3e]" value="">Precio máximo</option>
              {precios.map((p) => (
                <option key={p.value} className="text-[#0d1b3e]" value={p.value}>{p.label}</option>
              ))}
            </select>

            <button className="bg-[#c9973a] hover:bg-[#e8b554] text-white rounded-xl px-6 py-3.5 font-bold text-sm tracking-wide transition-all duration-200 flex items-center justify-center gap-2 group shadow-lg shadow-[#c9973a]/30">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
              </svg>
              Buscar
              <span className="group-hover:translate-x-0.5 transition-transform">→</span>
            </button>
          </div>

          {/* Quick filters */}
          <div className="flex flex-wrap gap-2 mt-4 pt-4 border-t border-white/8">
            {quickTags.map((tag) => (
              <button
                key={tag}
                className="text-white/40 hover:text-[#c9973a] text-xs font-medium border border-white/8 hover:border-[#c9973a]/40 rounded-full px-3.5 py-1.5 transition-all duration-200"
              >
                {tag}
              </button>
            ))}
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="mt-16 flex flex-col items-center gap-2 opacity-40">
          <span className="text-white text-xs tracking-widest uppercase">Explorar</span>
          <div className="w-px h-8 bg-gradient-to-b from-white to-transparent animate-pulse" />
        </div>
      </div>
    </section>
  );
}
