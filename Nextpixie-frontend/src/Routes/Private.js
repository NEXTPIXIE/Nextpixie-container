import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import { isAuthenticated } from "../Authentication";

export default function PrivateRoutes() {
  let auth = { token: isAuthenticated() };

  return auth.token ? <Outlet /> : <Navigate to="/" />;
}
