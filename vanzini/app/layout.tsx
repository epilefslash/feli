import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Vanzini Propiedades | Rosario, Argentina",
  description: "Más de 60 años encontrando el hogar ideal. Venta, alquiler e inversión inmobiliaria en Rosario.",
  keywords: "inmobiliaria Rosario, departamentos en venta Rosario, alquiler Rosario, propiedades Rosario",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className="h-full scroll-smooth">
      <body className="min-h-full flex flex-col antialiased">{children}</body>
    </html>
  );
}
