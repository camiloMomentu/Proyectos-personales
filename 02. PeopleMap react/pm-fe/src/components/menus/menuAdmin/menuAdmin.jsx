import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./menuAdmin.css";

export default function MenuAdmin({ options, handlePM }) {
  return (
    <div className="menu_container">
      {options.map((item, key) => {
        return (
          <NavLink
            key={key}
            to={item.path}
            className={({ isActive }) => {
              if (isActive) {
                return "option_menu_admin_active";
              } else {
                return "option_menu_admin";
              }
            }}
          >
            <p>{item.title}</p>
          </NavLink>
        );
      })}

      <div className="PM_menu_admin" onClick={handlePM}>
        <p>People Map</p>
      </div>
    </div>
  );
}
