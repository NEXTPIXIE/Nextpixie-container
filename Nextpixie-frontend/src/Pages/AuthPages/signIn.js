import { Box, Flex, Image, Stack, Text } from '@chakra-ui/react'
import React, { useState } from 'react'
import Header from '../../Components/Header'
import Label from '../../Components/Label'
import Input from '../../Components/Input'
import Button from '../../Components/Button'
import { FcGoogle } from 'react-icons/fc';
import { useNavigate } from 'react-router-dom'

export default function SignIn() {
    const [Loading, setLoading] = useState(false);
    const [Payload, setPayload] = useState({
       
        email: "",
        password: "",
    });

    const nav = useNavigate() 




    const handlePayload = (e)=>{
        setPayload({
          ...Payload,
           [e.target.id]: e.target.value
        })
    }

    const LoginBtn = ()=>{
        setLoading(true)
        
        setTimeout(() => {
            
            setLoading(false)
        }, 3000);
    }


    return (
        <Flex minH={"100vh"} flexDir={["column-reverse","column-reverse","row-reverse","row-reverse","row-reverse"]}>
            <Box w={["100%","44.5%","44.5%","44.5%","44.5%"]} display={["none","none","block","block","block",]}  px="16px" bg={"blue.blue600"}>
                
                <Image src='/image/authImg.png' />
            </Box>
            <Box w={["100%","100%","55.5%","55.5%","55.5%"]} px="6%" pb="20px">
             <Image src='/image/logo.png' w={"150px"} display={"block"}/>
                <Header text={"Nice to have you back!"} mt={"-20px"} />
                <Text color={"#808080"} fontWeight={"500"} mt="14px" fontSize={"16px"}
                    textAlign={"center"}>Please fill in your details to get started.</Text>


                <Stack mt="32px" spacing={"32px"}>
                    
                    <Box>
                        <Label text={"email address"} />
                        <Input placeholder='Enter email address' value={Payload.email} id="email" type='email' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"password"} />
                        <Input placeholder='Enter password' value={Payload.password} id="password" type='password' onChange={handlePayload} />
                    </Box>
                  
                </Stack>

                <Text fontWeight={"400"} cursor={"pointer"} fontSize={"16px"}  mt="32px" color={"#CCCCCC"} display={"flex"} justifyContent={"flex-end"}>Forgot Password?</Text>


                <Button 
                disabled={Payload.email === "" || Payload.password === ""  ? true : false} 
                mt={"32px"} py='25px' onClick={LoginBtn} isLoading={Loading}>Log In</Button>

                <Flex justifyContent={"center"} mt="44px">
                    <Box w={"135px"} border="1px solid #808080"></Box>

                </Flex>
                <Flex justifyContent={"center"} mt="-17px">

                    <Box textAlign={"center"} fontWeight={"400"} fontSize={"20px"} bg={"#fff"} w="45px" color="#808080" >or</Box>
                </Flex>


                <Button leftIcon={<FcGoogle/>} hoverBg="#333" py='29px' border="1px solid #2B2B2B"  mt={"39px"} background='transparent' color='#000000'>Continue with Google</Button>

                <Text fontWeight={"400"} fontSize={"16px"} textAlign={"center"} mt="45px" color={"gray.gray600"}>Don't have an account? <Box as="span" color={"blue.blue100"} cursor={"pointer"} fontWeight={"700"} onClick={()=>nav("/sign-up")}>Sign Up</Box></Text>

            </Box>
        </Flex>
    )
}
