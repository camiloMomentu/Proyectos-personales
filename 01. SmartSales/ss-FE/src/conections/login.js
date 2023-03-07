import axios from "axios";

const host = "http://127.0.0.1";
const port = 8080;
const config = {
  headers: {
    Authorization: "Bearer " + "123456789",
  },
};

export async function postUser(data) {
  const response = await axios.post(`${host}:${port}/user`, data, config);
  console.log(response);
}

export function getUser(email, password, setVariable) {
  axios.get(
      `${host}:${port}/user/verify?email=${email}&password=${password}`,
      config
    )
    .then((response) => setVariable(response))
    .catch((error) => console.log(error));
}
