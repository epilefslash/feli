import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white">
      <header className="flex justify-between items-center px-8 py-6 max-w-6xl mx-auto">
        <div className="text-2xl font-bold text-purple-400">ResumeIA</div>
        <div className="text-sm text-slate-400">by Felipe Bayaguerra</div>
      </header>

      <section className="text-center px-6 py-20 max-w-4xl mx-auto">
        <div className="inline-block bg-purple-900/50 text-purple-300 text-sm px-4 py-2 rounded-full mb-6">
          ✨ Potenciado por Inteligencia Artificial
        </div>
        <h1 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
          Tu CV,{" "}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">
            transformado en 30 segundos
          </span>
        </h1>
        <p className="text-xl text-slate-300 mb-4 max-w-2xl mx-auto">
          Pegá tu CV y la IA lo convierte en <strong>3 versiones profesionales</strong> + cover letter + tips para la entrevista.
        </p>
        <p className="text-slate-400 mb-10">
          Lo mismo que te cobra un coach de carrera en $200... por solo{" "}
          <span className="text-green-400 font-bold text-xl">$7 USD</span>
        </p>
        <Link
          href="/mejorar"
          className="inline-block bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-bold text-lg px-10 py-4 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-105"
        >
          Mejorar mi CV ahora →
        </Link>
      </section>

      <section className="max-w-5xl mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-center mb-12">¿Qué recibís por $7?</h2>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { icon: "📄", title: "3 versiones de tu CV", desc: "Formal, creativo y ejecutivo. Uno para cada tipo de empresa." },
            { icon: "✉️", title: "Cover Letter", desc: "Carta de presentación personalizada para el puesto que buscás." },
            { icon: "💡", title: "Tips para la entrevista", desc: "Consejos específicos basados en tu perfil y experiencia." },
          ].map((item) => (
            <div key={item.title} className="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition">
              <div className="text-4xl mb-4">{item.icon}</div>
              <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
              <p className="text-slate-400">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="max-w-4xl mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-center mb-12">Cómo funciona</h2>
        <div className="flex flex-col md:flex-row items-center justify-center gap-4 text-center">
          {[
            { step: "1", text: "Pegás tu CV en texto" },
            { step: "2", text: "Pagás $7 con MP" },
            { step: "3", text: "La IA lo mejora en 30 seg" },
            { step: "4", text: "Descargás todo" },
          ].map((s, i) => (
            <div key={i} className="flex items-center gap-4">
              <div className="flex flex-col items-center">
                <div className="w-12 h-12 rounded-full bg-purple-600 flex items-center justify-center font-bold text-lg">
                  {s.step}
                </div>
                <p className="mt-2 text-sm text-slate-300 max-w-[100px]">{s.text}</p>
              </div>
              {i < 3 && <div className="text-slate-600 text-2xl hidden md:block">→</div>}
            </div>
          ))}
        </div>
      </section>

      <section className="text-center px-6 py-20">
        <h2 className="text-3xl font-bold mb-4">Empezá ahora. 30 segundos.</h2>
        <p className="text-slate-400 mb-8">Sin registro. Sin suscripción. Pago único.</p>
        <Link
          href="/mejorar"
          className="inline-block bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-bold text-lg px-10 py-4 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-105"
        >
          Mejorar mi CV — $7 USD →
        </Link>
      </section>

      <footer className="text-center text-slate-600 py-8 text-sm">
        © 2025 ResumeIA by Felipe Bayaguerra
      </footer>
    </main>
  );
}
