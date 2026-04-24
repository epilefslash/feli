import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Listings from "./components/Listings";
import Barrios from "./components/Barrios";
import Calculadora from "./components/Calculadora";
import Team from "./components/Team";
import Testimonios from "./components/Testimonios";
import Alertas from "./components/Alertas";
import Contacto from "./components/Contacto";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <Hero />
        <Listings />
        <Barrios />
        <Calculadora />
        <Team />
        <Testimonios />
        <Alertas />
        <Contacto />
      </main>
      <Footer />
    </>
  );
}
