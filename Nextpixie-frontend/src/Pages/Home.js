import React from 'react'
import MainLayout from '../Layouts/Index'
import Request from '../Utils/Request'
import Seo from '../Utils/Seo'

export default function Home() {
    // const getApi = async ()=>{
    //    const res = await new Request().get({url:"https://jsonplaceholder.typicode.com/posts"})
    //     console.log(res)
    // }
    
  return (
        <MainLayout pageTitle='eco-basket'>
            <Seo title='Home' description='HomePage'/>
        
          
        </MainLayout>
  )
}
