import React, { useEffect, useState } from "react";
import "./frame.css";
import Draggable from "react-draggable";
import Line from "../line";
import { UndefinedSVG, MaleSVG, FemaleSVG } from "../../svg/SVGs";

export default function Frame({ attributes }) {
  const [showInfo, setShowInfo] = useState(false);

  function handleShowInfo(type) {
    if (type == "enter") {
      setShowInfo(true);
    }

    if (type == "leave") {
      setShowInfo(false);
    }

    if (type == "both") {
      if (showInfo) {
        setShowInfo(false);
      } else {
        setShowInfo(true);
      }
    }
  }

  return (
    <Draggable bounds="parent">
      <div
        className="frame_container"
        onMouseEnter={() => {
          handleShowInfo("enter");
        }}
        onMouseLeave={() => {
          handleShowInfo("leave");
        }}
        onClick={() => {
          handleShowInfo("both");
        }}
      >
        <div
          className={showInfo ? "top_frame_active" : "top_frame_unactive"}
          style={{ background: attributes.topColor }}
        ></div>

        <div className="frame">
          {attributes.sex == "H" ? (
            <MaleSVG />
          ) : attributes.sex == "M" ? (
            <FemaleSVG />
          ) : (
            <UndefinedSVG />
          )}
        </div>

        <div
          className={showInfo ? "frame_info_active" : "frame_info_unactive"}
        ></div>
      </div>
    </Draggable>
  );
}
