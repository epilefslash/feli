"use client";
import { useState, useMemo } from "react";

function fmt(n: number) {
  return new Intl.NumberFormat("es-AR", { maximumFractionDigits: 0 }).format(n);
}

export default function MortgageCalculator() {
  const [valor, setValor] = useState(100000);
  const [anticipo, setAnticipo] = useState(30);
  const [plazo, setPlazo] = useState(120);
  const [tasa, setTasa] = useState(8.5);

  const { prestamo, cuota, totalPagar, interesPagado } = useMemo(() => {
    const prestamo = valor * (1 - anticipo / 100);
    const r = tasa / 100 / 12;
    const cuota = prestamo * (r * Math.pow(1 + r, plazo)) / (Math.pow(1 + r, plazo) - 1);
    const totalPagar = cuota * plazo;
    const interesPagado = totalPagar - prestamo;
    return { prestamo, cuota, totalPagar, interesPagado };
  }, [valor, anticipo, plazo, tasa]);

  return (
    <section className="bg-[#0d1b3e] py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          {/* Left — copy */}
          <div>
            <p className="text-[#c9973a] text-xs font-bold tracking-[0.25em] uppercase mb-4">
              Herramienta gratuita
            </p>
            <h2 className="text-4xl md:text-5xl font-black text-white leading-tight mb-6">
              Calculá tu
              <br />
              <span className="text-[#c9973a]">cuota hipotecaria</span>
            </h2>
            <p className="text-white/50 text-lg leading-relaxed mb-8">
              Estimá cuánto pagarías por mes según el valor de la propiedad, tu anticipo y el plazo del crédito.
            </p>

            {/* Result cards */}
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-white/5 border border-white/10 rounded-2xl p-5">
                <p className="text-white/40 text-xs uppercase tracking-wider mb-1">Cuota mensual</p>
                <p className="text-[#c9973a] text-3xl font-black">USD {fmt(cuota)}</p>
              </div>
              <div className="bg-white/5 border border-white/10 rounded-2xl p-5">
                <p className="text-white/40 text-xs uppercase tracking-wider mb-1">Préstamo</p>
                <p className="text-white text-3xl font-black">USD {fmt(prestamo)}</p>
              </div>
              <div className="bg-white/5 border border-white/10 rounded-2xl p-5">
                <p className="text-white/40 text-xs uppercase tracking-wider mb-1">Total a pagar</p>
                <p className="text-white text-2xl font-bold">USD {fmt(totalPagar)}</p>
              </div>
              <div className="bg-white/5 border border-white/10 rounded-2xl p-5">
                <p className="text-white/40 text-xs uppercase tracking-wider mb-1">En intereses</p>
                <p className="text-white text-2xl font-bold">USD {fmt(interesPagado)}</p>
              </div>
            </div>

            <p className="text-white/25 text-xs mt-4">
              * Calculadora orientativa. Consultá con nuestros asesores para opciones reales de financiación.
            </p>
          </div>

          {/* Right — sliders */}
          <div className="bg-white/5 border border-white/10 rounded-3xl p-8 space-y-8">
            {/* Valor propiedad */}
            <div>
              <div className="flex justify-between mb-3">
                <label className="text-white/70 text-sm font-medium">Valor de la propiedad</label>
                <span className="text-white font-bold">USD {fmt(valor)}</span>
              </div>
              <input
                type="range"
                min={20000}
                max={500000}
                step={5000}
                value={valor}
                onChange={(e) => setValor(Number(e.target.value))}
                className="w-full accent-[#c9973a]"
              />
              <div className="flex justify-between text-white/25 text-xs mt-1">
                <span>USD 20.000</span><span>USD 500.000</span>
              </div>
            </div>

            {/* Anticipo */}
            <div>
              <div className="flex justify-between mb-3">
                <label className="text-white/70 text-sm font-medium">Anticipo</label>
                <span className="text-white font-bold">{anticipo}% — USD {fmt(valor * anticipo / 100)}</span>
              </div>
              <input
                type="range"
                min={10}
                max={80}
                step={5}
                value={anticipo}
                onChange={(e) => setAnticipo(Number(e.target.value))}
                className="w-full accent-[#c9973a]"
              />
              <div className="flex justify-between text-white/25 text-xs mt-1">
                <span>10%</span><span>80%</span>
              </div>
            </div>

            {/* Plazo */}
            <div>
              <div className="flex justify-between mb-3">
                <label className="text-white/70 text-sm font-medium">Plazo del crédito</label>
                <span className="text-white font-bold">{plazo} meses ({plazo / 12} años)</span>
              </div>
              <input
                type="range"
                min={12}
                max={360}
                step={12}
                value={plazo}
                onChange={(e) => setPlazo(Number(e.target.value))}
                className="w-full accent-[#c9973a]"
              />
              <div className="flex justify-between text-white/25 text-xs mt-1">
                <span>1 año</span><span>30 años</span>
              </div>
            </div>

            {/* Tasa */}
            <div>
              <div className="flex justify-between mb-3">
                <label className="text-white/70 text-sm font-medium">Tasa anual</label>
                <span className="text-white font-bold">{tasa}%</span>
              </div>
              <input
                type="range"
                min={1}
                max={25}
                step={0.5}
                value={tasa}
                onChange={(e) => setTasa(Number(e.target.value))}
                className="w-full accent-[#c9973a]"
              />
              <div className="flex justify-between text-white/25 text-xs mt-1">
                <span>1%</span><span>25%</span>
              </div>
            </div>

            <button className="w-full bg-[#c9973a] hover:bg-[#e8b554] text-white font-bold py-4 rounded-xl tracking-wide transition-colors">
              Hablar con un asesor →
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}
