import "./index.css";
import React, { useState } from "react";
import LoginFrame from "../../components/frames/Login/loginFrame";
import loginFrames from "./info/lists_frames";
import images from "../../images/images";
import RegisterModal from "../../components/modals/register/register";

export default function Login({ setLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [forguet, setForguet] = useState("");
  const [modalStatus, SetModalStatus] = useState(false);

  function handleState(name, value) {
    if (name == "email") {
      setEmail(value);
    }

    if (name == "password") {
      setPassword(value);
    }

    if (name == "forguet") {
      setForguet(value);
    }

    if (value == "SubmitAccount") {
      setLogin(email, password);
    }
  }

  function showModal() {
    if (modalStatus) {
      SetModalStatus(false);
    } else {
      SetModalStatus(true);
    }
  }

  return (
    <div className="login_container">
      <div className="form_container">
        <div className="title_login">
          <img src={images.logo} />
          <p>People Map</p>
        </div>
        {loginFrames.map((item, key) => {
          return (
            <LoginFrame
              attributes={item}
              handleFunction={handleState}
              showModal={showModal}
              key={key}
            />
          );
        })}
      </div>
      {modalStatus ? <RegisterModal handleModal={showModal} /> : <></>}
    </div>
  );
}
