import React from "react";
import MainLayout from "../Layouts/DashboardLayout/Index";
import Seo from "../Utils/Seo";

export default function Home() {
  return (
    <MainLayout pageTitle="">
      <Seo title="Home" description="HomePage" />
    </MainLayout>
  );
}
