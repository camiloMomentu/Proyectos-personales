import React from "react";
import "./styles.css";
import Dropdown from "../../components/dropdown/dropdown";
import { useState } from "react";

export default function Costs({}) {
  const listCosts = [{ anchor: "Comida" }, { anchor: "Obligatorio" }];

  const [type_cost, SetTypeCost] = useState("");
  const [cost, SetCost] = useState("");
  const [origin, SetOrigin] = useState("");

  function handleContent(name, value) {
    if (name == "type") {
      SetTypeCost(value);
    }

    if (name == "cost") {
      SetCost(value);
    }

    if (name == "origin") {
      SetOrigin(value);
    }
  }

  function submitCost() {
    let infoCost = {
      type: type_cost,
      cost: cost,
      origin: origin,
    };

    console.log(infoCost);
  }

  return (
    <div className="containerContentPage">
      <div className="subContainerContentPage_costs">
        <header className="headerCosts"></header>
        <div className="costsForm">
          <p className="subtitleCosts">Tipo de gasto</p>
          <textarea
            type="text"
            className="inputCosts"
            id="description"
            name={"type"}
            onChange={(e) => {
              handleContent(e.target.name, e.target.value);
            }}
          />

          <p className="subtitleCosts">Costo</p>
          <input
            type="number"
            className="inputCosts"
            name={"cost"}
            onChange={(e) => {
              handleContent(e.target.name, e.target.value);
            }}
          />

          <p className="subtitleCosts">Origen de pago</p>
          <Dropdown
            items={listCosts}
            className={"dropdown_costs"}
            name={"origin"}
          />

          <div className="savebutton">
            <button className="saveCosts" onClick={submitCost}>
              Guardar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
