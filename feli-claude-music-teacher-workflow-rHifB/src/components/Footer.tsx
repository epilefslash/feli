export default function Footer() {
  return (
    <footer className="py-8 px-6 border-t border-white/5">
      <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <span className="text-sm text-muted">
          &copy; {new Date().getFullYear()} Wafles. Todos los derechos
          reservados.
        </span>
        <a
          href="#"
          className="text-xs text-muted/50 hover:text-muted transition-colors"
        >
          Volver arriba
        </a>
      </div>
    </footer>
  );
}
