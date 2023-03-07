import React, { useState, useEffect } from "react";
import Login from "./views/login/index";
import PeopleMap from "./views/map/index";
import Data from "./views/data/index";
import axios from "axios";
import { petitions } from "./config";

export default function App() {
  const [isLogin, setIsLogin] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);

  function SubmitAccount(user, password) {
    axios
      .get(
        `${petitions.host}:${petitions.port}/user?email=${user}&password=${password}`,
        petitions.config
      )
      .then((response) => {
        setData(response.data);
        // setData(response.data.correct_password);
        setIsLogin(response.data.correct_password);
        setIsAdmin(response.data.is_admin);
      })
      .catch((error) => console.log(error));
  }

  function setData(value) {
    sessionStorage.setItem("sessionData", JSON.stringify(value));
  }

  function getData() {
    let data = sessionStorage.getItem("sessionData");
    return JSON.parse(data);
  }

  useEffect(() => {
    const userInfo = getData();
    if (userInfo != null) {
      if (userInfo.correct_password == true) {
        setIsLogin(true);
        setIsAdmin(userInfo.is_admin);
      }
    }
  }, []);

  return (
    <>
      {isLogin ? (
        isAdmin ? (
          <Data handleExit={setData} />
        ) : (
          <PeopleMap />
        )
      ) : (
        <Login setLogin={SubmitAccount} />
      )}
    </>
  );
}
