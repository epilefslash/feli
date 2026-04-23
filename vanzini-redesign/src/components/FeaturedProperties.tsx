const properties = [
  {
    id: 1,
    op: "VENTA",
    type: "Departamento",
    price: "USD 95.000",
    address: "Córdoba 1240, Centro",
    rooms: 2,
    baths: 1,
    sqm: 58,
    img: "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80",
    badge: "NUEVO",
  },
  {
    id: 2,
    op: "VENTA",
    type: "Casa",
    price: "USD 185.000",
    address: "Av. Francia 3400, Fisherton",
    rooms: 4,
    baths: 2,
    sqm: 180,
    img: "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80",
    badge: null,
  },
  {
    id: 3,
    op: "ALQUILER",
    type: "Departamento",
    price: "$650.000/mes",
    address: "Sarmiento 850, Centro",
    rooms: 1,
    baths: 1,
    sqm: 42,
    img: "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&q=80",
    badge: "DISPONIBLE",
  },
  {
    id: 4,
    op: "VENTA",
    type: "PH",
    price: "USD 140.000",
    address: "Paraguay 2100, Pichincha",
    rooms: 3,
    baths: 2,
    sqm: 120,
    img: "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=600&q=80",
    badge: null,
  },
  {
    id: 5,
    op: "VENTA",
    type: "Emprendimiento",
    price: "Desde USD 62.000",
    address: "Jujuy 2899, Pichincha",
    rooms: 2,
    baths: 1,
    sqm: 55,
    img: "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&q=80",
    badge: "EN POZO",
  },
  {
    id: 6,
    op: "ALQUILER",
    type: "Oficina",
    price: "$800.000/mes",
    address: "Córdoba 836, Centro",
    rooms: 0,
    baths: 1,
    sqm: 80,
    img: "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80",
    badge: null,
  },
];

function PropertyCard({ p }: { p: typeof properties[0] }) {
  return (
    <article className="group bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 flex flex-col">
      {/* Image */}
      <div className="relative overflow-hidden h-52">
        <img
          src={p.img}
          alt={p.address}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent" />

        {/* Op badge */}
        <span
          className={`absolute top-3 left-3 text-xs font-bold px-3 py-1 rounded-full tracking-wider ${
            p.op === "VENTA"
              ? "bg-[#0d1b3e] text-white"
              : "bg-[#c9973a] text-white"
          }`}
        >
          {p.op}
        </span>

        {/* Status badge */}
        {p.badge && (
          <span className="absolute top-3 right-3 text-xs font-bold px-3 py-1 bg-white/90 text-[#0d1b3e] rounded-full tracking-wider">
            {p.badge}
          </span>
        )}

        {/* Type */}
        <span className="absolute bottom-3 left-3 text-white/80 text-xs font-medium">
          {p.type}
        </span>
      </div>

      {/* Content */}
      <div className="p-5 flex flex-col flex-1">
        <p className="text-2xl font-black text-[#0d1b3e] mb-1">{p.price}</p>
        <p className="text-slate-500 text-sm mb-4 flex items-center gap-1.5">
          <svg className="w-3.5 h-3.5 text-[#c9973a]" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
          </svg>
          {p.address}
        </p>

        {/* Features */}
        <div className="flex items-center gap-4 text-sm text-slate-400 mb-5 mt-auto">
          {p.rooms > 0 && (
            <span className="flex items-center gap-1">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
              </svg>
              {p.rooms} amb.
            </span>
          )}
          <span className="flex items-center gap-1">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            {p.baths} baño{p.baths > 1 ? "s" : ""}
          </span>
          <span className="flex items-center gap-1">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
            </svg>
            {p.sqm} m²
          </span>
        </div>

        <button className="w-full border-2 border-[#0d1b3e] text-[#0d1b3e] hover:bg-[#0d1b3e] hover:text-white font-bold text-sm py-2.5 rounded-xl transition-all duration-200 tracking-wide">
          Ver propiedad
        </button>
      </div>
    </article>
  );
}

export default function FeaturedProperties() {
  return (
    <section className="bg-[#f5f3ef] py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between mb-12 gap-4">
          <div>
            <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-3">
              Propiedades destacadas
            </p>
            <h2 className="text-4xl md:text-5xl font-black text-[#0d1b3e] leading-tight">
              Las mejores oportunidades
              <br />
              del mercado
            </h2>
          </div>
          <button className="flex-shrink-0 flex items-center gap-2 text-[#0d1b3e] font-bold text-sm hover:text-[#c9973a] transition-colors group">
            Ver todas las propiedades
            <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </button>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {properties.map((p) => (
            <PropertyCard key={p.id} p={p} />
          ))}
        </div>

        {/* CTA */}
        <div className="text-center mt-12">
          <button className="bg-[#0d1b3e] hover:bg-[#162244] text-white font-bold px-10 py-4 rounded-xl tracking-wide transition-colors">
            Ver las 3.000+ propiedades →
          </button>
        </div>
      </div>
    </section>
  );
}
