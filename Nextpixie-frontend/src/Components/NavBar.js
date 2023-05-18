import React from "react";
import Logo from "./Logo";
import { NavLink, Link } from "react-router-dom";
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
    <div className=" flex justify-between shadow-NavBarboxShadow p-3 px-8 relative z-10">
      <Link to={"/"}>
        <Logo />
      </Link>

      <ul className="flex items-center gap-8">
        {NavLi.map((item) => (
          <NavLink
            key={item.id}
            className={({ isActive }) => {
              return isActive ? " text-Accent-1" : " text-Accent-5";
            }}
            to={item.link}
          >
            <li>{item.name}</li>
          </NavLink>
        ))}
      </ul>

      <div className="flex items-center gap-6">
        <Link to={"/login"} className="font-semibold">
          Log In
        </Link>
        <Link to={"/sign-up"}>
          <Button py="1px" px="26px" className={" "}>
            Sign up
          </Button>
        </Link>
      </div>
    </div>
  );
}
