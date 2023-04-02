import { AiFillPicture } from "react-icons/ai";
import { MdNotifications, MdOutlineAnalytics } from "react-icons/md";
import { RiSettings2Fill } from "react-icons/ri";
import { isActive } from "../Authentication";
export const NavList = (location) => {
  let List = [
    {
      name: "gallery",
      icon: <AiFillPicture />,
      link: "/dashboard/gallery",
      active: isActive(location, "/dashboard/gallery"),
      type: "mainMenu",
      display: true,
      smile: true,
    },

    {
      name: "analytics",
      icon: <MdOutlineAnalytics />,
      link: "/dashboard/analytics",
      active: isActive(location, "/dashboard/analytics"),
      type: "mainMenu",
      display: true,
    },

    {
      name: "notifications",
      icon: <MdNotifications />,
      link: "/dashboard/notifications",
      active: isActive(location, "/dashboard/notifications"),
      type: "others",
      display: true,
    },
    {
      name: "settings",
      icon: <RiSettings2Fill />,
      link: "/dashboard/settings",
      active: isActive(location, "/dashboard/settings"),
      type: "others",
      display: true,
    },
  ];

  return List;
};
