import { Text, View } from "react-native";
import Login from "./login";
import SignUp from "./signup";

export default function Page() {
  return (
    <View className="flex-1 w-full h-full">
      {/* TODO: To manage all things we need to manage in. */}
      <SignUp />
    </View>
  );
}
