import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Music from "@/components/Music";
import Shows from "@/components/Shows";
import About from "@/components/About";
import Videos from "@/components/Videos";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <Music />
      <Shows />
      <About />
      <Videos />
      <Contact />
      <Footer />
    </main>
  );
}
