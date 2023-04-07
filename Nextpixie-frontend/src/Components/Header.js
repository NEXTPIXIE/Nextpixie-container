import { Text } from '@chakra-ui/react'
import React from 'react'

export default function Header({mt="32px",text}) {
  return (
    <Text mt={mt} color={"black"} fontWeight={"700"} fontSize={"28px"} textAlign={"center"}>{text}</Text>
  )
}
