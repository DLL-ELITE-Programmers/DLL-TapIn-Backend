import { Text, TextInput } from "react-native";
import { View } from "react-native";

interface input {
  name: string;
  password?: boolean;
  hint?: string;
}

export default function Input(props: input) {
  const capitalized = (text: string) => {
    text = text.replace(/_/g, " ");
    return text[0].toUpperCase() + text.substring(1);
  };

  return (
    <View className={`w-full`}>
      <Text className="text-sm">{capitalized(props.name)}</Text>
      <TextInput
        placeholder={props.hint}
        secureTextEntry={props.password ?? false}
        className="border-[2px] border-black/50 focus:border-[#60affe] rounded-[5px]"
      />
    </View>
  );
}
