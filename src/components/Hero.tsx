"use client";

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background image */}
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style={{ backgroundImage: "url('/images/hero.jpg')" }}
      />
      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-dark/70 via-dark/50 to-dark" />

      <div className="relative z-10 text-center px-6 max-w-4xl mx-auto">
        <h1 className="text-7xl sm:text-8xl md:text-9xl font-black tracking-tighter leading-none text-cream animate-fade-up opacity-0">
          WAFLES
        </h1>
        <p className="mt-6 text-lg sm:text-xl text-cream/70 font-light tracking-wide animate-fade-up animate-delay-200 opacity-0">
          Buenos Aires, Argentina
        </p>
        <div className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-up animate-delay-400 opacity-0">
          <a
            href="#musica"
            className="px-8 py-3 bg-accent text-dark font-semibold tracking-wide uppercase text-sm rounded-none hover:bg-accent-light transition-colors duration-300"
          >
            Escuchá nuestra música
          </a>
          <a
            href="#shows"
            className="px-8 py-3 border border-cream/30 text-cream font-medium tracking-wide uppercase text-sm rounded-none hover:border-cream hover:bg-cream/5 transition-all duration-300"
          >
            Próximas fechas
          </a>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-fade-in animate-delay-600 opacity-0">
        <div className="w-[1px] h-16 bg-gradient-to-b from-transparent via-cream/40 to-transparent" />
      </div>
    </section>
  );
}
