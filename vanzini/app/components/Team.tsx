const equipo = [
  {
    nombre: "Alejandro Vanzini",
    cargo: "Director & Fundador",
    especialidad: "Inversiones y operaciones premium",
    experiencia: "35+ años",
    iniciales: "AV",
    color: "#0d1b3e",
  },
  {
    nombre: "Valentina Rossi",
    cargo: "Asesora Comercial Senior",
    especialidad: "Departamentos en venta — Centro y Pichincha",
    experiencia: "12 años",
    iniciales: "VR",
    color: "#c9973a",
  },
  {
    nombre: "Martín Gómez",
    cargo: "Asesor Comercial",
    especialidad: "Propiedades residenciales — Fisherton y Norte",
    experiencia: "8 años",
    iniciales: "MG",
    color: "#1a2d5a",
  },
  {
    nombre: "Carla Mendez",
    cargo: "Gestora de Alquileres",
    especialidad: "Contratos, indexación y administración",
    experiencia: "10 años",
    iniciales: "CM",
    color: "#7c5c2a",
  },
];

export default function Team() {
  return (
    <section id="nosotros" className="py-24" style={{ backgroundColor: "#f8f4ee" }}>
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-16">
          <div>
            <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
              Nuestro equipo
            </p>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight" style={{ color: "#0d1b3e" }}>
              Personas reales.<br />Resultados reales.
            </h2>
            <div className="mt-4 w-16 h-1 rounded-full" style={{ backgroundColor: "#c9973a" }} />
          </div>
          <div>
            <p className="text-gray-600 leading-relaxed text-lg">
              En inmobiliaria no comprás metros cuadrados — comprás confianza. Por eso cada asesor
              de Vanzini se especializa en una zona y tipo de propiedad, para que recibas el
              mejor asesoramiento posible.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {equipo.map((p) => (
            <div
              key={p.nombre}
              className="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition-all duration-300 border border-gray-100 text-center"
            >
              {/* Avatar */}
              <div
                className="w-20 h-20 rounded-full flex items-center justify-center text-2xl font-bold text-white mx-auto mb-4"
                style={{ backgroundColor: p.color }}
              >
                {p.iniciales}
              </div>

              <h3 className="font-bold text-lg mb-0.5" style={{ color: "#0d1b3e" }}>{p.nombre}</h3>
              <p className="text-sm font-semibold mb-3" style={{ color: "#c9973a" }}>{p.cargo}</p>
              <p className="text-gray-500 text-xs leading-relaxed mb-4">{p.especialidad}</p>

              <div
                className="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-full"
                style={{ backgroundColor: "rgba(13,27,62,0.07)", color: "#0d1b3e" }}
              >
                <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {p.experiencia} de experiencia
              </div>

              <div className="mt-4 pt-4 border-t border-gray-100">
                <a
                  href="#contacto"
                  className="text-sm font-semibold transition-opacity hover:opacity-70"
                  style={{ color: "#c9973a" }}
                >
                  Contactar →
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
