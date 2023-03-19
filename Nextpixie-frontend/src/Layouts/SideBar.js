import { Box, HStack, Image, Stack, Text } from '@chakra-ui/react'
import React, { useState } from 'react'
import { useEffect } from 'react'
import { AiOutlineCluster, AiOutlineCompass, AiOutlineFundProjectionScreen, AiOutlineHome, AiOutlineLogout, AiOutlineProject } from "react-icons/ai"
import { BiLogOut } from "react-icons/bi"
import { Link,useLocation, useNavigate } from 'react-router-dom'
import { NavList } from './NavList'



export default function SideBar() {

    const location = useLocation();

    const List = NavList(location);

   
    const Logout = ()=>{

    }

    

    return (

        <Box ml="32px" pb="10px"   bgColor={"transparent"} w='250px' mr="-10px"   >
                <Image ml="-15px" src='/image/logo-white.png' w=""/>
            <Text fontFamily="body" fontSize={"12px"} fontWeight={"600"} color="gray.gray500" ml="10px" textTransform={"uppercase"}>Main menu</Text>
            <Stack spacing={"18px"}  mt="32px">

                {
                    List?.filter(item => item.display === true && item.type === "mainMenu")
                    .map((item, i) => (
                        <Link to={item.link}>
                        <HStack  bgColor={item.active ? "gray.gray100": "transparent" } borderLeftRadius="8px" py={"8px"} px="8px" fontFamily="body" fontSize={"16px"} fontWeight={"600"} color={item.active ? "black": "gray.gray500" } _hover={{ bgColor: "gray.gray100", borderLeftRadius: "8px", color: "black"}} key={i} cursor="pointer">
                            <Box  fontSize={"20px"} pos="relative" top="-1px">{item.icon}</Box>
                            <Text textTransform={"capitalize"}>{item.name}</Text>
                        </HStack>
                        </Link>
                    ))
                }

                
          

            </Stack>
            <Stack mt="18px" spacing={"18px"}>
            <Text fontFamily="body" fontSize={"12px"} fontWeight={"600"} color="gray.gray500" ml="10px" textTransform={"uppercase"}>others</Text>
            {
                    List?.filter(item => item.display === true && item.type === "others")
                    .map((item, i) => (
                        <Link to={item.link}>
                        <HStack  bgColor={item.active ? "gray.gray100": "transparent" } borderLeftRadius="8px" py={"8px"} px="8px" fontFamily="body" fontSize={"16px"} fontWeight={"600"} color={item.active ? "black": "gray.gray500" } _hover={{ bgColor: "gray.gray100", borderLeftRadius: "8px", color: "black"}} key={i} cursor="pointer">
                            <Box  fontSize={"20px"} pos="relative" top="-1px">{item.icon}</Box>
                            <Text textTransform={"capitalize"}>{item.name}</Text>
                        </HStack>
                        </Link>
                    ))
                }

                <HStack onClick={Logout} bgColor={"transparent" } padding={"8px"} fontFamily="body" fontSize={"16px"} fontWeight={"600"} color={ "gray.gray500" } _hover={{ bgColor: "gray.gray100", borderLeftRadius: "8px", color: "black"}}  cursor="pointer">
                <Box  fontSize={"20px"} pos="relative" top="-1px"><BiLogOut/></Box>
                <Text textTransform={"capitalize"} >Sign Out</Text>
               </HStack>

            </Stack>
               
              



            
        </Box>
    )
}
