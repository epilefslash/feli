const barrios = [
  {
    nombre: "Centro",
    descripcion: "El corazón comercial y cultural de Rosario. Alta demanda de alquileres para profesionales.",
    precioPromedio: "USD 95.000",
    propiedades: 312,
    emoji: "🏙️",
    tags: ["Alta demanda", "Comercial", "Conectado"],
  },
  {
    nombre: "Pichincha",
    descripcion: "Barrio con identidad propia, arquitectura distintiva y vida nocturna. Ideal para inversión.",
    precioPromedio: "USD 78.000",
    propiedades: 186,
    emoji: "🎨",
    tags: ["Tendencia", "Inversión", "Bohemio"],
  },
  {
    nombre: "Fisherton",
    descripcion: "El barrio residencial más exclusivo. Casas con jardín, colegios top y aire tranquilo.",
    precioPromedio: "USD 185.000",
    propiedades: 143,
    emoji: "🌳",
    tags: ["Premium", "Familias", "Tranquilo"],
  },
  {
    nombre: "Alberdi",
    descripcion: "Barrio con fuerte actividad comercial y excelente conectividad al transporte público.",
    precioPromedio: "USD 68.000",
    propiedades: 224,
    emoji: "🚌",
    tags: ["Accesible", "Comercial", "Conectado"],
  },
  {
    nombre: "Echesortu",
    descripcion: "Barrio familiar consolidado con plazas, escuelas y oferta de departamentos modernos.",
    precioPromedio: "USD 72.000",
    propiedades: 168,
    emoji: "🌿",
    tags: ["Familiar", "Tranquilo", "Servicios"],
  },
  {
    nombre: "Norte / Fisherton",
    descripcion: "Zona de rápida expansión con terrenos y desarrollos nuevos de alto retorno a futuro.",
    precioPromedio: "USD 55.000",
    propiedades: 97,
    emoji: "📈",
    tags: ["Crecimiento", "Terrenos", "Potencial"],
  },
];

export default function Barrios() {
  return (
    <section id="barrios" className="py-24" style={{ backgroundColor: "#f8f4ee" }}>
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-14">
          <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
            Guía de zonas
          </p>
          <h2 className="text-4xl md:text-5xl font-bold" style={{ color: "#0d1b3e" }}>
            Conocé los barrios<br />de Rosario
          </h2>
          <p className="text-gray-600 mt-4 max-w-xl mx-auto">
            Cada zona tiene su carácter. Te ayudamos a elegir la que más se adapta a tu estilo de vida o estrategia de inversión.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {barrios.map((b) => (
            <div
              key={b.nombre}
              className="bg-white rounded-2xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 group cursor-pointer"
            >
              <div className="flex items-start justify-between mb-4">
                <div className="text-4xl">{b.emoji}</div>
                <div className="text-right">
                  <div className="text-xs text-gray-400 uppercase tracking-wider">Precio prom.</div>
                  <div className="text-lg font-bold" style={{ color: "#0d1b3e" }}>{b.precioPromedio}</div>
                </div>
              </div>

              <h3 className="text-xl font-bold mb-2" style={{ color: "#0d1b3e" }}>{b.nombre}</h3>
              <p className="text-gray-500 text-sm leading-relaxed mb-4">{b.descripcion}</p>

              <div className="flex flex-wrap gap-2 mb-4">
                {b.tags.map((tag) => (
                  <span
                    key={tag}
                    className="text-xs font-semibold px-2.5 py-1 rounded-full"
                    style={{ backgroundColor: "rgba(201,151,58,0.12)", color: "#a07020" }}
                  >
                    {tag}
                  </span>
                ))}
              </div>

              <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                <span className="text-sm text-gray-400">{b.propiedades} propiedades</span>
                <a
                  href="#contacto"
                  className="text-sm font-semibold flex items-center gap-1 transition-opacity hover:opacity-70"
                  style={{ color: "#c9973a" }}
                >
                  Ver más
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
