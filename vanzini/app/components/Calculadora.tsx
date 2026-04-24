"use client";

import { useState, useMemo } from "react";

export default function Calculadora() {
  const [precio, setPrecio] = useState(100000);
  const [entrada, setEntrada] = useState(30);
  const [plazo, setPlazo] = useState(120);
  const [tasa, setTasa] = useState(8);

  const { montoFinanciar, cuota, totalPagar, interesTotal } = useMemo(() => {
    const entradaMonto = (precio * entrada) / 100;
    const montoFinanciar = precio - entradaMonto;
    const tasaMensual = tasa / 100 / 12;
    const cuota =
      tasaMensual === 0
        ? montoFinanciar / plazo
        : (montoFinanciar * tasaMensual * Math.pow(1 + tasaMensual, plazo)) /
          (Math.pow(1 + tasaMensual, plazo) - 1);
    const totalPagar = cuota * plazo;
    const interesTotal = totalPagar - montoFinanciar;
    return { montoFinanciar, cuota, totalPagar, interesTotal };
  }, [precio, entrada, plazo, tasa]);

  const fmt = (n: number) =>
    new Intl.NumberFormat("es-AR", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(n);

  return (
    <section id="calculadora" className="py-24 bg-white">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          {/* Left: text */}
          <div>
            <p className="text-sm font-semibold uppercase tracking-widest mb-3" style={{ color: "#c9973a" }}>
              Herramienta gratuita
            </p>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight mb-6" style={{ color: "#0d1b3e" }}>
              Calculá tu<br />cuota hipotecaria
            </h2>
            <p className="text-gray-500 leading-relaxed mb-8">
              Estimá cuánto pagarías por mes según el precio de la propiedad,
              el porcentaje de entrada y el plazo del crédito. Nuestros asesores
              te acompañan en cada paso del proceso.
            </p>

            <div className="flex flex-col gap-3">
              {[
                { icon: "✓", text: "Asesoramiento sin costo en primera consulta" },
                { icon: "✓", text: "Gestión de créditos con todos los bancos" },
                { icon: "✓", text: "Proceso 100% digital y transparente" },
              ].map((item) => (
                <div key={item.text} className="flex items-start gap-3">
                  <span className="font-bold mt-0.5" style={{ color: "#c9973a" }}>{item.icon}</span>
                  <span className="text-gray-600 text-sm">{item.text}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Right: calculator */}
          <div
            className="rounded-2xl p-8"
            style={{ backgroundColor: "#0d1b3e" }}
          >
            <div className="space-y-7">
              {/* Precio */}
              <div>
                <div className="flex justify-between mb-2">
                  <label className="text-sm font-semibold text-blue-200">Precio de la propiedad</label>
                  <span className="text-white font-bold">{fmt(precio)}</span>
                </div>
                <input
                  type="range"
                  min={30000}
                  max={500000}
                  step={5000}
                  value={precio}
                  onChange={(e) => setPrecio(Number(e.target.value))}
                  className="w-full h-2 rounded-full accent-[#c9973a] cursor-pointer"
                />
                <div className="flex justify-between text-xs text-blue-300 mt-1">
                  <span>USD 30.000</span>
                  <span>USD 500.000</span>
                </div>
              </div>

              {/* Entrada */}
              <div>
                <div className="flex justify-between mb-2">
                  <label className="text-sm font-semibold text-blue-200">Entrada</label>
                  <span className="text-white font-bold">{entrada}% ({fmt((precio * entrada) / 100)})</span>
                </div>
                <input
                  type="range"
                  min={10}
                  max={80}
                  step={5}
                  value={entrada}
                  onChange={(e) => setEntrada(Number(e.target.value))}
                  className="w-full h-2 rounded-full accent-[#c9973a] cursor-pointer"
                />
                <div className="flex justify-between text-xs text-blue-300 mt-1">
                  <span>10%</span>
                  <span>80%</span>
                </div>
              </div>

              {/* Plazo */}
              <div>
                <div className="flex justify-between mb-2">
                  <label className="text-sm font-semibold text-blue-200">Plazo</label>
                  <span className="text-white font-bold">{plazo} meses ({plazo / 12} años)</span>
                </div>
                <input
                  type="range"
                  min={12}
                  max={360}
                  step={12}
                  value={plazo}
                  onChange={(e) => setPlazo(Number(e.target.value))}
                  className="w-full h-2 rounded-full accent-[#c9973a] cursor-pointer"
                />
                <div className="flex justify-between text-xs text-blue-300 mt-1">
                  <span>1 año</span>
                  <span>30 años</span>
                </div>
              </div>

              {/* Tasa */}
              <div>
                <div className="flex justify-between mb-2">
                  <label className="text-sm font-semibold text-blue-200">Tasa anual (TNA)</label>
                  <span className="text-white font-bold">{tasa}%</span>
                </div>
                <input
                  type="range"
                  min={1}
                  max={25}
                  step={0.5}
                  value={tasa}
                  onChange={(e) => setTasa(Number(e.target.value))}
                  className="w-full h-2 rounded-full accent-[#c9973a] cursor-pointer"
                />
                <div className="flex justify-between text-xs text-blue-300 mt-1">
                  <span>1%</span>
                  <span>25%</span>
                </div>
              </div>

              {/* Result */}
              <div className="rounded-xl p-5 mt-2" style={{ backgroundColor: "rgba(201,151,58,0.15)", border: "1px solid rgba(201,151,58,0.3)" }}>
                <div className="text-center mb-4">
                  <div className="text-sm text-blue-200 mb-1">Cuota mensual estimada</div>
                  <div className="text-4xl font-bold" style={{ color: "#c9973a" }}>{fmt(cuota)}</div>
                </div>
                <div className="grid grid-cols-2 gap-3 text-center text-sm">
                  <div>
                    <div className="text-blue-300 text-xs">Monto a financiar</div>
                    <div className="text-white font-semibold">{fmt(montoFinanciar)}</div>
                  </div>
                  <div>
                    <div className="text-blue-300 text-xs">Total a pagar</div>
                    <div className="text-white font-semibold">{fmt(totalPagar)}</div>
                  </div>
                </div>
              </div>

              <a
                href="#contacto"
                className="block w-full text-center py-3.5 rounded-xl font-bold text-white transition-opacity hover:opacity-90"
                style={{ backgroundColor: "#c9973a" }}
              >
                Hablar con un asesor
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
