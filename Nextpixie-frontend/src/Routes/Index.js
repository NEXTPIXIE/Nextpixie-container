import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Analytics from "../Pages/Dashboard/Analytics";
import Gallery from "../Pages/Dashboard/Gallery";
import Notifications from "../Pages/Dashboard/Notifications";
import Home from "../Pages/Home";
import NotFound from "../Pages/NotFound";
import LandingPageLayout from "../Layouts/LandingPageLayout";
import Features from "../Pages/Features";
import Examples from "../Pages/Examples";

export default function IndexRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<LandingPageLayout />}>
          <Route path="/" index element={<Home />} />
          <Route path="/features" element={<Features />} />
          <Route path="/examples" element={<Examples />} />
        </Route>
        <Route path="/dashboard/gallery" element={<Gallery />} />
        <Route path="/dashboard/notifications" element={<Notifications />} />
        <Route path="/dashboard/analytics" element={<Analytics />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
