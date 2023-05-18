import { Box, Flex, Image, Stack, Text } from '@chakra-ui/react'
import React, { useState } from 'react'
import Header from '../../Components/Header'
import Label from '../../Components/Label'
import Input from '../../Components/Input'
import Button from '../../Components/Button'
import { FcGoogle } from 'react-icons/fc';
import { useNavigate } from 'react-router-dom'

export default function EmailVerification() {
    const [Loading, setLoading] = useState(false);
    const [Payload, setPayload] = useState({
       
        otp: "",
        email: "",
        
    });

    const nav = useNavigate() 




    const handlePayload = (e)=>{
        setPayload({
          ...Payload,
           [e.target.id]: e.target.value
        })
    }

    const Proceed = ()=>{
        setLoading(true)
        
        setTimeout(() => {
            
            setLoading(false)
        }, 3000);
    }

    const resendOtp  =()=>{

    }


    return (
        <Flex minH={"100vh"} flexDir={["column-reverse","column-reverse","row","row","row"]}>
            <Box w={["100%","44.5%","44.5%","44.5%","44.5%"]} display={["none","none","block","block","block",]}  px="16px" bg={"blue.blue600"}>
                
            <Image src='/image/logo.png' />
            <Image src='/image/authImg.png' />
            </Box>
            <Box w={["100%","100%","55.5%","55.5%","55.5%"]} px="6%" pb="20px">
            <Image src='/image/logo.png' w={"150px"} display={["block","block","none","none","none",]}/>
            <Header text={"Email Verification"} mt={["-20px","-20px","65px","65px","65px"]} />
                <Text color={"#808080"} fontWeight={"500"} mt="14px" fontSize={"16px"}
                    textAlign={"center"}>Kindly input the OTP code that was sent to your email address.</Text>


                <Stack mt="32px" spacing={"32px"}>
                    
                    <Box>
                        <Label text={"OTP code"} />
                        <Input placeholder='Enter OTP code' value={Payload.otp} id="otp" type='text' onChange={handlePayload} />
                    </Box>
                   
                  
                </Stack>

                <Text display={"flex"} justifyContent={"flex-end"} fontWeight={"400"} fontSize={"16px"} textAlign={"center"} mt="32px" color={"gray.gray600"}>Didn’t get an OTP Code? 
                <Box as="span" pl="5px" color={"blue.blue100"} cursor={"pointer"} fontWeight={"700"} onClick={resendOtp}> Resend </Box></Text>


                <Button 
                disabled={Payload.otp === "" ? true : false} 
                mt={"32px"} py='25px' onClick={Proceed} isLoading={Loading}>Proceed</Button>

               



                <Text fontWeight={"400"} fontSize={"16px"} textAlign={"center"} mt="45px" color={"gray.gray600"}>Already have an account? <Box as="span" cursor={"pointer"} color={"blue.blue100"} fontWeight={"700"} onClick={()=>nav("/sign-in")}>Sign In</Box></Text>

            </Box>
        </Flex>
    )
}
