import React, { useState } from "react";
import "./styles.css";
import images from "../../img/images";
import tablesInfo from "../../info/table";
import CellSearch from "./components/cells/cell";
import Row from "./components/row/row";
import Dropdown from "../../components/dropdown/dropdown";
import ProductsModal from "../../components/productsModal/productsModal";

export default function Billing({}) {
  const [generalDiscount, setGeneralDiscount] = useState(0);
  const [productsOpen, SetProductsOpen] = useState(false);

  let productsExample = [
    { id: 123, name: "producto prueba", price: 999999, amount: 5 },
  ];

  let clients = [{ anchor: "Camilo" }];

  function handleChange(name, value) {
    if (name == "generalDiscount") {
      setGeneralDiscount(value);
    }
  }

  function showProducts() {
    if (productsOpen == true) {
      SetProductsOpen(false);
    } else {
      SetProductsOpen(true);
    }
  }

  return (
    <div className="containerContentPage">
      <div className="subContainerContentPage">
        <div className="billingOptions">
          <div className="Option">
            <p>Cliente</p>
            <Dropdown items={clients} />
          </div>
          <div className="Option">
            <p>Porcentaje de descuento</p>
            <input
              type="number"
              id="porcentage"
              name="generalDiscount"
              autoComplete="off"
              value={generalDiscount}
              onChange={(e) => {
                handleChange(e.target.name, e.target.value);
              }}
            />
            <p>%</p>
          </div>
        </div>
        <div className="tableBillingContainer">
          <table className="tableBilling" border={"0"}>
            <thead>
              <tr>
                {tablesInfo.titles.map((item, index) => {
                  return (
                    <th className="tableHeader" key={index}>
                      {item}
                    </th>
                  );
                })}
              </tr>
            </thead>
            <tbody>
              <Row
                attributes={{
                  id: 1234,
                  product: "Prueba producto",
                  price: 999999,
                  discount: 0,
                  finalPrice: 999999,
                  amount: 1,
                }}
              />
              <CellSearch show={showProducts} />
            </tbody>
          </table>
        </div>
        <div className="unHeaderContainer">
          <div className="unHeader">
            <div className="discountContainer">
              <p className="titleCalc">Descuento:</p>
              <p className="contentCalc"></p>
            </div>
            <div className="salesContainer">
              <p className="titleCalc">Venta:</p>
              <p className="contentCalc"></p>
            </div>
          </div>
          <button className="imgSave">
            <img src={images.saveIcon} className="saveIcon" />
          </button>
        </div>
      </div>
      {productsOpen ? (
        <ProductsModal products={productsExample} close={showProducts} />
      ) : (
        <></>
      )}
    </div>
  );
}
