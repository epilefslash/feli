"use client";

import { useState, useEffect } from "react";

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const links = [
    { label: "Propiedades", href: "#propiedades" },
    { label: "Barrios", href: "#barrios" },
    { label: "Calculadora", href: "#calculadora" },
    { label: "Nosotros", href: "#nosotros" },
    { label: "Contacto", href: "#contacto" },
  ];

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-white shadow-md py-3" : "bg-transparent py-5"
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
        {/* Logo */}
        <a href="#" className="flex items-center gap-2">
          <span
            className="text-2xl font-bold tracking-tight"
            style={{ color: scrolled ? "#0d1b3e" : "white" }}
          >
            VANZINI
          </span>
          <span
            className="text-xs font-medium tracking-widest uppercase mt-1"
            style={{ color: "#c9973a" }}
          >
            Propiedades
          </span>
        </a>

        {/* Desktop links */}
        <div className="hidden md:flex items-center gap-8">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              className={`text-sm font-medium transition-colors hover:text-[#c9973a] ${
                scrolled ? "text-[#0d1b3e]" : "text-white"
              }`}
            >
              {l.label}
            </a>
          ))}
          <a
            href="#contacto"
            className="ml-2 px-5 py-2 rounded text-sm font-semibold text-white transition-colors"
            style={{ backgroundColor: "#c9973a" }}
          >
            Consultar ahora
          </a>
        </div>

        {/* Mobile hamburger */}
        <button
          className="md:hidden"
          style={{ color: scrolled ? "#0d1b3e" : "white" }}
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Menú"
        >
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {menuOpen ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div className="md:hidden bg-white shadow-lg px-6 py-4 flex flex-col gap-4">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              className="text-[#0d1b3e] font-medium text-base"
              onClick={() => setMenuOpen(false)}
            >
              {l.label}
            </a>
          ))}
          <a
            href="#contacto"
            className="text-center px-5 py-2 rounded text-sm font-semibold text-white"
            style={{ backgroundColor: "#c9973a" }}
            onClick={() => setMenuOpen(false)}
          >
            Consultar ahora
          </a>
        </div>
      )}
    </nav>
  );
}
