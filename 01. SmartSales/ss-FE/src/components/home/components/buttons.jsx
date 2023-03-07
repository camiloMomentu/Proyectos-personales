import React, { useState } from "react";
import "./buttonStyles.css";
import { NavLink } from "react-router-dom";

export default function ButtonView({ attribites }) {
  const [selected, SetSelection] = useState(false);
  const active = "selectorButton_active";
  const inactive = "selectorButton_inactive";

  return (
    <NavLink
      to={attribites.route}
      className={({ isActive }) => {
        if (isActive == true) {
          SetSelection(true);
          return active;
        } else {
          SetSelection(false);
          return inactive;
        }
      }}
    >
      <img
        src={selected ? attribites.image.active : attribites.image.inactive}
      />
      <p>{attribites.text}</p>
    </NavLink>
  );
}
