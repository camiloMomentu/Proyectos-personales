import React from "react";
import "./input.css";

export default function Input({ attribute, handleChange, param }) {
  return (
    <>
      <input
        id={attribute.id}
        name={attribute.name}
        placeholder={attribute.placeholder}
        type={attribute.type}
        autoComplete="off"
        onChange={(e) => handleChange(e.target.name, e.target.value)}
        className="InputLogin"
      />
    </>
  );
}
