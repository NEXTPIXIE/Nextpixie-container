import { Text } from '@chakra-ui/react'
import React from 'react'

export default function Label({text}) {
  return (
    <Text color={"black"} fontWeight={"500"} fontSize={"16px"} textTransform={"capitalize"} mb="12px">{text}</Text>
  )
}
