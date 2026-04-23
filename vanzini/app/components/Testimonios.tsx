const reviews = [
  {
    nombre: "Gabriela Torres",
    rol: "Compradora — Departamento en Pichincha",
    texto:
      "Encontré el departamento que buscaba en menos de dos semanas. Valentina me acompañó en cada paso, desde la visita hasta la escritura. No esperaba ese nivel de atención.",
    estrellas: 5,
  },
  {
    nombre: "Rodrigo Keller",
    rol: "Inversor — Terrenos en Fisherton Norte",
    texto:
      "Opero con Vanzini desde hace 8 años. Siempre me dan información de mercado real antes de comprar. La rentabilidad de mis inversiones habla por sí sola.",
    estrellas: 5,
  },
  {
    nombre: "Laura Fenandez",
    rol: "Propietaria — Alquiler de local comercial",
    texto:
      "Carla me consiguió un inquilino en 10 días y se encarga de todo: contratos, indexación y mantenimiento. Mis propiedades nunca estuvieron tan bien administradas.",
    estrellas: 5,
  },
  {
    nombre: "Tomás Echevarría",
    rol: "Comprador — Casa en Fisherton",
    texto:
      "Asesoramiento impecable para el crédito hipotecario. Martín nos explicó cada opción y nos consiguió una tasa que el banco no nos había ofrecido directamente.",
    estrellas: 5,
  },
];

export default function Testimonios() {
  return (
    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-14">
          <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
            Lo que dicen nuestros clientes
          </p>
          <h2 className="text-4xl md:text-5xl font-bold" style={{ color: "#0d1b3e" }}>
            8.000 familias no pueden<br />equivocarse
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {reviews.map((r) => (
            <div
              key={r.nombre}
              className="rounded-2xl p-8 border border-gray-100 shadow-sm hover:shadow-md transition-all"
              style={{ backgroundColor: "#f8f4ee" }}
            >
              {/* Stars */}
              <div className="flex gap-1 mb-4">
                {Array.from({ length: r.estrellas }).map((_, i) => (
                  <svg key={i} className="w-5 h-5" fill="#c9973a" viewBox="0 0 24 24">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                  </svg>
                ))}
              </div>

              <p className="text-gray-700 leading-relaxed text-base mb-6 italic">"{r.texto}"</p>

              <div className="flex items-center gap-3">
                <div
                  className="w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold text-white flex-shrink-0"
                  style={{ backgroundColor: "#0d1b3e" }}
                >
                  {r.nombre.split(" ").map((n) => n[0]).join("")}
                </div>
                <div>
                  <div className="font-semibold text-sm" style={{ color: "#0d1b3e" }}>{r.nombre}</div>
                  <div className="text-xs text-gray-400">{r.rol}</div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Google rating bar */}
        <div
          className="mt-12 rounded-2xl p-8 flex flex-col md:flex-row items-center gap-8 text-white"
          style={{ backgroundColor: "#0d1b3e" }}
        >
          <div className="text-center md:text-left">
            <div className="text-6xl font-bold" style={{ color: "#c9973a" }}>4.8</div>
            <div className="flex justify-center md:justify-start gap-1 mt-2">
              {[1, 2, 3, 4, 5].map((i) => (
                <svg key={i} className="w-5 h-5" fill={i <= 4 ? "#c9973a" : "#6b7280"} viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                </svg>
              ))}
            </div>
            <div className="text-blue-300 text-sm mt-1">Basado en +420 reseñas en Google</div>
          </div>
          <div className="flex-1 w-full">
            {[
              { label: "5 estrellas", pct: 82 },
              { label: "4 estrellas", pct: 11 },
              { label: "3 estrellas", pct: 4 },
              { label: "2 o menos", pct: 3 },
            ].map((row) => (
              <div key={row.label} className="flex items-center gap-3 mb-2">
                <span className="text-xs text-blue-200 w-20">{row.label}</span>
                <div className="flex-1 h-2 rounded-full bg-blue-900 overflow-hidden">
                  <div
                    className="h-full rounded-full"
                    style={{ width: `${row.pct}%`, backgroundColor: "#c9973a" }}
                  />
                </div>
                <span className="text-xs text-blue-300 w-8 text-right">{row.pct}%</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
