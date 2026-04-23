"use client";

import { useState } from "react";

export default function Alertas() {
  const [email, setEmail] = useState("");
  const [tipo, setTipo] = useState("Departamento");
  const [barrio, setBarrio] = useState("Cualquier barrio");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <section
      className="py-24 relative overflow-hidden"
      style={{ background: "linear-gradient(135deg, #0d1b3e 0%, #1a2d5a 100%)" }}
    >
      {/* Decorative circle */}
      <div
        className="absolute -right-32 -top-32 w-96 h-96 rounded-full opacity-10"
        style={{ backgroundColor: "#c9973a" }}
      />
      <div
        className="absolute -left-20 -bottom-20 w-64 h-64 rounded-full opacity-10"
        style={{ backgroundColor: "#c9973a" }}
      />

      <div className="relative max-w-3xl mx-auto px-6 text-center">
        <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
          Servicio gratuito
        </p>
        <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
          Alertas de propiedades
        </h2>
        <p className="text-blue-200 text-lg mb-10">
          Configurá tu búsqueda y te avisamos al instante cuando aparezca una propiedad
          que se ajuste a tus criterios. Sin spam. Podés cancelar cuando quieras.
        </p>

        {submitted ? (
          <div
            className="rounded-2xl p-10 text-center"
            style={{ backgroundColor: "rgba(201,151,58,0.15)", border: "1px solid rgba(201,151,58,0.4)" }}
          >
            <div className="text-5xl mb-4">✅</div>
            <h3 className="text-2xl font-bold text-white mb-2">¡Alerta configurada!</h3>
            <p className="text-blue-200">
              Te contactaremos a <strong className="text-white">{email}</strong> cuando encontremos
              propiedades que coincidan con tu búsqueda.
            </p>
          </div>
        ) : (
          <form
            onSubmit={handleSubmit}
            className="bg-white rounded-2xl p-8 shadow-2xl text-left"
          >
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-5">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                  Tipo de propiedad
                </label>
                <select
                  value={tipo}
                  onChange={(e) => setTipo(e.target.value)}
                  className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                >
                  {["Departamento", "Casa", "Local", "Terreno", "Cochera", "Oficina"].map((t) => (
                    <option key={t}>{t}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                  Barrio
                </label>
                <select
                  value={barrio}
                  onChange={(e) => setBarrio(e.target.value)}
                  className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                >
                  {["Cualquier barrio", "Centro", "Pichincha", "Fisherton", "Alberdi", "Echesortu", "Norte"].map((b) => (
                    <option key={b}>{b}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                  Precio máximo
                </label>
                <select
                  className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                >
                  {["Sin límite", "USD 50.000", "USD 100.000", "USD 150.000", "USD 200.000", "USD 300.000+"].map((p) => (
                    <option key={p}>{p}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                  Operación
                </label>
                <select
                  className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                >
                  {["Venta", "Alquiler", "Cualquiera"].map((op) => (
                    <option key={op}>{op}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="mb-5">
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                Tu email
              </label>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="tu@email.com"
                className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
              />
            </div>

            <button
              type="submit"
              className="w-full py-4 rounded-xl text-white font-bold text-base transition-opacity hover:opacity-90"
              style={{ backgroundColor: "#c9973a" }}
            >
              Crear alerta gratuita
            </button>

            <p className="text-center text-xs text-gray-400 mt-3">
              Sin spam. Podés cancelar en cualquier momento.
            </p>
          </form>
        )}
      </div>
    </section>
  );
}
