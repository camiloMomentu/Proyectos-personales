import React, { useState } from "react";
import "./register.css";
import images from "../../../images/images";
import axios from "axios";
import { petitions } from "../../../config";

export default function RegisterModal({ handleModal }) {
  const [firstName, setFirstName] = useState();
  const [lastName, setLasttName] = useState();
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [company, setCompany] = useState();

  function handleInfo(name, value) {
    if (name == "name") {
      setFirstName(value);
    }

    if (name == "lastName") {
      setLasttName(value);
    }

    if (name == "email") {
      setEmail(value);
    }

    if (name == "password") {
      setPassword(value);
    }

    if (name == "company") {
      setCompany(value);
    }
  }

  function SetUser() {
    const data = {
      firstName: firstName,
      lastName: lastName,
      email: email,
      password: password,
      company: company,
    };

    axios
      .post(`${petitions.host}:${petitions.port}/user`, data, petitions.config)
      .then(() => {
        handleModal();
      })
      .catch((error) => console.log(error));
  }

  return (
    <div className="modal_backgroun">
      <div className="frame_modal">
        <header>
          <button onClick={handleModal}>
            <img src={images.close} />
          </button>
        </header>

        <div className="info_container">
          <p>Registrarme</p>
          <div className="inputs_container">
            <input
              type="text"
              placeholder="Nombre"
              name="name"
              onChange={(e) => {
                handleInfo(e.target.name, e.target.value);
              }}
              autoComplete="off"
            />
            <input
              type="text"
              placeholder="Apellido"
              name="lastName"
              onChange={(e) => {
                handleInfo(e.target.name, e.target.value);
              }}
              autoComplete="off"
            />
            <input
              type="text"
              placeholder="Correo"
              name="email"
              onChange={(e) => {
                handleInfo(e.target.name, e.target.value);
              }}
              autoComplete="off"
            />
            <input
              type="password"
              placeholder="Contraseña"
              name="password"
              onChange={(e) => {
                handleInfo(e.target.name, e.target.value);
              }}
              autoComplete="off"
            />
            <input
              type="text"
              placeholder="Empresa"
              name="company"
              onChange={(e) => {
                handleInfo(e.target.name, e.target.value);
              }}
              autoComplete="off"
            />
          </div>

          <div className="button_container">
            <button className="register_button" onClick={SetUser}>
              Enviar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
