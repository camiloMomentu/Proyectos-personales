import React, { useState, useEffect } from "react";
import "./loginStyles.css";
import images from "./img/images";
import Input from "./components/input/input";
import Register from "./components/register/register";
import ForgetPassword from "./components/forgetPassword/forgetPassword";
import App from "./App";
import axios from "axios";
import petitions from "./conections/config";

export default function Login() {
  const [user, setUser] = useState("");
  const [password, SetPassword] = useState("");
  const [isLogin, SetIsLogin] = useState(false);
  const [openRegister, SetOpenRegister] = useState(false);
  const [forgetPassword, SetForgetPasword] = useState(false);
  const [login, setLogin] = useState({});
  const [errorLogin, SeterrorLogin] = useState(true);

  function handleChange(name, value) {
    if (name == "user") {
      setUser(value);
    } else {
      SetPassword(value);
    }
  }

  function setData(value) {
    let obj = { isLogin: value };
    sessionStorage.setItem("sessionData", JSON.stringify(obj));
  }

  function getData() {
    let data = sessionStorage.getItem("sessionData");
    return (data = JSON.parse(data));
  }

  function submitAccount() {
    axios
      .get(
        `${petitions.host}:${petitions.port}/user/verify?email=${user}&password=${password}`,
        petitions.config
      )
      .then((response) => {
        setLogin(response.data);
        SetIsLogin(response.data.correct_password);
        setData(response.data.correct_password);
        SeterrorLogin(response.data.correct_password);
      })
      .catch((error) => console.log(error));
  }

  function registerModal() {
    if (openRegister == true) {
      SetOpenRegister(false);
    } else {
      SetOpenRegister(true);
    }
  }

  function forgetPasswordModal() {
    if (forgetPassword == true) {
      SetForgetPasword(false);
    } else {
      SetForgetPasword(true);
    }
  }

  useEffect(() => {
    if (getData() != null) {
      if (getData().isLogin == true) {
        SetIsLogin(true);
      }
    }
  }, []);

  return (
    <>
      {isLogin ? (
        <App />
      ) : (
        <div className="container">
          <header className="headerLogin">
            <img src={images.logo} />
          </header>
          <div className="titleContainer">
            <p className="title">SmartSales</p>
          </div>
          <div className="container_form">
            <div className="inputs_container">
              <Input
                attribute={{
                  id: "user",
                  name: "user",
                  type: "text",
                  placeholder: "Email",
                }}
                handleChange={handleChange}
              />
              <Input
                attribute={{
                  id: "password",
                  name: "password",
                  type: "password",
                  placeholder: "Password",
                }}
                handleChange={handleChange}
              />

              {!errorLogin ? (
                <div className="error_login">
                  <p>Contraseña o usuario incorrectos</p>
                </div>
              ) : (
                <></>
              )}
            </div>

            <button className="loginButton" onClick={submitAccount}>
              Login
            </button>

            <div className="linksContainer">
              <button className="linkLogin" onClick={forgetPasswordModal}>
                Olvidé mi contraseña
              </button>
              <br />
              <button className="linkLogin" onClick={registerModal}>
                Registrarse
              </button>
            </div>
          </div>
          {openRegister ? (
            <Register closeRegisterModal={registerModal} />
          ) : (
            <></>
          )}
          {forgetPassword ? (
            <ForgetPassword closeRegisterModal={forgetPasswordModal} />
          ) : (
            <></>
          )}
        </div>
      )}
    </>
  );
}
