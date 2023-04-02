import React from "react";
import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <div>
      Page Not Found <br /> Go to <Link to={"/"}>Gallery</Link>
    </div>
  );
};

export default NotFound;
