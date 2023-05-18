import React from "react";
import { useNavigate } from "react-router-dom";
import Button from "../../Components/Button";
import WeddingPhoto from "../../Assets/Images/Home/wedding-photo.png";
import PortraitPhoto from "../../Assets/Images/Home/portrait-photo.png";
import PortraitPhoto2 from "../../Assets/Images/Home/portrait-photo-2.png";
import FamilyPhoto from "../../Assets/Images/Home/family-photo.png";
import NaturePhoto from "../../Assets/Images/Home/nature-photo.png";
import ArchitecturePhoto from "../../Assets/Images/Home/architecture-photo.png";

const Examples = () => {
  const navigate = useNavigate();
  const data = [
    {
      id: 1,
      title: "Ella & Daniel’s Shoot",
      category: "Wedding",
      image: WeddingPhoto,
    },
    {
      id: 2,
      title: "Zaira’s Shoot",
      category: "Portrait",
      image: PortraitPhoto,
      // grid: "row-span-1",
    },
    {
      id: 3,
      title: "Sanni Family Shoot",
      category: "Family Shoot",
      image: FamilyPhoto,
    },
    {
      id: 4,
      title: "Sunsets",
      category: "Nature",
      image: NaturePhoto,
    },
    {
      id: 5,
      title: "Mike Oyewole",
      category: "Portrait",
      image: PortraitPhoto2,
      grid: "row-span-1",
    },
    {
      id: 6,
      title: "Parkview Home",
      category: "Architecture",
      image: ArchitecturePhoto,
    },
  ];

  return (
    <div className=" w-full flex items-center flex-col gap-4 p-12 mt-8 px-16">
      <h1 className=" text-Accent-1 text-[1.6rem] font-bold">
        Share your masterpiece today!
      </h1>
      <main className="grid grid-cols-3 gap-8 my-8">
        {data.map((item) => (
          <div
            className={`w-full rounded-lg flex flex-col items-center gap-4 h-fit ${
              item.grid || ""
            }`}
          >
            <figure className="w-full">
              <img
                className="w-full h-full object-cover"
                src={item.image}
                alt={item.title}
              />
            </figure>
            <div className="w-full flex flex-col items-center gap-[0.2rem]">
              <h4 className="text-base font-medium">{item.title}</h4>
              <p className="text-xs">{item.category}</p>
            </div>
          </div>
        ))}
      </main>
      <Button
        py="1px"
        px="40px"
        onClick={() => {
          navigate("/examples");
        }}
        w="fit-content"
      >
        See All Examples
      </Button>
    </div>
  );
};

export default Examples;
