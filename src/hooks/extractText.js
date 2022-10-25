import { useState, useEffect } from "react";
import TextRecognition from "@react-native-ml-kit/text-recognition";

const extractText = async (listOfImages) => {
  console.log(listOfImages);
  //   const [imagesAndTexts, setImagesAndTexts] = useState([]);

  //   await worker.load();
  //   await worker.loadLanguage("eng");
  //   await worker.initialize("eng");
  //   const url =
  //     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Lorem_ipsum_flush_justified.svg/1280px-Lorem_ipsum_flush_justified.svg.png";
  //   for (let i = 0; i < listOfImages.length; i++) {
  //     const data = await worker.recognize(url);
  //     // listOfImages[i].uri;
  //   }
  //   console.log(data);
  //   await worker.terminate();

  for (let i = 0; i < listOfImages.length; i++) {
    console.log(listOfImages[i].uri);
    const data = await TextRecognition(listOfImages[i].uri);
    console.log("data");
    console.log(data);
    // listOfImages[i].uri;
  }

  return imagesAndTexts;
};

export default extractText;
