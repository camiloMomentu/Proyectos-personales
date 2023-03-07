import React, { useState, useEffect, useRef } from "react";
import "./styles.css";

export default function Dropdown({
  items = [],
  className = "dropdown_wrapper",
}) {
  const activatorRef = useRef(null);
  const dropdownListRef = useRef(null);
  const [isOpen, setIsOpen] = useState(false);
  const [textValue, setValue] = useState("");

  function clickHandler() {
    setIsOpen(!isOpen);
  }

  function keyHandler(event) {
    if (event.key === "Escape" && isOpen) {
      setIsOpen(false);
    }
  }

  function clickOutsideHandler(event) {
    if (dropdownListRef.current) {
      if (
        dropdownListRef.current.contains(event.target) ||
        activatorRef.current.contains(event.target)
      ) {
        return;
      }

      setIsOpen(false);
    }
  }

  function getText(value) {
    clickHandler();
    setValue(value);
  }

  useEffect(() => {
    if (isOpen) {
      dropdownListRef.current.querySelector("button").focus();
      document.addEventListener("mousedown", clickOutsideHandler);
    } else {
      document.addEventListener("mousedown", clickOutsideHandler);
    }
  }, [isOpen]);

  return (
    <div className={className} onKeyUp={keyHandler}>
      <button
        className={"dropdown_activator"}
        aria-haspopup="true"
        aria-controls={textValue}
        onClick={clickHandler}
        ref={activatorRef}
      >
        {textValue}
        {isOpen ? (
          <svg
            height="24"
            fill="rgb(70,70,70)"
            viewBox="0 0 24 24"
            width="24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="m0 0h24v24h-24z" fill="none" />
            <path d="m7.41 15.41 4.59-4.58 4.59 4.58 1.41-1.41-6-6-6 6z" />
          </svg>
        ) : (
          <svg
            height="24"
            fill="rgb(70,70,70)"
            viewBox="0 0 24 24"
            width="24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="m0 0h24v24h-24z" fill="none" />
            <path d="m7.41 8.59 4.59 4.58 4.59-4.58 1.41 1.41-6 6-6-6z" />
          </svg>
        )}
      </button>
      <ul
        ref={dropdownListRef}
        className={`${"dropdown_item_list"} ${isOpen ? "active" : ""} `}
      >
        {items.map((item, index) => {
          return (
            <li className={"item_list"} key={index}>
              <button
                value={item.anchor}
                onClick={(e) => {
                  getText(e.target.value);
                }}
              >
                {item.anchor}
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
