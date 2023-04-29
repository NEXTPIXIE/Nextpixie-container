import React from "react";
import Seo from "../../Utils/Seo";
import Intro from "./Intro";

export default function Home() {
  return (
    <>
      <Seo title="Home" description="HomePage" />
      <div>
        <Intro />
      </div>
    </>
  );
}
