import { Box, Flex, Image, Stack, Text } from '@chakra-ui/react'
import React from 'react'
import Header from '../../Components/Header'
import Label from '../../Components/Label'
import Input from '../../Components/Input'
import Button from '../../Components/Button'

export default function SignUp() {
  return (
   <Flex  minH={"100vh"}>
        <Box w="35%" px="16px" bg={"blue.blue600"}>
            <Image src='/image/logo.png'/>
            <Image src='/image/authImg.png'/>
        </Box>
        <Box w="65%" px="10%" pb="10px">
            <Header text={"Welcome to NextPixie!"} mt="65px"/>
            <Text color={"#808080"} fontWeight={"500"} mt="14px" fontSize={"16px"}
             textAlign={"center"}>Please fill in your details to get started.</Text>


             <Stack mt="32px" spacing={"32px"}>
                <Box>
                    <Label text={"full name"}/>
                    <Input placeholder='Enter full name' type='text' onChange={""}/>
                </Box>
                <Box>
                    <Label text={"business name"}/>
                    <Input placeholder='Enter business name' type='text' onChange={""}/>
                </Box>
                <Box>
                    <Label text={"email address"}/>
                    <Input placeholder='Enter email address' type='email' onChange={""}/>
                </Box>
                <Box>
                    <Label text={"password"}/>
                    <Input placeholder='Enter password' type='passwordx' onChange={""}/>
                </Box>
             </Stack>

             <Button mt={"32px"}>sign up</Button>
        </Box>
   </Flex>
  )
}
