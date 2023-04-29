import { Button as ButtonBox } from "@chakra-ui/button";
import { Box } from "@chakra-ui/react";
import React from "react";
import { useNavigate } from "react-router-dom";

export default function Button({
  children,
  onClick = () => {},
  isLoading = false,
  link = false,
  isSubmit = false,
  size = "md",
  disabled = false,
  full = false,
  background = "blue.blue100",
  color = "#fff",
  border,
  w = "100%",
  leftIcon,
  rightIcon,
  href,
  mt,
  mb,
  mx,
  my,
  px = "85px",
  loadingText = "Please wait . . .",
  py = "8px",
  pt,
  pb,
  className,
  rounded,
  fontWeight,
  _hover,
  _active,
}) {
  const history = useNavigate();

  return (
    <ButtonBox
      fontSize={size === "xs" ? "xs" : size === "sm" ? "sm" : "16px"}
      fontWeight={fontWeight || "600"}
      color={color}
      bg={background}
      border={border}
      textTransform={"capitalize"}
      transition="0.5s"
      _hover={
        _hover || {
          // bg: "blue.blue400",
          color: "black",
          bg: "transparent",
          border: "1px solid #000",
        }
      }
      _active={
        _active || {
          bg: "blue.blue400",
          border: "1px solid #000",
          color: "black",
        }
      }
      rounded={rounded || "4px"}
      size={size}
      as="button"
      onClick={() => {
        link ? history(link) : onClick();
      }}
      isLoading={isLoading}
      loadingText={loadingText}
      type={isSubmit ? "submit" : "button"}
      disabled={isLoading || disabled}
      w={w}
      px={px}
      py={py}
      pt={pt || "0px"}
      pb={pb || "0px"}
      leftIcon={leftIcon}
      rightIcon={rightIcon}
      mt={mt}
      mb={mb}
      mx={mx || "0px"}
      my={my || "0px"}
      className={className || ""}
    >
      <Box as="a" href={href}>
        {children}
      </Box>
    </ButtonBox>
  );
}
