import axios from "axios";
import { local } from "./Config";


export const SignUpApi = (Payload) => {


    const headers = new Headers();
    headers.append("Content-Type", "application/json");

     return axios.post(`${local}/auth/register/user`, Payload,{

            headers: headers,
    
        })
          .then((response) => {
            // console.log(response);
            return response
          })
          .catch(function (error) {
            console.log(error);
            throw new Error("Network error, please contact Administrator")
          });

}

export const ResendOtp = (Payload) => {


    const headers = new Headers();
    headers.append("Content-Type", "application/json");

     return axios.post(`${local}/auth/request/otp`, Payload,{

            headers: headers,
    
        })
          .then((response) => {
            return response
          })
          .catch(function (error) {
            console.log(error);
            throw new Error("Network error, please contact Administrator")
          });

}


export const VerifyEmail = (Payload) => {

    // console.log("ApiPayload", Payload)

    const headers = new Headers();
    headers.append("Content-Type", "application/json");

     return axios.post(`${local}/auth/verify/otp`, Payload,{

            headers: headers,
    
        })
          .then((response) => {
            return response
          })
          .catch(function (error) {
            console.log(error);
            throw new Error("Network error, please contact Administrator")
          });

}
export const Login = (Payload) => {

    // console.log("ApiPayload", Payload)

    const headers = new Headers();
    headers.append("Content-Type", "application/json");

     return axios.post(`${local}/auth/user/login`, Payload,{

            headers: headers,
    
        })
          .then((response) => {
            return response
          })
          .catch(function (error) {
            console.log(error)
            return error
          });

}