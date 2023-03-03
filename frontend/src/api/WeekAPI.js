const BASE_URL = "http://127.0.0.1:8000/workouts/"  

const token = localStorage.getItem("token")

const tryCatchFetch = async (url) => {
  
  const headers = {}
  if (token) {
    headers.Authorization = `Token ${token}`;
    // console.log(headers, "This is our header token data1") // remove when done
  }

  try {
    // console.log(headers, "This is our header token data2") // remove when done
    const response = await fetch(url, {headers,})
    if (response.ok) {
      return await response.json()
    }
    else {
      throw new Error(`Bad response: ${response.status} ${response.statusText}`)
    }
  }
  catch (e) {
    console.error(e)
    return null
  }
}

const fetchWeeks = async () => {
  const url = BASE_URL
  // console.log("Fetching weeks from API..."); // Delete this line when done testing
  return await tryCatchFetch(url, token);
  // console.log("Response from API:", response); // Delete this line when done testing
}


const exportItems = {
  fetchWeeks,
}

export default exportItems




// const BASE_URL = "http://127.0.0.1:8000/workouts/"  


// const tryCatchFetch = async (url, init = null) => {

//   try {
//     const response = await fetch(url, init)
//     if (response.ok) {
//       return await response.json()
//     }
//     else {
//       throw new Error(`Bad response: ${response.status} ${response.statusText}`)
//     }
//   }
//   catch (e) {
//     console.error(e)
//     return null
//   }
// }

// const fetchWeeks = async () => {
//   const url = BASE_URL
//   // console.log("Fetching weeks from API..."); // Delete this line when done testing
//   return await tryCatchFetch(url);
//   // console.log("Response from API:", response); // Delete this line when done testing
// }

// // const fetchWeekByNumber = async (week_number) => {
// //   const url = BASE_URL + `${week_number}`
// //   return await tryCatchFetch(url)
// // }

// const exportItems = {
//   fetchWeeks,
//   // fetchWeekByNumber,
// }

// export default exportItems
