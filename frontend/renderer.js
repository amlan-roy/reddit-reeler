const { webFrame, dialog } = require("electron");

const chooseFile = document.getElementById("imgInput");
const tempText =
  "Hello world. I am Amlan Roy and I am typing this just to make a placeholder text. This text represents the detected image text.";

chooseFile.addEventListener("change", function () {
  getImgData();
});

const uploadFiles = document.getElementById("uploadImagesButton");
uploadFiles.addEventListener("click", function () {
  setSelectedImages();
});

function getImgData() {
  const files = chooseFile.files;
  console.log(files);
}

function setSelectedImages() {
  const chooseFile = document.getElementById("imgInput");
  const files = chooseFile.files;

  const filenames = [];

  let l = files.length;

  for (let i = 0; i < l; i++) {
    filenames.push(files[i].path);
  }

  // console.log(filenames);
  setFileList(filenames);
}

function setFileList(filenames) {
  const fileNamesContainer = document.getElementById("fileNamesContainer");
  deleteAll();

  const cutFileNames = [];
  for (let i = 0; filenames.length; i++) {
    const splitNames = filenames[i].split("\\");
    const fileName = splitNames[splitNames.length - 1];
    const e = document.createElement("li");
    e.innerHTML = fileName;
    e.className = "list-group-item";
    const id = `list-group-item-${i}`;
    e.id = id;
    e.style = `overflow:hidden;
white-space: nowrap;
text-overflow:ellipsis;`;
    e.addEventListener("click", function () {
      fileNameOnClick(filenames[i], id);
    });
    fileNamesContainer.appendChild(e);
  }
}

function fileNameOnClick(filepath, id) {
  const fileNamesLists = document.querySelectorAll("#fileNamesContainer > li");
  for (let i = 0; i < fileNamesLists.length; i++) {
    fileNamesLists[i].classList.remove("active");
  }
  document.getElementById(id).classList.add("active");

  setActiveImage(filepath);
}

function deleteAll() {
  const fileNamesLists = document.querySelectorAll("#fileNamesContainer > li");
  for (let i = 0; i < fileNamesLists.length; i++) {
    fileNamesLists[i].remove();
  }
  const displayImage = document.getElementById("displayImage");
  const descriptionText = document.getElementById("descriptionText");

  displayImage.src = "https://via.placeholder.com/250";
  descriptionText.value = "";
}

function setActiveImage(filepath) {
  const displayImage = document.getElementById("displayImage");
  const descriptionText = document.getElementById("descriptionText");

  displayImage.src = filepath;
  descriptionText.value = tempText;
}
