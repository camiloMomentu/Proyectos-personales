import React from "react";
import "./styles.css";
import images from "../../../../img/images";

export default function CellSearch({ show }) {
  return (
    <tr>
      <td className="tableCell" id="cellSearch">
        <input type="text" className="inputCell" />
        <button className="imgContainerCell" onClick={show}>
          <img src={images.search} />
        </button>
      </td>
    </tr>
  );
}
