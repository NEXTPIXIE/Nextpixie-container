import React from "react";
import NavBar from "../../Components/NavBar";
import Footer from "../../Components/Footer";

const LandingPageLayout = ({ children }) => {
  return (
    <div>
      <NavBar />
      {children}
      <Footer />
    </div>
  );
};

export default LandingPageLayout;
