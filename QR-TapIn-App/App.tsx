import "./global.css";
import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import { Text, View } from "react-native";
import { get, get_unauth } from "./utils/access";

export default function App() {
  const [data, setData] = useState<unknown[]>([]);
  useEffect(() => {
    (async () => {
      const response = await get_unauth("api/users");
      setData(response);
    })();
  }, []);
  return (
    <View className="flex flex-col bg-[#fff] w-full h-full">
      <StatusBar style="auto" />
      {/* NOTE: mt-[30px] was the one who created the gap for the statusbar */}
      <View className="bg-slate-400 mt-[30px] w-full h-full flex-1 items-center justify-center">
        <Text>Open up App.tsx to start working on your app!</Text>
        <Text>Basta miss ko na sya.</Text>
        {data.map((user: unknown, index: number) => {
          return (
            <Text key={index}>
              {user.username} - {user.last_name}, {user.first_name}
            </Text>
          );
        })}
      </View>
    </View>
  );
}
