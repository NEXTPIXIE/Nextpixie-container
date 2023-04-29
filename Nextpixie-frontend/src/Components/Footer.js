import React from "react";
import Button from "./Button";
import { Link, useNavigate } from "react-router-dom";
import Logo from "./Logo";

export default function Footer() {
  const navigate = useNavigate();
  return (
    <div className=" bg-CustomBlue-1 flex flex-col items-center gap-8 p-16 px-24">
      <div className=" flex flex-col items-center">
        <h1 className=" text-center">Become part of the NextPixie Family.</h1>
        <p className=" text-center">
          We empower working professionals to grow their personal brand by
          sharing visual content that promotes their credibility, expertise, and
          achievements.
        </p>
        <Button
          background="#20486D"
          py="1px"
          px="40px"
          onClick={() => {
            navigate("/examples");
          }}
          w="fit-content"
        >
          Get Started
        </Button>
      </div>
      <span className="w-full bg-Accent-6 h-[0.05rem] rounded-full"></span>
      <div>
        <div>
          <div>
            <Logo />
            <p>
              NextPixie is an innovative platform designed to help professionals
              send images and videos to other people, allowing them to monitor
              and analyze the performance of what they shared.
            </p>
            <div>
              <img src="" alt="Linkedin-icon" />
              <img src="" alt="twitter-icon" />
              <img src="" alt="instagram-icon" />
            </div>
          </div>
          <div>
            <span>Product</span>
            <Link>Gallery</Link>
            <Link>Features</Link>
            <Link>Examples</Link>
          </div>
          <div>
            <span>Company</span>
            <Link>About Us</Link>
            <Link>Contact</Link>
          </div>
          <div>
            <span>Resources</span>
            <Link>Tutorials</Link>
            <Link>FAQs</Link>
          </div>
          <div>
            <span>Legal</span>
            <Link>Terms of Use</Link>
            <Link>Privacy Policy</Link>
          </div>
        </div>
        <span>2023 NextPixie. All Rights Reserved.</span>
      </div>
    </div>
  );
}
