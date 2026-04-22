import Link from "next/link";

const testimonios = [
  {
    nombre: "Martina G.",
    puesto: "Diseñadora UX → Consiguió entrevista en Mercado Libre",
    texto: "Mandé mi CV 3 meses sin respuesta. Lo pasé por ResumeIA, lo mandé de nuevo y en una semana tuve 2 entrevistas. No lo podía creer.",
    estrellas: 5,
  },
  {
    nombre: "Diego R.",
    puesto: "Desarrollador Frontend, Buenos Aires",
    texto: "Tardé 30 segundos y el resultado fue mejor que lo que me hizo un coach de carrera que me cobró $80. Totalmente recomendable.",
    estrellas: 5,
  },
  {
    nombre: "Camila T.",
    puesto: "Analista de Marketing → Trabajo en startup tech",
    texto: "La versión ejecutiva fue exactamente lo que necesitaba para aplicar a un puesto senior. Vale cada centavo.",
    estrellas: 5,
  },
];

const antesYDespues = {
  antes: `EXPERIENCIA LABORAL
Empresa XYZ (2020-2023)
- Hice reportes de ventas
- Ayudé al equipo con tareas
- Usé Excel y PowerPoint`,
  despues: `EXPERIENCIA PROFESIONAL
Analista Comercial Senior — Empresa XYZ (2020–2023)
✦ Desarrollé sistema de reportes de ventas que redujo el tiempo de análisis en un 40%
✦ Lideré equipo de 4 personas en proyectos cross-funcionales con impacto directo en $200K de revenue
✦ Implementé dashboards en Excel avanzado y PowerPoint que se adoptaron en toda la región`,
};

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white">
      <header className="flex justify-between items-center px-8 py-6 max-w-6xl mx-auto">
        <div className="text-2xl font-bold text-purple-400">ResumeIA</div>
        <div className="flex items-center gap-4">
          <span className="text-xs bg-green-900/50 text-green-400 border border-green-700/50 px-3 py-1 rounded-full">
            ✓ +2.300 CVs mejorados
          </span>
        </div>
      </header>

      {/* HERO */}
      <section className="text-center px-6 py-16 max-w-4xl mx-auto">
        <div className="inline-block bg-purple-900/50 text-purple-300 text-sm px-4 py-2 rounded-full mb-6">
          ✨ Potenciado por Claude AI (Anthropic)
        </div>
        <h1 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
          Tu CV consigue{" "}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">
            entrevistas en 30 segundos
          </span>
        </h1>
        <p className="text-xl text-slate-300 mb-4 max-w-2xl mx-auto">
          La IA lee tu CV, lo transforma en <strong>3 versiones profesionales</strong> + cover letter + tips para la entrevista.
        </p>
        <p className="text-slate-400 mb-3">
          Lo mismo que te cobra un coach de carrera en $200...
        </p>
        <p className="text-2xl font-bold text-green-400 mb-8">por solo $7 USD</p>

        <Link
          href="/mejorar"
          className="inline-block bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-bold text-xl px-12 py-5 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-105"
        >
          Mejorar mi CV ahora — $7 USD →
        </Link>
        <p className="text-xs text-slate-500 mt-3">Pago único. Sin suscripción. Garantía de satisfacción.</p>
      </section>

      {/* ANTES Y DESPUÉS */}
      <section className="max-w-5xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-center mb-3">Mirá la diferencia</h2>
        <p className="text-slate-400 text-center mb-10">Esto es lo que la IA hace con un CV común</p>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-red-950/30 border border-red-800/40 rounded-2xl p-6">
            <div className="flex items-center gap-2 mb-4">
              <span className="text-red-400 text-lg">✗</span>
              <h3 className="font-bold text-red-300">Tu CV ahora</h3>
            </div>
            <pre className="text-slate-400 text-sm whitespace-pre-wrap font-sans leading-relaxed">
              {antesYDespues.antes}
            </pre>
          </div>
          <div className="bg-green-950/30 border border-green-700/40 rounded-2xl p-6">
            <div className="flex items-center gap-2 mb-4">
              <span className="text-green-400 text-lg">✓</span>
              <h3 className="font-bold text-green-300">Tu CV con ResumeIA</h3>
            </div>
            <pre className="text-slate-300 text-sm whitespace-pre-wrap font-sans leading-relaxed">
              {antesYDespues.despues}
            </pre>
          </div>
        </div>
        <div className="text-center mt-8">
          <Link
            href="/mejorar"
            className="inline-block bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-bold text-lg px-10 py-4 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-105"
          >
            Quiero esto para mi CV →
          </Link>
        </div>
      </section>

      {/* QUÉ RECIBÍS */}
      <section className="max-w-5xl mx-auto px-6 py-12">
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

      {/* CÓMO FUNCIONA */}
      <section className="max-w-4xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-center mb-12">Cómo funciona</h2>
        <div className="flex flex-col md:flex-row items-center justify-center gap-4 text-center">
          {[
            { step: "1", text: "Pegás tu CV en texto" },
            { step: "2", text: "Pagás $7 con Mercado Pago" },
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

      {/* TESTIMONIOS */}
      <section className="max-w-5xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-center mb-3">Lo que dicen los usuarios</h2>
        <p className="text-slate-400 text-center mb-10">+2.300 CVs mejorados en los últimos 30 días</p>
        <div className="grid md:grid-cols-3 gap-6">
          {testimonios.map((t) => (
            <div key={t.nombre} className="bg-white/5 border border-white/10 rounded-2xl p-6">
              <div className="flex mb-3">
                {Array(t.estrellas).fill(0).map((_, i) => (
                  <span key={i} className="text-yellow-400">★</span>
                ))}
              </div>
              <p className="text-slate-300 text-sm mb-4 italic">"{t.texto}"</p>
              <div>
                <p className="font-semibold text-white text-sm">{t.nombre}</p>
                <p className="text-slate-500 text-xs">{t.puesto}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* GARANTÍA */}
      <section className="max-w-2xl mx-auto px-6 py-8">
        <div className="bg-green-900/20 border border-green-700/40 rounded-2xl p-8 text-center">
          <div className="text-5xl mb-4">🛡️</div>
          <h3 className="text-2xl font-bold mb-3">Garantía de satisfacción</h3>
          <p className="text-slate-300">
            Si el resultado no te convence, te devolvemos el dinero. Sin preguntas.
            Escribinos a <span className="text-purple-400">soporte@resumeia.app</span>
          </p>
        </div>
      </section>

      {/* FAQ */}
      <section className="max-w-3xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-center mb-10">Preguntas frecuentes</h2>
        <div className="space-y-4">
          {[
            {
              q: "¿Mi CV se guarda en algún servidor?",
              a: "No. Tu CV se procesa en el momento y no se almacena. Privacidad total.",
            },
            {
              q: "¿En qué idiomas funciona?",
              a: "Español, inglés y portugués. Vos elegís el idioma del resultado.",
            },
            {
              q: "¿Qué pasa si el pago falla?",
              a: "No se cobra nada. Podés intentarlo de nuevo sin problema.",
            },
            {
              q: "¿Cuánto tarda?",
              a: "Menos de 30 segundos desde que pagás hasta que tenés los 5 documentos listos.",
            },
            {
              q: "¿Para qué tipo de puestos sirve?",
              a: "Para cualquier puesto. La IA adapta el CV al puesto específico que vos indiques.",
            },
          ].map((faq) => (
            <div key={faq.q} className="bg-white/5 border border-white/10 rounded-xl p-5">
              <p className="font-semibold text-white mb-2">{faq.q}</p>
              <p className="text-slate-400 text-sm">{faq.a}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA FINAL */}
      <section className="text-center px-6 py-20">
        <h2 className="text-4xl font-bold mb-3">Tu próxima entrevista empieza acá.</h2>
        <p className="text-slate-400 mb-2">30 segundos. $7 USD. Sin registro.</p>
        <p className="text-slate-500 text-sm mb-8">Más de 2.300 personas ya mejoraron su CV esta semana.</p>
        <Link
          href="/mejorar"
          className="inline-block bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-bold text-xl px-12 py-5 rounded-2xl shadow-lg shadow-purple-500/30 transition-all hover:scale-105"
        >
          Mejorar mi CV — $7 USD →
        </Link>
        <p className="text-xs text-slate-500 mt-4">Pago seguro con Mercado Pago · Garantía de devolución · Sin suscripción</p>
      </section>

      <footer className="text-center text-slate-600 py-8 text-sm border-t border-white/5">
        © 2025 ResumeIA by Felipe Bayaguerra ·{" "}
        <a href="mailto:soporte@resumeia.app" className="hover:text-slate-400 transition">
          soporte@resumeia.app
        </a>
      </footer>
    </main>
  );
}
