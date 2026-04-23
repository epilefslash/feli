export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer style={{ backgroundColor: "#0d1b3e" }}>
      <div className="max-w-7xl mx-auto px-6 pt-16 pb-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
          {/* Brand */}
          <div className="lg:col-span-1">
            <div className="mb-4">
              <span className="text-2xl font-bold text-white">VANZINI</span>
              <span className="block text-xs font-medium tracking-widest uppercase mt-0.5" style={{ color: "#c9973a" }}>
                Propiedades
              </span>
            </div>
            <p className="text-blue-300 text-sm leading-relaxed mb-6">
              Más de 60 años conectando personas con propiedades en Rosario. Confianza, trayectoria y resultados.
            </p>
            <div className="flex gap-3">
              {["📸", "🎵", "👥"].map((icon, i) => (
                <a
                  key={i}
                  href="#"
                  className="w-9 h-9 rounded-full flex items-center justify-center text-sm transition-colors"
                  style={{ backgroundColor: "rgba(255,255,255,0.08)" }}
                >
                  {icon}
                </a>
              ))}
            </div>
          </div>

          {/* Propiedades */}
          <div>
            <h4 className="text-white font-bold text-sm uppercase tracking-wider mb-5">Propiedades</h4>
            <ul className="space-y-3">
              {[
                "Departamentos en venta",
                "Casas en venta",
                "Locales comerciales",
                "Terrenos",
                "Alquileres",
                "Inversiones",
              ].map((link) => (
                <li key={link}>
                  <a href="#propiedades" className="text-blue-300 text-sm hover:text-[#c9973a] transition-colors">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Barrios */}
          <div>
            <h4 className="text-white font-bold text-sm uppercase tracking-wider mb-5">Barrios</h4>
            <ul className="space-y-3">
              {["Centro", "Pichincha", "Fisherton", "Alberdi", "Echesortu", "Norte"].map((link) => (
                <li key={link}>
                  <a href="#barrios" className="text-blue-300 text-sm hover:text-[#c9973a] transition-colors">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contacto */}
          <div>
            <h4 className="text-white font-bold text-sm uppercase tracking-wider mb-5">Contacto</h4>
            <ul className="space-y-4 text-sm">
              <li className="flex items-start gap-3 text-blue-300">
                <span className="mt-0.5">📍</span>
                <span>Córdoba 1234, Rosario, Santa Fe</span>
              </li>
              <li className="flex items-start gap-3 text-blue-300">
                <span>📞</span>
                <span>+54 341 XXX-XXXX</span>
              </li>
              <li className="flex items-start gap-3 text-blue-300">
                <span>📧</span>
                <span>consultas@vanzini.com.ar</span>
              </li>
              <li className="flex items-start gap-3 text-blue-300">
                <span>🕐</span>
                <div>
                  <div>Lun–Vie 9:00–18:00</div>
                  <div>Sáb 9:00–13:00</div>
                </div>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="pt-8 border-t flex flex-col md:flex-row justify-between items-center gap-4" style={{ borderColor: "rgba(255,255,255,0.1)" }}>
          <p className="text-blue-400 text-xs">
            © {year} Vanzini Propiedades. Todos los derechos reservados.
          </p>
          <div className="flex gap-6">
            {["Política de privacidad", "Términos y condiciones", "Mapa del sitio"].map((link) => (
              <a key={link} href="#" className="text-blue-400 text-xs hover:text-[#c9973a] transition-colors">
                {link}
              </a>
            ))}
          </div>
          <p className="text-blue-400 text-xs">
            Matrícula CPCR Nº 0000 — Rosario, Argentina
          </p>
        </div>
      </div>
    </footer>
  );
}
