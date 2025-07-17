import { Text, View } from "react-native";
import Input from "../widgets/input";

export default function Login() {
  return (
    <View className="flex-1 justify-center items-center">
      <Text className="text-[2rem]">QR Tap In</Text>
      <Input name="username" />
    </View>
  );
}
