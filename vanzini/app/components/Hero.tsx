"use client";

import { useState } from "react";

const TIPOS = ["Departamento", "Casa", "Local", "Terreno", "Cochera", "Oficina"];
const BARRIOS = ["Centro", "Pichincha", "Fisherton", "Alberdi", "Norte", "Echesortu", "Todos"];
const OPERACIONES = ["Venta", "Alquiler", "Temporario"];

export default function Hero() {
  const [tipo, setTipo] = useState("Departamento");
  const [barrio, setBarrio] = useState("Todos");
  const [operacion, setOperacion] = useState("Venta");

  return (
    <section className="relative min-h-screen flex flex-col items-center justify-center overflow-hidden">
      {/* Background gradient overlay */}
      <div
        className="absolute inset-0 z-0"
        style={{
          background: "linear-gradient(135deg, #0d1b3e 0%, #1a2d5a 50%, #0d1b3e 100%)",
        }}
      />

      {/* Subtle pattern */}
      <div
        className="absolute inset-0 z-0 opacity-10"
        style={{
          backgroundImage:
            "radial-gradient(circle at 25% 25%, #c9973a 0%, transparent 50%), radial-gradient(circle at 75% 75%, #c9973a 0%, transparent 50%)",
        }}
      />

      <div className="relative z-10 text-center px-6 max-w-5xl mx-auto pt-24 pb-16">
        {/* Badge */}
        <div
          className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold tracking-wider uppercase mb-8"
          style={{ backgroundColor: "rgba(201,151,58,0.2)", color: "#c9973a", border: "1px solid rgba(201,151,58,0.4)" }}
        >
          <span className="w-2 h-2 rounded-full bg-[#c9973a] animate-pulse" />
          Más de 60 años en el mercado rosarino
        </div>

        <h1 className="text-5xl md:text-7xl font-bold text-white leading-tight mb-6">
          Tu próxima<br />
          <span style={{ color: "#c9973a" }}>propiedad ideal</span><br />
          te espera
        </h1>

        <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-12 leading-relaxed">
          Más de 3.000 propiedades en Rosario. Asesoramiento personalizado,
          gestión 100% digital y respuesta en menos de 48 horas.
        </p>

        {/* Search Box */}
        <div className="bg-white rounded-2xl shadow-2xl p-6 max-w-3xl mx-auto">
          {/* Tabs */}
          <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg">
            {OPERACIONES.map((op) => (
              <button
                key={op}
                onClick={() => setOperacion(op)}
                className="flex-1 py-2 rounded-md text-sm font-semibold transition-all"
                style={
                  operacion === op
                    ? { backgroundColor: "#0d1b3e", color: "white" }
                    : { color: "#64748b" }
                }
              >
                {op}
              </button>
            ))}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
            <div>
              <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">
                Tipo de propiedad
              </label>
              <select
                value={tipo}
                onChange={(e) => setTipo(e.target.value)}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
              >
                {TIPOS.map((t) => <option key={t}>{t}</option>)}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">
                Barrio
              </label>
              <select
                value={barrio}
                onChange={(e) => setBarrio(e.target.value)}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
              >
                {BARRIOS.map((b) => <option key={b}>{b}</option>)}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">
                Precio máximo
              </label>
              <select className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]">
                <option>Sin límite</option>
                <option>USD 50.000</option>
                <option>USD 100.000</option>
                <option>USD 150.000</option>
                <option>USD 200.000</option>
                <option>USD 300.000+</option>
              </select>
            </div>
          </div>

          <button
            className="w-full py-3.5 rounded-xl text-white font-bold text-base transition-all hover:opacity-90 active:scale-[0.99]"
            style={{ backgroundColor: "#c9973a" }}
          >
            Buscar propiedades
          </button>
        </div>

        {/* Quick stats */}
        <div className="flex flex-wrap justify-center gap-8 mt-12">
          {[
            { value: "60+", label: "Años de trayectoria" },
            { value: "3.000+", label: "Propiedades activas" },
            { value: "8.000+", label: "Familias asesoradas" },
            { value: "48hs", label: "Tiempo de respuesta" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <div className="text-3xl font-bold" style={{ color: "#c9973a" }}>{stat.value}</div>
              <div className="text-sm text-blue-200 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 z-10 animate-bounce">
        <svg className="w-6 h-6 text-white opacity-60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </div>
    </section>
  );
}
