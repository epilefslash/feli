import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import StatsBar from "@/components/StatsBar";
import FeaturedProperties from "@/components/FeaturedProperties";
import NeighborhoodGuides from "@/components/NeighborhoodGuides";
import Services from "@/components/Services";
import MortgageCalculator from "@/components/MortgageCalculator";
import Testimonials from "@/components/Testimonials";
import Team from "@/components/Team";
import PropertyAlerts from "@/components/PropertyAlerts";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <Hero />
        <StatsBar />
        <FeaturedProperties />
        <NeighborhoodGuides />
        <Services />
        <MortgageCalculator />
        <Testimonials />
        <Team />
        <PropertyAlerts />
      </main>
      <Footer />
    </>
  );
}
