import "./index.css";
import React, { useEffect, useState } from "react";
import Frame from "../../components/frames/frame/frame";
import MenuMap from "../../components/menus/menuMap/menuMap";
import InfoList from "../../components/infoList/infoList";

export default function PeopleMap({ handleAdmin }) {
  const [rigthSize, setRigthSize] = useState(false);
  const [bottomSize, setBottomSize] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);

  function getData() {
    let data = sessionStorage.getItem("sessionData");
    return JSON.parse(data);
  }

  function handleSize(id) {
    if (id == "rigth") {
      if (rigthSize) {
        setRigthSize(false);
      } else {
        setRigthSize(true);
      }
    }

    if (id == "bottom") {
      if (bottomSize) {
        setBottomSize(false);
      } else {
        setBottomSize(true);
      }
    }
  }

  useEffect(() => {
    setIsAdmin(getData().is_admin);
  }, []);

  return (
    <div className="app_container">
      <div className="frames_container">
        <Frame attributes={{ sex: "H", topColor: "#45C4B0" }} />
      </div>
      <div
        className={rigthSize ? "rigth_bar_active" : "rigth_bar_unactive"}
        onClick={() => {
          handleSize("rigth");
        }}
      >
        <div
          className={
            rigthSize ? "rigth_content_active" : "rigth_content_unactive"
          }
        ></div>
        <div className="rigth_button"></div>
      </div>
      <div
        className={bottomSize ? "bottom_bar_active" : "bottom_bar_unactive"}
        onClick={() => {
          handleSize("bottom");
        }}
      >
        <div className="bottom_button"></div>
        <div
          className={
            bottomSize ? "bottom_content_active" : "bottom_content_unactive"
          }
        >
          <InfoList />
        </div>
      </div>
      <MenuMap admin={isAdmin} handleAdmin={handleAdmin} />
    </div>
  );
}
