const testimonials = [
  {
    name: "Claudia Méndez",
    role: "Compradora — Departamento en Pichincha",
    text: "En menos de 3 semanas encontramos el departamento ideal. El equipo de Vanzini entendió exactamente lo que buscábamos y manejó toda la documentación sin errores. Totalmente recomendable.",
    stars: 5,
    avatar: "CM",
  },
  {
    name: "Roberto Galván",
    role: "Vendedor — Casa en Fisherton",
    text: "Puse la casa en venta con Vanzini y se vendió al precio que pedí en 45 días. La estrategia de fotografía y publicación fue impecable. Muy profesionales en todo el proceso.",
    stars: 5,
    avatar: "RG",
  },
  {
    name: "Sofía Ibáñez",
    role: "Inversora — Emprendimiento en pozo",
    text: "Me asesoraron sobre el mejor emprendimiento para invertir según mi capital. Hoy mi unidad ya valorizó un 40% desde el pozo. Claridad y honestidad en todo momento.",
    stars: 5,
    avatar: "SI",
  },
  {
    name: "Martín Peluso",
    role: "Propietario — Alquiler en Centro",
    text: "Delegué la gestión de mi departamento en alquiler y no me preocupo por nada. Cobro todos los meses, sin retrasos, y si hay algún problema lo resuelven ellos.",
    stars: 5,
    avatar: "MP",
  },
];

export default function Testimonials() {
  return (
    <section className="bg-[#f5f3ef] py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="text-center mb-14">
          <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-3">
            Testimonios
          </p>
          <h2 className="text-4xl md:text-5xl font-black text-[#0d1b3e] leading-tight mb-4">
            Lo que dicen nuestros clientes
          </h2>
          <div className="flex items-center justify-center gap-3">
            <div className="flex">
              {[...Array(5)].map((_, i) => (
                <svg key={i} className="w-5 h-5 text-[#c9973a]" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                </svg>
              ))}
            </div>
            <span className="text-[#0d1b3e] font-bold">4.8 / 5</span>
            <span className="text-slate-400 text-sm">· +900 reseñas verificadas</span>
          </div>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {testimonials.map((t) => (
            <div
              key={t.name}
              className="bg-white rounded-2xl p-8 shadow-sm hover:shadow-md transition-shadow"
            >
              {/* Stars */}
              <div className="flex gap-0.5 mb-4">
                {[...Array(t.stars)].map((_, i) => (
                  <svg key={i} className="w-4 h-4 text-[#c9973a]" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                  </svg>
                ))}
              </div>

              {/* Quote */}
              <p className="text-slate-600 leading-relaxed mb-6 text-base">
                &ldquo;{t.text}&rdquo;
              </p>

              {/* Author */}
              <div className="flex items-center gap-3">
                <div className="w-11 h-11 rounded-full bg-[#0d1b3e] flex items-center justify-center text-white font-bold text-sm flex-shrink-0">
                  {t.avatar}
                </div>
                <div>
                  <p className="font-bold text-[#0d1b3e] text-sm">{t.name}</p>
                  <p className="text-slate-400 text-xs">{t.role}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
