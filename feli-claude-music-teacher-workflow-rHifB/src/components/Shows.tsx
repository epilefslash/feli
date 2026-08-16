const shows = [
  {
    date: "12 ABR",
    venue: "Distrito Siete",
    city: "CABA",
    ticketUrl: "#",
    status: "Próximo",
  },
  {
    date: "26 ABR",
    venue: "La Tangente",
    city: "CABA",
    ticketUrl: "#",
    status: "Próximo",
  },
  {
    date: "10 MAY",
    venue: "Camping",
    city: "Córdoba",
    ticketUrl: "#",
    status: "Próximo",
  },
  {
    date: "24 MAY",
    venue: "Centro Cultural Recoleta",
    city: "CABA",
    ticketUrl: "#",
    status: "Próximo",
  },
];

export default function Shows() {
  return (
    <section id="shows" className="py-24 sm:py-32 px-6 bg-surface">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-sm font-medium tracking-[0.3em] uppercase text-accent mb-2">
          En vivo
        </h2>
        <h3 className="text-4xl sm:text-5xl font-bold tracking-tight text-cream mb-16">
          Próximas fechas
        </h3>

        <div className="space-y-0">
          {shows.map((show, i) => (
            <div
              key={i}
              className="group flex flex-col sm:flex-row items-start sm:items-center justify-between py-6 border-b border-white/5 hover:border-white/10 transition-colors"
            >
              <div className="flex items-baseline gap-6 mb-3 sm:mb-0">
                <span className="text-2xl sm:text-3xl font-bold text-cream font-mono tracking-tight min-w-[120px]">
                  {show.date}
                </span>
                <div>
                  <h4 className="text-lg font-semibold text-cream group-hover:text-accent transition-colors">
                    {show.venue}
                  </h4>
                  <p className="text-sm text-muted">{show.city}</p>
                </div>
              </div>
              <a
                href={show.ticketUrl}
                className="px-6 py-2 border border-accent/50 text-accent text-sm font-medium uppercase tracking-wider hover:bg-accent hover:text-dark transition-all duration-300"
              >
                Entradas
              </a>
            </div>
          ))}
        </div>

        {shows.length === 0 && (
          <p className="text-muted text-center text-lg">
            No hay fechas programadas por ahora. Seguinos en redes para
            enterarte primero.
          </p>
        )}
      </div>
    </section>
  );
}
