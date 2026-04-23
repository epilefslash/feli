const neighborhoods = [
  {
    name: "Centro",
    tagline: "El corazón de Rosario",
    avgPrice: "USD 1.900/m²",
    count: 342,
    img: "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=500&q=80",
    color: "from-blue-900",
  },
  {
    name: "Pichincha",
    tagline: "Barrio bohemio y en auge",
    avgPrice: "USD 1.600/m²",
    count: 218,
    img: "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=500&q=80",
    color: "from-emerald-900",
  },
  {
    name: "Fisherton",
    tagline: "Tranquilidad y verde",
    avgPrice: "USD 1.400/m²",
    count: 187,
    img: "https://images.unsplash.com/photo-1560472355-536de3962603?w=500&q=80",
    color: "from-teal-900",
  },
  {
    name: "Alberdi",
    tagline: "Clásico y en renovación",
    avgPrice: "USD 1.200/m²",
    count: 156,
    img: "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=500&q=80",
    color: "from-purple-900",
  },
  {
    name: "Echesortu",
    tagline: "Residencial y tranquilo",
    avgPrice: "USD 1.350/m²",
    count: 98,
    img: "https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=500&q=80",
    color: "from-orange-900",
  },
  {
    name: "Belgrano Norte",
    tagline: "Inversión en crecimiento",
    avgPrice: "USD 1.100/m²",
    count: 74,
    img: "https://images.unsplash.com/photo-1486325212027-8081e485255e?w=500&q=80",
    color: "from-slate-900",
  },
];

export default function NeighborhoodGuides() {
  return (
    <section className="bg-[#0d1b3e] py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="text-center mb-14">
          <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-3">
            Guías de barrios
          </p>
          <h2 className="text-4xl md:text-5xl font-black text-white leading-tight mb-4">
            Conocé cada rincón de Rosario
          </h2>
          <p className="text-white/45 text-lg max-w-xl mx-auto">
            Precios promedio, perfil de barrio y propiedades disponibles en cada zona.
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {neighborhoods.map((n) => (
            <article
              key={n.name}
              className="group relative rounded-2xl overflow-hidden cursor-pointer h-64"
            >
              <img
                src={n.img}
                alt={n.name}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
              <div className={`absolute inset-0 bg-gradient-to-t ${n.color}/80 to-transparent`} />
              <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent" />

              {/* Content */}
              <div className="absolute inset-0 p-6 flex flex-col justify-end">
                <div className="flex items-end justify-between">
                  <div>
                    <h3 className="text-2xl font-black text-white mb-0.5">{n.name}</h3>
                    <p className="text-white/60 text-sm">{n.tagline}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-[#c9973a] font-bold text-sm">{n.avgPrice}</p>
                    <p className="text-white/50 text-xs">{n.count} propiedades</p>
                  </div>
                </div>

                {/* Hover CTA */}
                <div className="mt-4 transform translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                  <button className="w-full bg-[#c9973a] text-white text-xs font-bold py-2 rounded-lg tracking-wider uppercase">
                    Ver propiedades en {n.name}
                  </button>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
