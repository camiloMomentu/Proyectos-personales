import React from "react";
import "./styles.css";
import Row from "./components/row/row";
import images from "../../img/images";

export default function ProductsModal({ products, close }) {
  return (
    <div className="containerBackground">
      <div className="containerTable">
        <div className="closeProducts">
          <button onClick={close}>
            <img src={images.close} />
          </button>
        </div>
        <div className="searchContainer">
          <p>Buscar</p>
          <input type="text" />
          <img src={images.search} />
        </div>
        <div className="ScrollContainer">
          <table className="tableProducts">
            <thead className="tableTitles">
              <tr>
                <th className="titleProduct">ID</th>
                <th className="titleProduct">Producto</th>
                <th className="titleProduct">Precio</th>
                <th className="titleProduct">Cantidad</th>
              </tr>
            </thead>
            <tbody>
              {products.map((item, index) => {
                return <Row item={item} key={index} />;
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
