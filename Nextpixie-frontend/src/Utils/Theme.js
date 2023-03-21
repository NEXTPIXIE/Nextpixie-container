import { extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  fonts: {
    heading: "'Public Sans', sans-serif",
    body: "'Public Sans', sans-serif",
  },
  colors: {
    blue: {
      blue500: '#211f5c',
      blue400: '#2C346D',
      blue300: '#3A4A7E',
      blue200: '#20486D',
      blue100: '#00203F',
      
    },
    red: {
      red500: '#EE4223',
      red400: '#F05C36',
      red300: '#F06944',
      red200: '#F3937A',
      red100: '#F5BDB7',
    },
    orange: {
      orange500: '#F5862E',
      orange400: '#F79749',
      orange300: '#FBBA7F',
      orange200: '#FCC38D',
      orange100: '#FEE8C9',
    },
    gray: {
      gray500: 'rgba(255, 255, 255, 0.6)',
      gray400: '#EBF5FF',
      gray300: '#858383',
      gray200: '#C0C0C1',
      gray100: '#EBF5FF;',
    },
    background: '#EEF3FF',
    green: '#38890B',
    white: '#FFFFFF',
    black: '#000000',
  },
  initialColorMode: 'light',
  useSystemColorMode: false,
});

export default theme;