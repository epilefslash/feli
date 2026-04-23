const propiedades = [
  {
    id: 1,
    tipo: "Departamento",
    operacion: "Venta",
    barrio: "Pichincha",
    ambientes: 2,
    m2: 65,
    precio: "USD 85.000",
    tag: "Destacado",
    tagColor: "#c9973a",
    img: "🏢",
    desc: "Luminoso departamento a estrenar, balcón corrido, cocina integrada.",
  },
  {
    id: 2,
    tipo: "Casa",
    operacion: "Venta",
    barrio: "Fisherton",
    ambientes: 4,
    m2: 180,
    precio: "USD 220.000",
    tag: "Exclusivo",
    tagColor: "#0d1b3e",
    img: "🏡",
    desc: "Casa con jardín, pileta y cochera doble en barrio cerrado premium.",
  },
  {
    id: 3,
    tipo: "Departamento",
    operacion: "Alquiler",
    barrio: "Centro",
    ambientes: 1,
    m2: 38,
    precio: "$ 420.000 / mes",
    tag: "Nuevo",
    tagColor: "#16a34a",
    img: "🏙️",
    desc: "Monoambiente moderno con amenities, ideal para profesionales.",
  },
  {
    id: 4,
    tipo: "Local",
    operacion: "Alquiler",
    barrio: "Echesortu",
    ambientes: 1,
    m2: 90,
    precio: "$ 850.000 / mes",
    tag: "Comercial",
    tagColor: "#7c3aed",
    img: "🏪",
    desc: "Local a la calle con depósito, sobre avenida comercial de alto tráfico.",
  },
  {
    id: 5,
    tipo: "Terreno",
    operacion: "Venta",
    barrio: "Norte",
    ambientes: 0,
    m2: 600,
    precio: "USD 95.000",
    tag: "Inversión",
    tagColor: "#c9973a",
    img: "🌿",
    desc: "Terreno en esquina en zona de rápido desarrollo. Apto multifamiliar.",
  },
  {
    id: 6,
    tipo: "Departamento",
    operacion: "Venta",
    barrio: "Alberdi",
    ambientes: 3,
    m2: 95,
    precio: "USD 130.000",
    tag: "Oportunidad",
    tagColor: "#dc2626",
    img: "🏢",
    desc: "3 dormitorios, 2 baños, parrilla. Edificio con seguridad 24hs.",
  },
];

export default function Listings() {
  return (
    <section id="propiedades" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-14 gap-4">
          <div>
            <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
              Portafolio activo
            </p>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight" style={{ color: "#0d1b3e" }}>
              Propiedades<br />destacadas
            </h2>
            <div className="mt-4 w-16 h-1 rounded-full" style={{ backgroundColor: "#c9973a" }} />
          </div>
          <a
            href="#contacto"
            className="inline-flex items-center gap-2 text-sm font-semibold transition-opacity hover:opacity-80"
            style={{ color: "#0d1b3e" }}
          >
            Ver todas las propiedades
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </a>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {propiedades.map((p) => (
            <div
              key={p.id}
              className="group rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 bg-white"
            >
              {/* Image placeholder */}
              <div
                className="relative h-52 flex items-center justify-center text-6xl"
                style={{ backgroundColor: "#f0f4f8" }}
              >
                {p.img}
                <span
                  className="absolute top-3 left-3 text-xs font-bold px-3 py-1 rounded-full text-white"
                  style={{ backgroundColor: p.tagColor }}
                >
                  {p.tag}
                </span>
                <span
                  className="absolute top-3 right-3 text-xs font-semibold px-3 py-1 rounded-full text-white"
                  style={{ backgroundColor: "rgba(13,27,62,0.85)" }}
                >
                  {p.operacion}
                </span>
              </div>

              <div className="p-5">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-xs font-semibold uppercase tracking-wider text-gray-400">{p.tipo}</span>
                  <span className="text-gray-300">•</span>
                  <span className="text-xs font-semibold uppercase tracking-wider text-gray-400">{p.barrio}</span>
                </div>

                <p className="text-gray-600 text-sm leading-relaxed mb-4">{p.desc}</p>

                <div className="flex items-center gap-4 text-sm text-gray-500 mb-4">
                  {p.ambientes > 0 && (
                    <span className="flex items-center gap-1">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                      </svg>
                      {p.ambientes} amb.
                    </span>
                  )}
                  <span className="flex items-center gap-1">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
                    </svg>
                    {p.m2} m²
                  </span>
                </div>

                <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                  <span className="text-xl font-bold" style={{ color: "#0d1b3e" }}>{p.precio}</span>
                  <a
                    href="#contacto"
                    className="text-sm font-semibold px-4 py-2 rounded-lg transition-all text-white"
                    style={{ backgroundColor: "#c9973a" }}
                  >
                    Consultar
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
