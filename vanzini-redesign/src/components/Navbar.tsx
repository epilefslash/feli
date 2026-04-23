"use client";
import { useState, useEffect } from "react";
import Link from "next/link";

const links = [
  { label: "Propiedades", href: "/propiedades" },
  { label: "Barrios", href: "/barrios" },
  { label: "Tasaciones", href: "/tasaciones" },
  { label: "Nosotros", href: "/nosotros" },
  { label: "Contacto", href: "/contacto" },
];

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 60);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`fixed top-0 inset-x-0 z-50 transition-all duration-500 ${
        scrolled
          ? "bg-[#0d1b3e]/96 backdrop-blur-xl shadow-2xl py-3"
          : "bg-transparent py-5"
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-3 group">
          <div className="w-9 h-9 bg-[#c9973a] rounded-sm flex items-center justify-center">
            <span className="text-white font-black text-sm tracking-tighter">V</span>
          </div>
          <span className="text-white font-bold text-xl tracking-widest uppercase">
            Vanzini
          </span>
        </Link>

        {/* Desktop nav */}
        <nav className="hidden lg:flex items-center gap-8">
          {links.map(({ label, href }) => (
            <Link
              key={label}
              href={href}
              className="text-white/70 hover:text-[#c9973a] text-sm font-medium tracking-wide transition-colors duration-200 relative group"
            >
              {label}
              <span className="absolute -bottom-1 left-0 w-0 h-px bg-[#c9973a] group-hover:w-full transition-all duration-300" />
            </Link>
          ))}
        </nav>

        {/* Right side */}
        <div className="hidden lg:flex items-center gap-5">
          <a
            href="tel:+5403413507070"
            className="flex items-center gap-2 text-white/60 hover:text-white text-sm transition-colors"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
                d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
            </svg>
            0341 350-7070
          </a>
          <Link
            href="/contacto"
            className="bg-[#c9973a] hover:bg-[#e8b554] text-white text-sm font-bold px-5 py-2.5 tracking-wider uppercase transition-colors duration-200"
          >
            Publicar propiedad
          </Link>
        </div>

        {/* Mobile toggle */}
        <button onClick={() => setOpen(!open)} className="lg:hidden text-white p-2">
          {open ? (
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          ) : (
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          )}
        </button>
      </div>

      {/* Mobile menu */}
      {open && (
        <div className="lg:hidden bg-[#0d1b3e] border-t border-white/10 px-6 py-6 flex flex-col gap-5">
          {links.map(({ label, href }) => (
            <Link key={label} href={href} className="text-white/80 text-base font-medium" onClick={() => setOpen(false)}>
              {label}
            </Link>
          ))}
          <Link href="/contacto" className="bg-[#c9973a] text-white text-sm font-bold px-5 py-3 text-center tracking-wider uppercase mt-2">
            Publicar propiedad
          </Link>
        </div>
      )}
    </header>
  );
}
