import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Vanzini Propiedades | Inmobiliaria en Rosario desde 1965",
  description:
    "Más de 3.000 propiedades en venta y alquiler en Rosario. Tasaciones en 48hs. 60 años de experiencia en el mercado inmobiliario rosarino.",
  keywords: "inmobiliaria rosario, departamentos en venta rosario, alquiler rosario, tasaciones rosario",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
