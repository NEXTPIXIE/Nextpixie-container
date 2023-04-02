import React from "react";
import Logo from "./Logo";
import { NavLink } from "react-router-dom";

export default function NavBar() {
  const NavLi = [
    {
      id: 1,
      name: "Gallery",
      link: "/gallery",
      active: true,
    },
    {
      id: 2,
      name: "Features",
      link: "/gallery",
      active: true,
    },
    {
      id: 3,
      name: "Examples",
      link: "/gallery",
      active: true,
    },
  ];
  return (
    <div>
      <Logo />

      <ul>
        {NavLi.map((item) => (
          <NavLink key={item.id}>
            <li>{item.name}</li>
          </NavLink>
        ))}
      </ul>
    </div>
  );
}
