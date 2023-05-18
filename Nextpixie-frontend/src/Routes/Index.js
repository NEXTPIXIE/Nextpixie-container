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
import SignUp from "../Pages/AuthPages/SignUp";
import SignIn from "../Pages/AuthPages/signIn";
import EmailVerification from "../Pages/AuthPages/EmailVerification";

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
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/email-verification" element={<EmailVerification />} />
      </Routes>
    </BrowserRouter>
  );
}
