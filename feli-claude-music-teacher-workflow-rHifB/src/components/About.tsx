export default function About() {
  return (
    <section id="banda" className="py-24 sm:py-32 px-6">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-sm font-medium tracking-[0.3em] uppercase text-accent mb-2">
          Quiénes somos
        </h2>
        <h3 className="text-4xl sm:text-5xl font-bold tracking-tight text-cream mb-16">
          La banda
        </h3>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          {/* Image */}
          <div className="relative">
            <div
              className="aspect-[4/3] bg-surface-light bg-cover bg-center"
              style={{ backgroundImage: "url('/images/band.jpg')" }}
            />
            <div className="absolute inset-0 bg-gradient-to-t from-dark/30 to-transparent" />
          </div>

          {/* Text */}
          <div className="space-y-6">
            <p className="text-lg text-cream/80 leading-relaxed">
              Wafles nació en Buenos Aires con la idea de mezclar sonidos que nos
              gustan sin ponerles etiqueta. Somos un grupo de amigos haciendo
              música que nos divierte y nos mueve.
            </p>
            <p className="text-lg text-cream/80 leading-relaxed">
              Con una formación amplia y versátil, cada show es una experiencia
              diferente. Guitarras, teclados, vientos, voces y mucha energía
              arriba del escenario.
            </p>
            <p className="text-lg text-cream/80 leading-relaxed">
              Desde nuestros primeros ensayos hasta las fechas en vivo, la
              premisa siempre fue la misma: pasarla bien y que la gente se lleve
              algo de eso.
            </p>
            <div className="pt-4">
              <div className="flex flex-wrap gap-x-8 gap-y-3 text-sm text-muted">
                <span>Buenos Aires, Argentina</span>
                <span>Est. 2023</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
