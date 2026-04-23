const team = [
  {
    name: "Martín Vanzini",
    role: "Director General",
    exp: "35 años de experiencia",
    img: "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&q=80",
    specialties: ["Emprendimientos", "Inversiones"],
  },
  {
    name: "Carolina Ríos",
    role: "Jefa de Alquileres",
    exp: "12 años de experiencia",
    img: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&q=80",
    specialties: ["Alquileres", "Administración"],
  },
  {
    name: "Diego Ferreira",
    role: "Asesor Senior",
    exp: "18 años de experiencia",
    img: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=300&q=80",
    specialties: ["Compra-venta", "Centro"],
  },
  {
    name: "Lucía Castellano",
    role: "Tasadora Oficial",
    exp: "10 años de experiencia",
    img: "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&q=80",
    specialties: ["Tasaciones", "Fisherton"],
  },
];

export default function Team() {
  return (
    <section className="bg-white py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="text-center mb-14">
          <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-3">
            Nuestro equipo
          </p>
          <h2 className="text-4xl md:text-5xl font-black text-[#0d1b3e] leading-tight mb-4">
            Personas reales, resultados reales
          </h2>
          <p className="text-slate-500 text-lg max-w-lg mx-auto">
            Más de 30 profesionales especializados por zona y tipo de propiedad.
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {team.map((m) => (
            <div key={m.name} className="group text-center">
              {/* Photo */}
              <div className="relative w-40 h-40 mx-auto mb-5 rounded-2xl overflow-hidden">
                <img
                  src={m.img}
                  alt={m.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#0d1b3e]/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
              </div>

              <h3 className="font-bold text-[#0d1b3e] text-lg mb-0.5">{m.name}</h3>
              <p className="text-[#c9973a] text-sm font-semibold mb-1">{m.role}</p>
              <p className="text-slate-400 text-xs mb-3">{m.exp}</p>

              <div className="flex flex-wrap justify-center gap-1.5">
                {m.specialties.map((s) => (
                  <span key={s} className="bg-slate-100 text-slate-500 text-xs px-2.5 py-1 rounded-full font-medium">
                    {s}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* CTA */}
        <div className="mt-16 bg-[#f5f3ef] rounded-3xl p-10 flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 className="text-2xl font-black text-[#0d1b3e] mb-2">¿Querés trabajar con nosotros?</h3>
            <p className="text-slate-500">Sumamos profesionales con vocación de servicio y ambición de crecimiento.</p>
          </div>
          <button className="flex-shrink-0 bg-[#0d1b3e] hover:bg-[#162244] text-white font-bold px-8 py-4 rounded-xl tracking-wide transition-colors">
            Ver posiciones abiertas →
          </button>
        </div>
      </div>
    </section>
  );
}
