const propLinks = ["Departamentos", "Casas", "PH", "Oficinas", "Locales", "Terrenos", "Cocheras", "Emprendimientos"];
const barriosLinks = ["Centro", "Pichincha", "Fisherton", "Alberdi", "Echesortu", "Belgrano Norte"];
const serviciosLinks = ["Compra y Venta", "Alquileres", "Tasaciones", "Administración", "Financiamiento"];

export default function Footer() {
  return (
    <footer className="bg-[#080f1f] pt-20 pb-8">
      <div className="max-w-7xl mx-auto px-6">
        {/* Top grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-10 pb-16 border-b border-white/8">
          {/* Brand */}
          <div className="lg:col-span-2">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-9 h-9 bg-[#c9973a] rounded-sm flex items-center justify-center">
                <span className="text-white font-black text-sm">V</span>
              </div>
              <span className="text-white font-bold text-xl tracking-widest uppercase">Vanzini</span>
            </div>
            <p className="text-white/40 text-sm leading-relaxed mb-6 max-w-xs">
              Liderando el mercado inmobiliario de Rosario desde 1965. Más de 60 años conectando personas con propiedades.
            </p>

            {/* Contact */}
            <div className="space-y-3">
              <a href="tel:+5403413507070" className="flex items-center gap-3 text-white/50 hover:text-[#c9973a] text-sm transition-colors group">
                <div className="w-8 h-8 bg-white/5 group-hover:bg-[#c9973a]/20 rounded-lg flex items-center justify-center transition-colors">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
                  </svg>
                </div>
                0341 350-7070
              </a>
              <a href="https://wa.me/5493413507070" className="flex items-center gap-3 text-white/50 hover:text-[#c9973a] text-sm transition-colors group">
                <div className="w-8 h-8 bg-white/5 group-hover:bg-[#c9973a]/20 rounded-lg flex items-center justify-center transition-colors">
                  <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                  </svg>
                </div>
                WhatsApp
              </a>
              <p className="flex items-center gap-3 text-white/40 text-sm">
                <div className="w-8 h-8 bg-white/5 rounded-lg flex items-center justify-center">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
                  </svg>
                </div>
                Brown 2063, Piso 3 y 4 — Rosario
              </p>
            </div>

            {/* Socials */}
            <div className="flex gap-3 mt-6">
              {["IG", "FB", "TK", "YT"].map((s) => (
                <a
                  key={s}
                  href="#"
                  className="w-9 h-9 bg-white/5 hover:bg-[#c9973a] rounded-lg flex items-center justify-center text-white/40 hover:text-white text-xs font-bold transition-all duration-200"
                >
                  {s}
                </a>
              ))}
            </div>
          </div>

          {/* Propiedades */}
          <div>
            <h4 className="text-white font-bold text-sm tracking-wider uppercase mb-5">Propiedades</h4>
            <ul className="space-y-3">
              {propLinks.map((l) => (
                <li key={l}>
                  <a href="#" className="text-white/40 hover:text-[#c9973a] text-sm transition-colors">{l}</a>
                </li>
              ))}
            </ul>
          </div>

          {/* Barrios */}
          <div>
            <h4 className="text-white font-bold text-sm tracking-wider uppercase mb-5">Barrios</h4>
            <ul className="space-y-3">
              {barriosLinks.map((l) => (
                <li key={l}>
                  <a href="#" className="text-white/40 hover:text-[#c9973a] text-sm transition-colors">{l}</a>
                </li>
              ))}
            </ul>
          </div>

          {/* Servicios */}
          <div>
            <h4 className="text-white font-bold text-sm tracking-wider uppercase mb-5">Servicios</h4>
            <ul className="space-y-3">
              {serviciosLinks.map((l) => (
                <li key={l}>
                  <a href="#" className="text-white/40 hover:text-[#c9973a] text-sm transition-colors">{l}</a>
                </li>
              ))}
            </ul>

            {/* Horarios */}
            <div className="mt-8 p-4 bg-white/5 rounded-xl">
              <p className="text-white/60 text-xs font-bold uppercase tracking-wider mb-2">Horario de atención</p>
              <p className="text-white/40 text-xs">Lun – Vie: 9:00 a 18:00</p>
              <p className="text-white/40 text-xs">Sáb: 9:00 a 13:00</p>
            </div>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-white/25 text-xs">
            © 2025 Vanzini Propiedades S.R.L. · COCIR Matrícula 0042 · Todos los derechos reservados.
          </p>
          <div className="flex gap-6">
            {["Privacidad", "Términos", "Cookies"].map((l) => (
              <a key={l} href="#" className="text-white/25 hover:text-white/60 text-xs transition-colors">{l}</a>
            ))}
          </div>
        </div>
      </div>
    </footer>
  );
}
