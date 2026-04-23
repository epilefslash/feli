"use client";

import { useState } from "react";

export default function Contacto() {
  const [form, setForm] = useState({ nombre: "", email: "", telefono: "", mensaje: "", interes: "Comprar" });
  const [sent, setSent] = useState(false);

  const set = (field: string, val: string) => setForm((f) => ({ ...f, [field]: val }));

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSent(true);
  };

  return (
    <section id="contacto" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
          {/* Info */}
          <div>
            <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
              Hablemos
            </p>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight mb-6" style={{ color: "#0d1b3e" }}>
              ¿Listo para encontrar<br />tu propiedad?
            </h2>
            <p className="text-gray-500 leading-relaxed mb-10">
              Completá el formulario y un asesor especializado te contactará en menos de 48 horas.
              Primera consulta sin costo ni compromiso.
            </p>

            <div className="space-y-6">
              {[
                {
                  icon: "📍",
                  label: "Dirección",
                  value: "Córdoba 1234, Rosario, Santa Fe",
                },
                {
                  icon: "📞",
                  label: "Teléfono",
                  value: "+54 341 XXX-XXXX",
                },
                {
                  icon: "📧",
                  label: "Email",
                  value: "consultas@vanzini.com.ar",
                },
                {
                  icon: "🕐",
                  label: "Horarios",
                  value: "Lun–Vie 9:00–18:00 | Sáb 9:00–13:00",
                },
              ].map((c) => (
                <div key={c.label} className="flex items-start gap-4">
                  <span className="text-2xl flex-shrink-0">{c.icon}</span>
                  <div>
                    <div className="text-xs font-bold uppercase tracking-wider text-gray-400 mb-0.5">{c.label}</div>
                    <div className="text-gray-700 font-medium">{c.value}</div>
                  </div>
                </div>
              ))}
            </div>

            {/* Social */}
            <div className="mt-10 pt-8 border-t border-gray-100">
              <div className="text-xs font-bold uppercase tracking-wider text-gray-400 mb-4">Seguinos en redes</div>
              <div className="flex gap-4">
                {[
                  { name: "Instagram", handle: "@vanzinipropiedades", icon: "📸" },
                  { name: "TikTok", handle: "@vanzini", icon: "🎵" },
                  { name: "Facebook", handle: "Vanzini Propiedades", icon: "👥" },
                ].map((s) => (
                  <div key={s.name} className="flex items-center gap-2 text-sm text-gray-600">
                    <span>{s.icon}</span>
                    <span>{s.handle}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Form */}
          <div>
            {sent ? (
              <div
                className="rounded-2xl p-12 text-center h-full flex flex-col items-center justify-center"
                style={{ backgroundColor: "#f8f4ee" }}
              >
                <div className="text-6xl mb-4">🎉</div>
                <h3 className="text-2xl font-bold mb-2" style={{ color: "#0d1b3e" }}>¡Mensaje enviado!</h3>
                <p className="text-gray-500">
                  Un asesor de Vanzini se comunicará con vos en las próximas 48 horas.
                </p>
              </div>
            ) : (
              <form
                onSubmit={handleSubmit}
                className="rounded-2xl p-8 border border-gray-100 shadow-sm"
                style={{ backgroundColor: "#f8f4ee" }}
              >
                <div className="mb-5">
                  <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                    Me interesa...
                  </label>
                  <div className="flex gap-2">
                    {["Comprar", "Alquilar", "Invertir", "Vender"].map((op) => (
                      <button
                        key={op}
                        type="button"
                        onClick={() => set("interes", op)}
                        className="flex-1 py-2 rounded-lg text-sm font-semibold transition-all"
                        style={
                          form.interes === op
                            ? { backgroundColor: "#0d1b3e", color: "white" }
                            : { backgroundColor: "white", color: "#6b7280", border: "1px solid #e5e7eb" }
                        }
                      >
                        {op}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                      Nombre *
                    </label>
                    <input
                      required
                      type="text"
                      value={form.nombre}
                      onChange={(e) => set("nombre", e.target.value)}
                      className="w-full border border-gray-200 bg-white rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                      placeholder="Tu nombre"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                      Teléfono
                    </label>
                    <input
                      type="tel"
                      value={form.telefono}
                      onChange={(e) => set("telefono", e.target.value)}
                      className="w-full border border-gray-200 bg-white rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                      placeholder="+54 341..."
                    />
                  </div>
                </div>

                <div className="mb-4">
                  <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                    Email *
                  </label>
                  <input
                    required
                    type="email"
                    value={form.email}
                    onChange={(e) => set("email", e.target.value)}
                    className="w-full border border-gray-200 bg-white rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a]"
                    placeholder="tu@email.com"
                  />
                </div>

                <div className="mb-6">
                  <label className="block text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
                    Contanos qué buscás
                  </label>
                  <textarea
                    value={form.mensaje}
                    onChange={(e) => set("mensaje", e.target.value)}
                    rows={4}
                    className="w-full border border-gray-200 bg-white rounded-xl px-4 py-3 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#c9973a] resize-none"
                    placeholder="Ej: Busco un departamento de 2 ambientes en Pichincha, hasta USD 90.000..."
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-4 rounded-xl text-white font-bold text-base transition-all hover:opacity-90"
                  style={{ backgroundColor: "#c9973a" }}
                >
                  Enviar consulta →
                </button>

                <p className="text-center text-xs text-gray-400 mt-3">
                  Respuesta garantizada en menos de 48 horas
                </p>
              </form>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
