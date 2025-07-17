import { ReactNode } from "react";
import { Button, View } from "react-native";

interface button {
  children: string;
  onclick?: void;
}
export default function Btn(props: button) {
  return (
    <Button
      className="bg-blue-500 rounded-md w-full flex-1"
      onPress={() => {
        props.onclick;
      }}
      title={props.children}
    />
  );
}
