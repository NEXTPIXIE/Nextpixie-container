import React from "react";
import { useNavigate } from "react-router-dom";
import Button from "../../Components/Button";
import HomePageIntroImage from "../../Assets/Images/Home/home-page-intro-image.png";

const Intro = () => {
  const navigate = useNavigate();
  return (
    <div className="bg-CustomBlue-1 flex items-center flex-col p-10 pt-16">
      <div className="w-[66%] flex items-center flex-col gap-6">
        <h1 className=" text-center text-[2rem] font-bold flex flex-col">
          <div className=" flex items-center justify-center">
            <span className="relative">
              <p className=" relative text-center z-[1] leading-[40px]">
                Upload & Share
              </p>
              <div className=" bg-Secondary-6 w-full absolute h-[40%] bottom-0 "></div>
            </span>{" "}
            Your{" "}
          </div>{" "}
          Spectacular Visuals Easily.
        </h1>
        <p className=" text-center leading-[34px] font-medium text-base">
          NextPixie is an innovative platform designed to help professionals
          send images and videos to other people, allowing them to monitor and
          analyze the performance of what they share.
        </p>
        <Button
          py="1px"
          px="40px"
          onClick={() => {
            navigate("/sign-up");
          }}
          w="fit-content"
        >
          Get Started
        </Button>
        <figure className="mt-12 w-full">
          <img
            className="w-full h-full"
            src={HomePageIntroImage}
            alt="HomePageIntroImage"
          />
        </figure>
      </div>
    </div>
  );
};

export default Intro;
