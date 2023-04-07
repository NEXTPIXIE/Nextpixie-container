import {
  Box,
  FormControl,
  FormHelperText,
  FormLabel,
  Input as InputBox,
  InputGroup,
  InputLeftElement,
  InputRightElement,
} from "@chakra-ui/react";
import React, { useState } from "react";
import { useEffect } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";

export default function Input({
  id = "",
  val = false,
  label = "",
  bColor = "#fff",
  isRequired = false,
  type = "email",
  readOnly = false,
  helper = null,
  onChange = null,
  isDisabled = false,
  size = "lg",
  placeholder = `Enter ${label.toLowerCase()}`,
  pl = 0,
  rightIcon = null,
  w = "100%",
  borderColor = "blue.blue400",
  labelBg = "blue.blue350",
  leftIcon,
  iconColor = "#fff",
  ...rest
}) {
  const [active, setActive] = useState(rest.value);
  // const [value, setValue] = useState(val);

  const [inputType, setInputType] = useState(type);

  const switchEye = ()=>{
    
      if (inputType === "password") {
        setInputType("text");
      } else {
        setInputType("password");
      }
    }
  
useEffect(() => {
  switchEye()
}, [])
  return (
    <FormControl
      id={id}
      isReadOnly={readOnly}
      isDisabled={isDisabled}
      isRequired={isRequired}
      pos="relative"
    >
      <FormLabel
        pos="absolute"
        transform={`translateY(${
          active || val ? "-19px" : "7px"
        }) translateX(30px)`}
        bottom={"3"}
        zIndex="10"
        fontSize={active ? "xs" : "12px"}
        fontWeight="400"
        color={"#00000"}
        bg={active ? labelBg : "transparent"}
        px="0px"
      >
        {/* {label} */}
      </FormLabel>

      <InputGroup>
        <InputGroup>
          <InputLeftElement
            pointerEvents="none"
            children={
              <Box
                pos={"relative"}
                color={active ? borderColor : iconColor}
                top="4.5px"
                fontSize={"20px"}
              >
                {leftIcon}
              </Box>
            }
          />
          <InputBox
            // borderColor={Colors.red}
            onChange={onChange}
            {...rest}
            placeholder={active || !label ? placeholder : ""}
            type={inputType}
            focusBorderColor={"blue.blue400"}
            _focus={{ borderColor: borderColor }}
            size={size}
            color="#00000"
            _autofill={{ bgColor: "#fff !important" }}
            fontWeight={"400"}
            fontSize="16px"
            fontFamily={"body"}
            borderColor={bColor}
            rounded="4px"
            pl={"12px !important"}
            bg="rgba(235, 245, 255, 0.42)"
         
            w={w}
            onFocus={() => setActive(true)}
            onBlur={() => {
              if (!rest.value) {
                setActive(false);
              }
            }}
            // height="56px"
          />
          {rightIcon && <InputRightElement children={rightIcon} />}
        </InputGroup>
        {type === "password" && (
          <InputRightElement
            children={
              inputType === "password" ? (
                <FaEyeSlash color="green.500" />
              ) : (
                <FaEye color="green.500" />
              )
            }
            cursor={"pointer"}
            onClick={switchEye}
          />
        )}
      </InputGroup>
      {helper && (
        <FormHelperText pos={"absolute"} p={1} m="0" fontSize={"10px"}>
          {helper}
        </FormHelperText>
      )}
    </FormControl>
  );
}
