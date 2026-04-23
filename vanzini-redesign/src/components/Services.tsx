const services = [
  {
    icon: (
      <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
          d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75" />
      </svg>
    ),
    title: "Compra y Venta",
    desc: "Acompañamiento integral desde la búsqueda hasta la escritura. Valuación precisa y estrategia de precio óptima.",
    features: ["Análisis de mercado", "Fotografía profesional", "Publicación en portales", "Gestión notarial"],
  },
  {
    icon: (
      <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
          d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
      </svg>
    ),
    title: "Alquileres",
    desc: "Gestión completa de alquileres. Selección de inquilinos, contratos y administración mensual sin preocupaciones.",
    features: ["Selección de inquilinos", "Contrato digital", "Cobro y transferencia", "Gestión de problemas"],
  },
  {
    icon: (
      <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
          d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    ),
    title: "Tasaciones",
    desc: "Valoración oficial de tu propiedad en 48 horas. Certificado respaldado por el Colegio de Corredores Inmobiliarios.",
    features: ["Visita presencial", "Análisis comparativo", "Informe digital", "Certificado oficial COCIR"],
  },
  {
    icon: (
      <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
          d="M3.75 21h16.5M4.5 3h15M5.25 3v18m13.5-18v18M9 6.75h1.5m-1.5 3h1.5m-1.5 3h1.5m3-6H15m-1.5 3H15m-1.5 3H15M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21" />
      </svg>
    ),
    title: "Emprendimientos",
    desc: "Comercialización de proyectos en pozo. Representamos los mejores desarrollos de Rosario con planes en cuotas.",
    features: ["Proyectos seleccionados", "Financiación directa", "Seguimiento de obra", "Unidades desde el pozo"],
  },
];

export default function Services() {
  return (
    <section className="bg-white py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="text-center mb-16">
          <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-3">
            Nuestros servicios
          </p>
          <h2 className="text-4xl md:text-5xl font-black text-[#0d1b3e] leading-tight mb-4">
            Todo lo que necesitás
            <br />en un solo lugar
          </h2>
          <p className="text-slate-500 text-lg max-w-lg mx-auto">
            Cubrimos cada etapa del proceso inmobiliario con profesionalismo y transparencia.
          </p>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {services.map((s) => (
            <div
              key={s.title}
              className="group p-8 rounded-2xl border-2 border-slate-100 hover:border-[#c9973a] hover:shadow-xl transition-all duration-300 cursor-pointer"
            >
              <div className="w-14 h-14 bg-[#0d1b3e] group-hover:bg-[#c9973a] rounded-xl flex items-center justify-center text-[#c9973a] group-hover:text-white mb-6 transition-colors duration-300">
                {s.icon}
              </div>
              <h3 className="text-xl font-bold text-[#0d1b3e] mb-3">{s.title}</h3>
              <p className="text-slate-500 text-sm leading-relaxed mb-5">{s.desc}</p>
              <ul className="space-y-2">
                {s.features.map((f) => (
                  <li key={f} className="flex items-center gap-2 text-sm text-slate-400">
                    <span className="w-1.5 h-1.5 rounded-full bg-[#c9973a] flex-shrink-0" />
                    {f}
                  </li>
                ))}
              </ul>
              <button className="mt-6 text-[#0d1b3e] group-hover:text-[#c9973a] text-sm font-bold flex items-center gap-1 transition-colors">
                Saber más
                <svg className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
