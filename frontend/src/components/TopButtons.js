import React from "react";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import FileUploadIcon from "@mui/icons-material/FileUpload";
import { Container } from "@mui/system";

function TopButtons() {
  return (
    <div className="justify-between flex">
      <Button variant="contained" startIcon={<FileUploadIcon />}>
        Upload Images
      </Button>
      <Button variant="contained" color="error" startIcon={<DeleteIcon />}>
        Delete all
      </Button>
    </div>
  );
}

export default TopButtons;
