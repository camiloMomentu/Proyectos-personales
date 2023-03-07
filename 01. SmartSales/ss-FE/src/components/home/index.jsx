import React from "react";
import "./styles.css";
import images from "../../img/images";
import Menu from "./components/menu";
import { Link } from "react-router-dom";

export default function MenuHome({ title, buttons }) {
  function setData(value) {
    let obj = { isLogin: value };
    sessionStorage.setItem("sessionData", JSON.stringify(obj));
  }

  function exit() {
    setData(false);
    window.location.reload(true);
  }

  return (
    <>
      <header className="headerIndex">
        <div id="imgContainer">
          <Link to={"/"}>
            <img src={images.logo} />
          </Link>
        </div>
        <p>{title}</p>
        <button className="exitContainer" onClick={exit}>
          <img src={images.exit} />
        </button>
      </header>
      <div className="containerContent">
        <Menu buttons={buttons} />
      </div>
    </>
  );
}
