import React from "react";
import NavBar from "../../Components/NavBar";
import Footer from "../../Components/Footer";
import { Outlet } from "react-router-dom";

const LandingPageLayout = () => {
  return (
    <div>
      <NavBar />
      <Outlet />
      <Footer />
    </div>
  );
};

export default LandingPageLayout;
