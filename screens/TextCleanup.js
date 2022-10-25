import { View, Text } from "react-native";
import React from "react";

const TextCleanup = ({ route, navigation }) => {
  const { images } = route.params;

  return (
    <View>
      <Text>TextCleanup</Text>
    </View>
  );
};

export default TextCleanup;
