import React from "react";
import { ImageList } from "@mui/material";
import Stack from "@mui/material/Stack";

const tempImages = [
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
  "https://via.placeholder.com/150",
];

function ImagesList() {
  return (
    <div className="my-4 bg-black overflow-x-scroll	w-100 flex flex-row">
      {tempImages.map((image) => (
        <img
          src={image}
          alt="placeholder"
          width={100}
          height={100}
          className="p-1"
          onClick={() => {}}
        />
      ))}
    </div>
  );
}

export default ImagesList;
