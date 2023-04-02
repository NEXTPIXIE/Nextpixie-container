import React from "react";
import Logo from "./Logo";
import { NavLink } from "react-router-dom";
import Button from "./Button";

export default function NavBar() {
  const NavLi = [
    {
      id: 1,
      name: "Gallery",
      link: "/",
      active: true,
    },
    {
      id: 2,
      name: "Features",
      link: "/features",
      active: false,
    },
    {
      id: 3,
      name: "Examples",
      link: "/examples",
      active: false,
    },
  ];
  return (
    <div className=" flex justify-between">
      <Logo />

      <ul>
        {NavLi.map((item) => (
          <NavLink key={item.id} to={item.link}>
            <li>{item.name}</li>
          </NavLink>
        ))}
      </ul>

      <div>
        <Button>Login</Button>
        <Button>Sign up</Button>
      </div>
    </div>
  );
}
