"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";

interface Resultados {
  cvFormal: string;
  cvCreativo: string;
  cvEjecutivo: string;
  coverLetter: string;
  tips: string;
}

function ResultadosContent() {
  const searchParams = useSearchParams();
  const [resultados, setResultados] = useState<Resultados | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [tab, setTab] = useState<"formal" | "creativo" | "ejecutivo" | "cover" | "tips">("formal");

  useEffect(() => {
    const datos = searchParams.get("datos");
    if (!datos) {
      setError("No se encontraron datos. Volvé a intentarlo.");
      setLoading(false);
      return;
    }

    async function procesar() {
      try {
        const decoded = JSON.parse(Buffer.from(datos!, "base64url").toString());
        const res = await fetch("/api/procesar-cv", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(decoded),
        });
        const data = await res.json();
        if (data.error) throw new Error(data.error);
        setResultados(data);
      } catch (e) {
        setError("Error procesando tu CV. Contactá a soporte.");
        console.error(e);
      } finally {
        setLoading(false);
      }
    }

    procesar();
  }, [searchParams]);

  function descargar(texto: string, nombre: string) {
    const blob = new Blob([texto], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${nombre}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  }

  function descargarTodo() {
    if (!resultados) return;
    const todo = `=== CV FORMAL ===\n${resultados.cvFormal}\n\n=== CV CREATIVO ===\n${resultados.cvCreativo}\n\n=== CV EJECUTIVO ===\n${resultados.cvEjecutivo}\n\n=== COVER LETTER ===\n${resultados.coverLetter}\n\n=== TIPS PARA LA ENTREVISTA ===\n${resultados.tips}`;
    descargar(todo, "ResumeIA-Pack-Completo");
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-6 animate-bounce">🤖</div>
          <h2 className="text-2xl font-bold mb-3">La IA está mejorando tu CV...</h2>
          <p className="text-slate-400">Esto tarda unos 30 segundos. ¡Ya casi está!</p>
          <div className="mt-6 flex justify-center gap-2">
            {["Analizando tu CV", "Mejorando redacción", "Generando cover letter", "Preparando tips"].map((s, i) => (
              <div key={i} className="text-xs text-purple-400 animate-pulse" style={{ animationDelay: `${i * 0.5}s` }}>
                {s}...
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="text-5xl mb-4">⚠️</div>
          <h2 className="text-2xl font-bold mb-2">Algo salió mal</h2>
          <p className="text-slate-400 mb-6">{error}</p>
          <a href="/mejorar" className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-xl">
            Volver a intentar
          </a>
        </div>
      </div>
    );
  }

  const tabs = [
    { id: "formal", label: "CV Formal", content: resultados?.cvFormal },
    { id: "creativo", label: "CV Creativo", content: resultados?.cvCreativo },
    { id: "ejecutivo", label: "CV Ejecutivo", content: resultados?.cvEjecutivo },
    { id: "cover", label: "Cover Letter", content: resultados?.coverLetter },
    { id: "tips", label: "💡 Tips", content: resultados?.tips },
  ] as const;

  const currentContent = tabs.find((t) => t.id === tab)?.content || "";

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-slate-900 text-white px-6 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-10">
          <div className="text-5xl mb-4">🎉</div>
          <h1 className="text-4xl font-extrabold mb-2">¡Tu CV está listo!</h1>
          <p className="text-slate-400">Revisá cada versión y descargá la que más te guste.</p>
        </div>

        <div className="mb-6 flex justify-center">
          <button
            onClick={descargarTodo}
            className="bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600 text-white font-bold px-8 py-3 rounded-xl shadow-lg transition-all hover:scale-105"
          >
            ⬇️ Descargar TODO el pack completo
          </button>
        </div>

        <div className="flex flex-wrap gap-2 mb-6 justify-center">
          {tabs.map((t) => (
            <button
              key={t.id}
              onClick={() => setTab(t.id)}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                tab === t.id
                  ? "bg-purple-600 text-white"
                  : "bg-white/10 text-slate-300 hover:bg-white/20"
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>

        <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-purple-300">
              {tabs.find((t) => t.id === tab)?.label}
            </h2>
            <button
              onClick={() => descargar(currentContent, `ResumeIA-${tab}`)}
              className="text-sm bg-purple-700 hover:bg-purple-600 px-4 py-2 rounded-xl transition"
            >
              ⬇️ Descargar este
            </button>
          </div>
          <pre className="text-slate-300 text-sm whitespace-pre-wrap leading-relaxed font-sans">
            {currentContent}
          </pre>
        </div>

        <div className="text-center mt-10">
          <p className="text-slate-500 text-sm mb-3">¿Te fue útil? Compartilo 👇</p>
          <a
            href={`https://twitter.com/intent/tweet?text=Mejoré mi CV con IA en 30 segundos 🔥 Probalo en resumeia.vercel.app`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm bg-sky-700 hover:bg-sky-600 px-5 py-2 rounded-xl transition"
          >
            Compartir en Twitter/X
          </a>
        </div>
      </div>
    </main>
  );
}

export default function ResultadosPage() {
  return (
    <Suspense>
      <ResultadosContent />
    </Suspense>
  );
}
