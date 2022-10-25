import { View, Text, Button } from "react-native";
import React, { useState } from "react";
import extractText from "../hooks/extractText";

const TextCleanup = ({ route, navigation }) => {
  const { images } = route.params;
  const [imagesAndText, setImagesAndText] = useState([]);

  return (
    <View>
      <Button
        title="Check"
        onPress={() => {
          extractText(images);
        }}
      >
        TextCleanup
      </Button>
    </View>
  );
};

export default TextCleanup;
