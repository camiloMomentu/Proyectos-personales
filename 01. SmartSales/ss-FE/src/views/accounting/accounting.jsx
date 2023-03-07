import React from "react";
import "./styles.css";

export default function Accounting({}) {
  return (
    <div className="containerContentPage">
      <div className="subContainerContentPage">
        <div className="generalContainer">
          <div className="izqContainer">
            <div className="tableContainerAcounting">
              <table border={"0"}>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Producto</th>
                    <th>Precio</th>
                    <th>Cantidad</th>
                    <th>Descuento</th>
                  </tr>
                </thead>
                <tbody></tbody>
              </table>
            </div>
            <div className="costContainer">
              <p className="titleCost">Gastos</p>
              <div className="tableContainerCosts">
                <table>
                  <thead>
                    <th>Tipo</th>
                    <th>Gasto</th>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>
          </div>
          <div className="derContainer">
            <div className="attributeAccountingContainer">
              <p className="textTitle">Fecha</p>
              <input type="date" className="inputDate" />
            </div>
            <div className="attributeAccountingContainer">
              <p className="textTitle">Descuentos</p>
              <p className="textValue"></p>
            </div>
            <div className="attributeAccountingContainer">
              <p className="textTitle">Ganancias</p>
              <p className="textValue"></p>
            </div>
            <div className="attributeAccountingContainer">
              <p className="textTitle">Ventas netas</p>
              <p className="textValue"></p>
            </div>
            <div className="attributeAccountingContainer">
              <p className="textTitle">Gastos</p>
              <p className="textValue"></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
