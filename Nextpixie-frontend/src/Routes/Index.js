import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Analytics from "../Pages/Dashboard/Analytics";
import Gallery from "../Pages/Dashboard/Gallery";
import Notifications from "../Pages/Dashboard/Notifications";
import Home from "../Pages/Home";

export default function IndexRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard/gallery" element={<Gallery />} />
        <Route path="/dashboard/notifications" element={<Notifications />} />
        <Route path="/dashboard/analytics" element={<Analytics />} />
      </Routes>
    </BrowserRouter>
  );
}
