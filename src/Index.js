import { NavigationContainer } from "@react-navigation/native";
import { StyleSheet } from "react-native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import SelectAudio from "./screens/SelectAudio";
import SelectBackgroundVideo from "./screens/SelectBackgroundVideo";
import SelectImages from "./screens/SelectImages";
import TextCleanup from "./screens/TextCleanup";

const Stack = createNativeStackNavigator();

const Index = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="SelectImages"
          component={SelectImages}
          options={{ title: "Select Images" }}
        />
        <Stack.Screen
          name="TextCleanup"
          component={TextCleanup}
          options={{ title: "Clean up text" }}
        />
        <Stack.Screen
          name="SelectBackgroundVideo"
          component={SelectBackgroundVideo}
          options={{ title: "Select Background Video" }}
        />
        <Stack.Screen
          name="SelectAudio"
          component={SelectAudio}
          options={{ title: "Select Audio" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});

export default Index;
