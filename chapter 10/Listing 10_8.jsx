#Listing 10_8: Get response with Axios
import React, { useEffect, useState } from 'react'
import axios from 'axios'

function Api() {
  const [userData, setData] = useState([]);
    useEffect  (() => {
        axios.get("https://reqres.in/api/users?page=2")
        .then((Response) => {
            console.log(Response)
            setData(Response.data)
        })
    }, [])

  return (
    <div>
      <h2>GET API with Axios</h2>
    {userData.data?.map((item, index) => {
      return (
        <div key={index}  style={{border: "1px solid", margin: "10px", padding: "10px"}}>
          <p><b>Name:</b> {item.last_name}, {item.first_name} <b>Email:</b> {item.email}</p>
        </div>
      )
    })}
    </div>
  )
}

export default Api
