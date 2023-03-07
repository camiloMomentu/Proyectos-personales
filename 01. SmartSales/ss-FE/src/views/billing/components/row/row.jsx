import React, { useState } from "react";
import "./styles.css";
import images from "../../../../img/images";

export default function Row({ attributes }) {
  const [discountValue, setDiscount] = useState(attributes.discount);
  const [finalPriceValue, setPrice] = useState(attributes.finalPrice);
  const [amountValue, setAmount] = useState(attributes.amount);

  function handleChange(name, value) {
    if (name == "discount") {
      setDiscount(value);
    }

    if (name == "finalPrice") {
      setPrice(value);
    }

    if (name == "amount") {
      setAmount(value);
    }
  }

  return (
    <tr className="rowTable">
      <td className="tableCell" id="idCell">
        {attributes.id}
        <button className="imgTrash">
          <img src={images.del} />
        </button>
      </td>
      <td className="tableCell" id="product">
        {attributes.product}
      </td>
      <td className="tableCell" id="price">
        {attributes.price}
      </td>
      <td className="tableCell" id="discount">
        <input
          name="discount"
          type="number"
          value={discountValue}
          autoComplete="off"
          onChange={(e) => {
            handleChange(e.target.name, e.target.value);
          }}
        />
      </td>
      <td className="tableCell" id="finalPrice">
        <input
          name="finalPrice"
          type="number"
          value={finalPriceValue}
          autoComplete="off"
          onChange={(e) => {
            handleChange(e.target.name, e.target.value);
          }}
        />
      </td>
      <td className="tableCell" id="amount">
        <input
          name="amount"
          type="number"
          value={amountValue}
          autoComplete="off"
          onChange={(e) => {
            handleChange(e.target.name, e.target.value);
          }}
        />
      </td>
    </tr>
  );
}
