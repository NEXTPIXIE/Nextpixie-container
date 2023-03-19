import { Box, Stack } from '@chakra-ui/react'
import React from 'react'
import NavBar from './NavBar'
import SideBar from './SideBar'

export default function MainLayout({ children, bgColor = "blue.blue100", layoutColor = "gray.gray100", color = "black" }) {
  return (

    <Box bgColor={bgColor} minH="100vh" pt="24px">

      <Stack align={"flex-start"} pos={"relative"} direction={["column-reverse", "column-reverse", "column-reverse", "column-reverse", "row"]} >
        <Box display={["none", "none", "none", "none", "flex"]}>
          <SideBar />
        </Box>

        <Box width={'100%'}>

          <Box borderRadius="8px" mt="15px" p="20px" color={color} mr="0px" minH='86vh' width={['100%', '100%', '100%', '100%', '98.5%']} bgColor={layoutColor}>
            {children}
          </Box>


        </Box>
      </Stack>



    </Box>
  )
}
