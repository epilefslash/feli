"use client";

const releases = [
  {
    title: "Último Single",
    year: "2025",
    type: "Single",
    cover: "/images/release-1.jpg",
    spotifyUrl: "#",
  },
  {
    title: "EP Debut",
    year: "2024",
    type: "EP",
    cover: "/images/release-2.jpg",
    spotifyUrl: "#",
  },
  {
    title: "Demo",
    year: "2023",
    type: "Demo",
    cover: "/images/release-3.jpg",
    spotifyUrl: "#",
  },
];

export default function Music() {
  return (
    <section id="musica" className="py-24 sm:py-32 px-6">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-sm font-medium tracking-[0.3em] uppercase text-accent mb-2">
          Releases
        </h2>
        <h3 className="text-4xl sm:text-5xl font-bold tracking-tight text-cream mb-16">
          Música
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {releases.map((release, i) => (
            <a
              key={i}
              href={release.spotifyUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="group block"
            >
              <div className="relative aspect-square overflow-hidden bg-surface mb-4">
                <div className="absolute inset-0 bg-accent/0 group-hover:bg-accent/10 transition-colors duration-500 z-10" />
                <div
                  className="w-full h-full bg-surface-light bg-cover bg-center transform group-hover:scale-105 transition-transform duration-700"
                  style={{ backgroundImage: `url('${release.cover}')` }}
                />
                {/* Play icon overlay */}
                <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-20">
                  <div className="w-16 h-16 rounded-full bg-accent/90 flex items-center justify-center">
                    <svg
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="currentColor"
                      className="text-dark ml-1"
                    >
                      <polygon points="5,3 19,12 5,21" />
                    </svg>
                  </div>
                </div>
              </div>
              <div className="flex items-baseline justify-between">
                <div>
                  <h4 className="text-lg font-semibold text-cream group-hover:text-accent transition-colors">
                    {release.title}
                  </h4>
                  <p className="text-sm text-muted">{release.type}</p>
                </div>
                <span className="text-sm text-muted font-mono">
                  {release.year}
                </span>
              </div>
            </a>
          ))}
        </div>

        {/* Streaming platforms */}
        <div className="mt-16 pt-12 border-t border-white/5">
          <p className="text-sm text-muted uppercase tracking-widest mb-6 text-center">
            Escuchanos en
          </p>
          <div className="flex flex-wrap items-center justify-center gap-8">
            {["Spotify", "Apple Music", "YouTube Music", "SoundCloud"].map(
              (platform) => (
                <a
                  key={platform}
                  href="#"
                  className="text-muted hover:text-cream transition-colors duration-300 text-sm font-medium tracking-wide"
                >
                  {platform}
                </a>
              )
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
