import { React, useState } from "react";
import "./styles.css";
import ProductsModal from "../../components/productsModal/productsModal";

export default function Products({}) {
  const [productsOpen, SetProductsOpen] = useState(false);

  function showProducts() {
    if (productsOpen == true) {
      SetProductsOpen(false);
    } else {
      SetProductsOpen(true);
    }
  }

  let productsExample = [
    { id: 123, name: "producto prueba", price: 999999, amount: 5 },
  ];

  return (
    <div className="containerContentPage">
      <div className="subContainerContentPage_products">
        <header className="headerProducts"></header>
        <div className="containerProducts">
          <div className="izqContainer_products">
            <div className="dataContainer_product">
              <p className="tileProduct">Código:</p>
              <div class="input-wrapper" onClick={showProducts}>
                <input type="search" className="inputSearchProducts" />
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="input-icon"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                    clip-rule="evenodd"
                  />
                </svg>
              </div>
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Producto:</p>
              <input type="text" className="inputProduct" />
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Tipo de producto:</p>
              <input type="text" className="inputProduct" />
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Cantidad en inventario:</p>
              <input type="text" className="inputProduct" />
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Costo:</p>
              <input type="text" className="inputProduct" />
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Porcentaje de ganancia:</p>
              <input type="text" className="inputProduct" />
            </div>
            <div className="dataContainer_product">
              <p className="tileProduct">Precio:</p>
              <input type="text" className="inputProduct" />
            </div>
          </div>
          <div className="derContainer_products"></div>
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
