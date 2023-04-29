import React from "react";
import Seo from "../../Utils/Seo";
import Intro from "./Intro";
import Examples from "./Examples";

export default function Home() {
  return (
    <>
      <Seo title="Home" description="HomePage" />
      <div>
        <Intro />
        <Examples />
      </div>
    </>
  );
}
