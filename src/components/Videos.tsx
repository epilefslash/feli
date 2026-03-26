const videos = [
  {
    title: "Wafles en vivo — Distrito Siete",
    thumbnail: "/images/video-1.jpg",
    url: "#",
  },
  {
    title: "Sesión en estudio",
    thumbnail: "/images/video-2.jpg",
    url: "#",
  },
];

export default function Videos() {
  return (
    <section id="videos" className="py-24 sm:py-32 px-6 bg-surface">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-sm font-medium tracking-[0.3em] uppercase text-accent mb-2">
          Visual
        </h2>
        <h3 className="text-4xl sm:text-5xl font-bold tracking-tight text-cream mb-16">
          Videos
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {videos.map((video, i) => (
            <a
              key={i}
              href={video.url}
              target="_blank"
              rel="noopener noreferrer"
              className="group block"
            >
              <div className="relative aspect-video overflow-hidden bg-surface-light">
                <div
                  className="w-full h-full bg-cover bg-center transform group-hover:scale-105 transition-transform duration-700"
                  style={{ backgroundImage: `url('${video.thumbnail}')` }}
                />
                <div className="absolute inset-0 bg-dark/30 group-hover:bg-dark/10 transition-colors duration-500" />
                {/* Play button */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="w-20 h-20 rounded-full border-2 border-cream/60 group-hover:border-accent group-hover:scale-110 flex items-center justify-center transition-all duration-300">
                    <svg
                      width="28"
                      height="28"
                      viewBox="0 0 24 24"
                      fill="currentColor"
                      className="text-cream group-hover:text-accent ml-1 transition-colors"
                    >
                      <polygon points="5,3 19,12 5,21" />
                    </svg>
                  </div>
                </div>
              </div>
              <h4 className="mt-4 text-lg font-semibold text-cream group-hover:text-accent transition-colors">
                {video.title}
              </h4>
            </a>
          ))}
        </div>

        {/* Photo gallery row */}
        <div className="mt-20">
          <h4 className="text-sm font-medium tracking-[0.3em] uppercase text-muted mb-8">
            Galería
          </h4>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {[1, 2, 3, 4].map((n) => (
              <div
                key={n}
                className="aspect-square bg-surface-light bg-cover bg-center hover:opacity-80 transition-opacity duration-300"
                style={{ backgroundImage: `url('/images/gallery-${n}.jpg')` }}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
