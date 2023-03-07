import React from "react";
import "./styles.css";

export default function Row({ item }) {
  function responseF() {
    let response = {
      id: item.id,
      name: item.name,
      price: item.price,
      amount: item.amount,
    };
    console.log(response);
  }
  return (
    <tr className="RowProduct" onClick={responseF}>
      <td className="CellProduct">{item.id}</td>
      <td className="CellProduct">{item.name}</td>
      <td className="CellProduct">{item.price}</td>
      <td className="CellProduct">{item.amount}</td>
    </tr>
  );
}
