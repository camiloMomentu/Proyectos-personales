import React from "react";
import "./infoList.css";

export default function InfoList({ attributes }) {
  return (
    <div className="info_list_container">
      <div className="item_container">
        <p className="title_list">Empleados:</p>
        <p className="text_list">3</p>
      </div>
    </div>
  );
}
