import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Image,
  Alert,
} from "react-native";
import React, { useState } from "react";
import * as ImagePicker from "expo-image-picker";

const SelectImages = ({ navigation }) => {
  const [image, setImage] = useState(null);

  const pickImage = async () => {
    // No permissions request is necessary for launching the image library
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      quality: 1,
      allowsMultipleSelection: true,
    });

    setImage(result.selected);
  };

  const ViewImages = () => {
    let images = [];

    if (!image) {
      return images;
    }

    for (let i = 0; i < image.length; i++) {
      images.push(
        <Image
          key={image[i].assetId}
          style={{
            width: 50,
            height: 50,
            borderColor: "black",
            borderWidth: 1,
            margin: 10,
          }}
          source={{
            uri: image[i].uri,
          }}
        />
      );
    }

    return images;
  };

  const nextScreen = () => {
    if (image) {
      navigation.navigate("TextCleanup", { images: image });
    } else {
      Alert.alert(
        "No Image Selected",
        "Please select atleast one image\nTry again",
        [{ text: "OK", onPress: () => console.log("OK Pressed") }]
      );
    }
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity
        style={styles.button}
        activeOpacity={0.7}
        onPress={pickImage}
      >
        <Text>Upload Images</Text>
      </TouchableOpacity>
      <View style={styles.imageContainers}>
        <ViewImages />
      </View>
      <TouchableOpacity
        style={styles.button}
        activeOpacity={0.7}
        onPress={nextScreen}
      >
        <Text>Next</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "flex-start",
  },
  button: {
    padding: 40,
    borderRadius: 4,
    borderWidth: 1,
    borderColor: "green",
    backgroundColor: "lightgreen",
    elevation: 5,
    shadowColor: "black",
    marginVertical: 50,
  },
  imageContainers: {
    flex: 1,
    flexDirection: "row",
    width: "100%",
    flexWrap: "wrap",
  },
});

export default SelectImages;
