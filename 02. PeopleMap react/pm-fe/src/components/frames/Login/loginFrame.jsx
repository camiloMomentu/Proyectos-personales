import React, { useEffect, useState } from "react";
import "./loginFrame.css";
import Draggable from "react-draggable";
import Line from "../line";
import images from "../../../images/images";

export default function LoginFrame({ attributes, handleFunction, showModal }) {
  const [status, SetStatus] = useState(false);
  const [hasLine, SetLine] = useState(false);
  const [XPos, SetX] = useState(attributes.position.x + 10);
  const [YPos, SetY] = useState(attributes.position.y + 35);

  useEffect(() => {
    if (attributes.position_father != "") {
      SetLine(true);
    }
  }, []);

  function show_content(target) {
    if ((attributes.type == "input") | (attributes.type == "link")) {
      if (
        (target != "inputLogin_active") &
        (target != "inputLogin_active_send")
      ) {
        if (status) {
          SetStatus(false);
        } else {
          SetStatus(true);
        }
      }
    }
  }

  function getPosition(event, data) {
    SetX(data.x + 10);
    SetY(data.y + 35);
  }

  return (
    <div className="principal_frame_container">
      <Draggable
        defaultPosition={attributes.position}
        onDrag={getPosition}
        disabled={attributes.father == 0 ? true : false}
      >
        <button
          className={status ? "principal_frame_big" : "principal_frame"}
          onClick={(e) => {
            attributes.title != "Ingresar"
              ? attributes.title == "Registrarse"
                ? showModal()
                : show_content(e.target.className)
              : handleFunction(e.target.name, "SubmitAccount");
          }}
          name={attributes.title}
        >
          <img
            src={attributes.image}
            className={
              !attributes.send_button
                ? "image_principal_frame"
                : !status
                ? "image_principal_frame"
                : "button_send_deactivate"
            }
          />
          <p>{attributes.title}</p>

          {attributes.type == "input" ? (
            <input
              type={attributes.input_config.type}
              name={attributes.input_config.name}
              id={attributes.input_config.name}
              className={
                status
                  ? attributes.send_button
                    ? "inputLogin_active_send"
                    : "inputLogin_active"
                  : "inputLogin_inactive"
              }
              autoComplete="off"
              placeholder={attributes.placeholder}
              onChange={(e) => {
                handleFunction(e.target.name, e.target.value);
              }}
            />
          ) : (
            <></>
          )}

          {attributes.send_button ? (
            <button
              className={status ? "button_send" : "button_send_deactivate"}
            >
              <img src={images.send} className />
            </button>
          ) : (
            <></>
          )}
        </button>
      </Draggable>

      {hasLine ? (
        <Line
          attributes={{
            id: attributes.id,
            id_father: attributes.father,
            x1: attributes.position_father.x + 210,
            y1: attributes.position_father.y + 35,
            x2: XPos,
            y2: YPos,
          }}
        />
      ) : (
        <></>
      )}
    </div>
  );
}
