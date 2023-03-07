import React, { useState } from "react";
import "./styles.css";
import images from "../../img/images";

export default function ForgetPassword({ closeRegisterModal }) {
  const [email, setEmail] = useState("");

  function handleInfo(value) {
    setEmail(value);
  }

  function sendEmail() {
    console.log(email);
  }

  return (
    <div className="forgetFill">
      <div className="forgetContainer">
        <button className="close" onClick={closeRegisterModal}>
          <img src={images.close} />
        </button>
        <p className="forgetTitle">Recuperar contraseña</p>
        <div className="inputContainer">
          <input
            type="text"
            name="email"
            placeholder="Correo"
            autoComplete="on"
            onChange={(e) => {
              handleInfo(e.target.value);
            }}
          />

          <button className="forgetButton" onClick={sendEmail}>
            Enviar email
          </button>
        </div>
      </div>
    </div>
  );
}
