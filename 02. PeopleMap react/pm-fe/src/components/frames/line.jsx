import React from "react";
import { PathLine } from "react-svg-pathline";
import "./line.css";

function Line({ attributes }) {
  return (
    <svg className="lines_svg">
      <PathLine
        points={[
          { x: attributes.x1, y: attributes.y1 },
          {
            x: attributes.x1 + (attributes.x2 - attributes.x1) / 2,
            y: attributes.y1,
          },
          {
            x: attributes.x1 + (attributes.x2 - attributes.x1) / 2,
            y: attributes.y2,
          },
          { x: attributes.x2, y: attributes.y2 },
        ]}
        stroke="white"
        strokeWidth="1"
        fill="none"
        r={10}
      />
    </svg>
  );
}

export default Line;
