#Listing 10_7: GET request with Axios
import React, { useEffect } from 'react'
import axios from 'axios'

function Api() {
    useEffect  (() => {
        axios.get("https://api.restful-api.dev/objects/7")
        .then((Response) => {
            console.log(Response)
        })
    }, [])

  return (
    <div>
      GET API with Axios
    </div>
  )
}

export default Api
