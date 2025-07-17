import "./global.css";
import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import { Text, View, StatusBar as sb } from "react-native";
import { get, get_unauth } from "./utils/access";
import Page from "./src/pages";

export default function App() {
  // const [data, setData] = useState<unknown[]>([]);
  // useEffect(() => {
  //   (async () => {
  //     const response = await get_unauth("api/users");
  //     setData(response);
  //   })();
  // }, []);

  console.log(Math.round(sb.currentHeight));

  return (
    <View className="flex flex-col bg-[#fff] w-full h-full">
      <StatusBar style="auto" />
      {/* NOTE: mt-[30px] was the one who created the gap for the statusbar */}
      <View
        className={`bg-slate-500 android:mt-[30px] ios:mt-[30px] w-full h-full flex-1 items-center justify-center`}
      >
        {/* <Text>Open up App.tsx to start working on your app!</Text>
        <Text>Basta miss ko na sya.</Text>
        {data.map((user: unknown, index: number) => {
          return (
            <Text key={index}>
              {user.username} - {user.last_name}, {user.first_name}
            </Text>
          );
        })}
        */}
        <Page />
      </View>
    </View>
  );
}
