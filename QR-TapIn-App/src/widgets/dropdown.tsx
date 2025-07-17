import { Text, View } from "react-native";
import { Dropdown } from "react-native-element-dropdown";

interface spinner {
  label: string;
  data: unknown;
  valueField: string;
  labelField: string;
  name?: string;
}

export default function Spinner(props: spinner) {
  const capitalized = (text: string) => {
    text = text.replace(/_/g, " ");
    return text[0].toUpperCase() + text.substring(1);
  };

  const name = props.name
    ? props.name
    : props.label.replace(/\s/gi, "_").toLowerCase();

  return (
    <View className={`w-full`}>
      <Text className="text-sm">{capitalized(props.label)}</Text>
      <Dropdown
        id={name}
        data={props.data}
        valueField={props.valueField}
        labelField={props.labelField}
        className="border-[2px] border-black/50 focus:border-[#60affe] rounded-[5px]"
      />
    </View>
  );
}
