import React, { useState } from "react";
import "./styles.css";
import images from "../../img/images";
import { postUser } from "../../conections/login";

export default function Register({ closeRegisterModal }) {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [last_name, setLastName] = useState("");
  const [company, setCompany] = useState("");
  const [password, setPassword] = useState("");
  const [rePassword, setRePassword] = useState("");

  function handleInfo(name, value) {
    if (name == "email") {
      setEmail(value);
    }

    if (name == "name") {
      setName(value);
    }

    if (name == "last_name") {
      setLastName(value);
    }

    if (name == "company") {
      setCompany(value);
    }

    if (name == "password") {
      setPassword(value);
    }

    if (name == "rePassword") {
      setRePassword(value);
    }
  }

  function register() {
    let infoRegister = {
      name: name,
      last_name: last_name,
      email: email,
      password: password,
      is_admin: true,
      is_active: true,
      created_at: Date.now(),
      company: company,
    };
    console.log(infoRegister);
  }

  return (
    <div className="registerFill">
      <div className="registerContainer">
        <button className="close" onClick={closeRegisterModal}>
          <img src={images.close} />
        </button>
        <p className="registerTitle">Registrarse</p>
        <div className="inputsContainer">
          <input
            type="text"
            name="email"
            placeholder="Correo"
            autoComplete="on"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <input
            type="text"
            name="name"
            placeholder="Nombre"
            autoComplete="off"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <input
            type="text"
            name="last_name"
            placeholder="Apellido"
            autoComplete="off"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <input
            type="text"
            name="company"
            placeholder="Empresa"
            autoComplete="off"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <input
            type="password"
            name="password"
            placeholder="Contraseña"
            autoComplete="off"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <input
            type="password"
            name="rePassword"
            placeholder="Repita su contraseña"
            autoComplete="off"
            onChange={(e) => {
              handleInfo(e.target.name, e.target.value);
            }}
          />
          <button className="registerButton" onClick={register}>
            Registarse
          </button>
        </div>
      </div>
    </div>
  );
}
