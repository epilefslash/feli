const stats = [
  { value: "60+", label: "Años de experiencia", icon: "🏆" },
  { value: "+3.000", label: "Propiedades activas", icon: "🏠" },
  { value: "+8.000", label: "Familias asesoradas", icon: "👨‍👩‍👧" },
  { value: "48hs", label: "Tasación express", icon: "⚡" },
];

export default function StatsBar() {
  return (
    <section className="bg-[#c9973a] py-0">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-2 lg:grid-cols-4">
          {stats.map(({ value, label, icon }, i) => (
            <div
              key={label}
              className={`flex flex-col items-center justify-center py-8 px-6 text-center ${
                i < stats.length - 1 ? "border-r border-white/20" : ""
              } ${i >= 2 ? "border-t border-white/20 lg:border-t-0" : ""}`}
            >
              <span className="text-2xl mb-1">{icon}</span>
              <span className="text-3xl font-black text-white tracking-tight">{value}</span>
              <span className="text-white/75 text-sm font-medium mt-1">{label}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
