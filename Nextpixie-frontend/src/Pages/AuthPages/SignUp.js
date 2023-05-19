import { Box, Flex, Image, Stack, Text } from '@chakra-ui/react'
import React, { useState } from 'react'
import Header from '../../Components/Header'
import Label from '../../Components/Label'
import Input from '../../Components/Input'
import Button from '../../Components/Button'
import { FcGoogle } from 'react-icons/fc';
import { useNavigate } from 'react-router-dom'
import { SignUpApi } from '../../Utils/ApiCall'

export default function SignUp() {
    const [Loading, setLoading] = useState(false);
    const [Payload, setPayload] = useState({
        first_name: "",
        last_name: "",
        business_name: "",
        email: "",
        password: "",
        confirm_password: ""
    });


    const nav = useNavigate() 
    const handlePayload = (e)=>{
        setPayload({
          ...Payload,
           [e.target.id]: e.target.value
        })
    }

    const signUpBtn = async ()=>{
        setLoading(true)


        try {
            setLoading(true)
            let result = await SignUpApi(Payload);
            console.log("result", result);
            if (result.status  === 200) {
                setLoading(false)
                localStorage.setItem("newEmail", Payload.email)
                setPayload({
                    first_name: "",
                    last_name: "",
                    business_name: "",
                    email: "",
                    password: "",
                    confirm_password: ""
                })

                nav("/email-verification")


    
            } else {

                setLoading(false)  

            }


        } catch (e) {

            setLoading(false)
           
            console.error('Error:', e.message);
        }



        
        
    }

    
    



    return (
        <Flex minH={"100vh"} flexDir={["column-reverse","column-reverse","row","row","row"]}>
            <Box w={["100%","44.5%","44.5%","44.5%","44.5%"]} display={["none","none","block","block","block",]}  px="16px" bg={"blue.blue600"}>
                <Image src='/image/logo.png' />
                <Image src='/image/authImg.png' />
            </Box>
            <Box w={["100%","100%","55.5%","55.5%","55.5%"]} px="6%" pb="20px">
             <Image src='/image/logo.png' w={"150px"} display={["block","block","none","none","none",]}/>
                <Header text={"Welcome to NextPixie!"} mt={["-20px","-20px","65px","65px","65px"]} />
                <Text color={"#808080"} fontWeight={"500"} mt="14px" fontSize={"16px"}
                    textAlign={"center"}>Please fill in your details to get started.</Text>


                <Stack mt="32px" spacing={"32px"}>
                    <Box>
                        <Label text={"first name"} />
                        <Input placeholder='Enter first name' value={Payload.first_name} id="first_name" type='text' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"last name"} />
                        <Input placeholder='Enter last name' value={Payload.last_name} id="last_name" type='text' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"business name"} />
                        <Input placeholder='Enter business name' value={Payload.business_name} id="business_name" type='text' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"email address"} />
                        <Input placeholder='Enter email address' value={Payload.email} id="email" type='email' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"password"} />
                        <Input placeholder='Enter password' value={Payload.password} id="password" type='password' onChange={handlePayload} />
                    </Box>
                    <Box>
                        <Label text={"confirm password"} />
                        <Input placeholder='Enter password' value={Payload.confirm_password} id="confirm_password" type='password' onChange={handlePayload} />
                    </Box>
                </Stack>

                <Button 
                disabled={Payload.first_name === "" || Payload.last_name === "" || Payload.business_name === "" || Payload.email === "" || Payload.password === "" || Payload.confirm_password === "" ? true : false} 
                mt={"32px"} py='25px' onClick={signUpBtn} isLoading={Loading}>sign up</Button>

                <Flex justifyContent={"center"} mt="44px">
                    <Box w={"135px"} border="1px solid #808080"></Box>

                </Flex>
                <Flex justifyContent={"center"} mt="-17px">

                    <Box textAlign={"center"} fontWeight={"400"} fontSize={"20px"} bg={"#fff"} w="45px" color="#808080" >or</Box>
                </Flex>


                <Button leftIcon={<FcGoogle/>} hoverBg="#333" py='29px' border="1px solid #2B2B2B"  mt={"39px"} background='transparent' color='#000000'>Sign up with Google</Button>

                <Text fontWeight={"400"} fontSize={"16px"} textAlign={"center"} mt="45px" color={"gray.gray600"}>Already have an account? <Box as="span" cursor={"pointer"} color={"blue.blue100"} fontWeight={"700"} onClick={()=>nav("/sign-in")}>Sign In</Box></Text>

            </Box>
        </Flex>
    )
}
