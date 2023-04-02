import React from "react";
import { Box, HStack, Image, Stack, Text } from "@chakra-ui/react";
import { BiLogOut } from "react-icons/bi";
import { Link, useLocation } from "react-router-dom";
import { NavList } from "./NavList";

export default function SideBar() {
  const location = useLocation();

  const List = NavList(location);

  const Logout = () => {};

  return (
    <Box ml="32px" pb="10px" bgColor={"transparent"} w="250px" mr="-10px">
      <Image ml="-15px" src="/image/logo-white.png" w="" />
      <Text
        fontFamily="body"
        fontSize={"12px"}
        fontWeight={"600"}
        color="gray.gray500"
        ml="10px"
        textTransform={"uppercase"}
      >
        Main menu
      </Text>
      <Stack spacing={"18px"} mt="32px">
        {List?.filter(
          (item) => item.display === true && item.type === "mainMenu"
        ).map((item, i) => (
          <Link to={item.link}>
            <HStack
              bgColor={item.active ? "gray.gray100" : "transparent"}
              borderLeftRadius="8px"
              py={"8px"}
              px="8px"
              fontFamily="body"
              fontSize={"16px"}
              fontWeight={"600"}
              color={item.active ? "black" : "gray.gray500"}
              _hover={{
                bgColor: "gray.gray100",
                borderLeftRadius: "8px",
                color: "black",
              }}
              key={i}
              cursor="pointer"
            >
              <Box fontSize={"20px"} pos="relative" top="-1px">
                {item.icon}
              </Box>
              <Text textTransform={"capitalize"}>{item.name}</Text>
            </HStack>
          </Link>
        ))}
      </Stack>
      <Stack mt="18px" spacing={"18px"}>
        <Text
          fontFamily="body"
          fontSize={"12px"}
          fontWeight={"600"}
          color="gray.gray500"
          ml="10px"
          textTransform={"uppercase"}
        >
          others
        </Text>
        {List?.filter(
          (item) => item.display === true && item.type === "others"
        ).map((item, i) => (
          <Link to={item.link}>
            <HStack
              bgColor={item.active ? "gray.gray100" : "transparent"}
              borderLeftRadius="8px"
              py={"8px"}
              px="8px"
              fontFamily="body"
              fontSize={"16px"}
              fontWeight={"600"}
              color={item.active ? "black" : "gray.gray500"}
              _hover={{
                bgColor: "gray.gray100",
                borderLeftRadius: "8px",
                color: "black",
              }}
              key={i}
              cursor="pointer"
            >
              <Box fontSize={"20px"} pos="relative" top="-1px">
                {item.icon}
              </Box>
              <Text textTransform={"capitalize"}>{item.name}</Text>
            </HStack>
          </Link>
        ))}

        <HStack
          onClick={Logout}
          bgColor={"transparent"}
          padding={"8px"}
          fontFamily="body"
          fontSize={"16px"}
          fontWeight={"600"}
          color={"gray.gray500"}
          _hover={{
            bgColor: "gray.gray100",
            borderLeftRadius: "8px",
            color: "black",
          }}
          cursor="pointer"
        >
          <Box fontSize={"20px"} pos="relative" top="-1px">
            <BiLogOut />
          </Box>
          <Text textTransform={"capitalize"}>Sign Out</Text>
        </HStack>
      </Stack>

      <Box
        bgColor="blue.blue200"
        rounded="8px"
        py="24px"
        px="30px"
        mr="32px"
        mt="60px"
      >
        <Text
          fontSize={"14px"}
          textAlign="center"
          fontWeight={"600"}
          color="white"
        >
          Upgrade to Pro
        </Text>
        <Text
          fontSize={"12px"}
          textAlign="center"
          mt="8px"
          fontWeight={"400"}
          color="white"
        >
          Access all of our features with no hassle.
        </Text>

        <Box
          cursor={"pointer"}
          mt="16px"
          fontSize={"12px"}
          color="black"
          fontWeight={"600"}
          bgColor="gray.gray400"
          rounded={"4px"}
          textAlign="center"
          py={"8px"}
          px="24px"
        >
          Coming soon!
        </Box>
      </Box>
    </Box>
  );
}
