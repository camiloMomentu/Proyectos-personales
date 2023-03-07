import React, { useEffect, useState } from "react";
import {
  MenuLogoSVG,
  MoreSVG,
  SearchSVG,
  CompareSVG,
  AdminSVG,
} from "../../svg/SVGs";
import "./menuMap.css";
import Draggable from "react-draggable";

export default function MenuMap({ admin, handleAdmin }) {
  const [activeMenu, setActiveMenu] = useState(false);

  function handleMenu() {
    if (activeMenu) {
      setActiveMenu(false);
    } else {
      setActiveMenu(true);
    }
  }

  useEffect(() => {
    console.log(admin);
  }, []);

  return (
    <Draggable axis="y" defaultPosition={{ x: 0, y: 200 }} bounds="parent">
      <div className="menu">
        <button className="options_button" onClick={handleMenu}>
          <MenuLogoSVG />
        </button>
        <div className={activeMenu ? "menu_active" : "menu_unactive"}>
          <div className="option_menu">
            <MoreSVG />
            <p>Nuevo</p>
          </div>

          <div className="option_menu">
            <SearchSVG />
            <p>Buscar</p>
          </div>

          <div className="option_menu">
            <CompareSVG />
            <p>Comparar</p>
          </div>

          {admin ? (
            <div className="option_menu" onClick={handleAdmin}>
              <AdminSVG />
              <p>Admin</p>
            </div>
          ) : (
            <></>
          )}
        </div>
      </div>
    </Draggable>
  );
}
