import React from "react";
import "./menuStyles.css";
import ButtonView from "./buttons";

export default function Menu({ buttons }) {
  return (
    <>
      <nav className="navigation">
        {buttons.map((item, index) => {
          return (
            <ButtonView
              key={index}
              attribites={{
                image: item.image,
                text: item.text,
                status: item.status,
                route: item.route,
              }}
            />
          );
        })}
      </nav>
    </>
  );
}
