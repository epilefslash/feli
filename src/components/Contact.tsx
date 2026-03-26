export default function Contact() {
  return (
    <section id="contacto" className="py-24 sm:py-32 px-6">
      <div className="max-w-3xl mx-auto text-center">
        <h2 className="text-sm font-medium tracking-[0.3em] uppercase text-accent mb-2">
          Hablemos
        </h2>
        <h3 className="text-4xl sm:text-5xl font-bold tracking-tight text-cream mb-6">
          Contacto & Booking
        </h3>
        <p className="text-lg text-cream/60 mb-12 max-w-xl mx-auto">
          Para shows, colaboraciones, prensa o cualquier consulta, escribinos.
        </p>

        <a
          href="mailto:waflesbanda@gmail.com"
          className="inline-block text-2xl sm:text-3xl font-semibold text-accent hover:text-accent-light transition-colors duration-300 border-b-2 border-accent/30 hover:border-accent pb-1"
        >
          waflesbanda@gmail.com
        </a>

        <div className="mt-16 pt-12 border-t border-white/5">
          <p className="text-sm text-muted uppercase tracking-widest mb-8">
            Seguinos
          </p>
          <div className="flex flex-wrap items-center justify-center gap-6">
            {[
              { name: "Instagram", url: "#" },
              { name: "Spotify", url: "#" },
              { name: "YouTube", url: "#" },
              { name: "TikTok", url: "#" },
              { name: "Twitter / X", url: "#" },
            ].map((social) => (
              <a
                key={social.name}
                href={social.url}
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2 border border-white/10 text-sm text-muted hover:text-cream hover:border-white/30 transition-all duration-300"
              >
                {social.name}
              </a>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
