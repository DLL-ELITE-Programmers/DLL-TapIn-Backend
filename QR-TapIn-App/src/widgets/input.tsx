import { Text, TextInput } from "react-native";
import { View } from "react-native";

interface input {
    name: string
}

export default function Input(props: input){
    const capitalized = (text: string) => {
        return text[0].toUpperCase() + text.substring(1)
    }
    return (
        <View className={`w-full`}>
            <Text className="text-sm">{capitalized(props.name)}</Text>
            <TextInput className="border-[2px] border-[#60affe] rounded-[5px]" />
        </View>
    )
}