import "./global.css";
import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import { StyleSheet, Text, View } from "react-native";
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
    <View className="bg-red-500" style={styles.container}>
      <Text>Open up App.tsx to start working on your app!</Text>
      <Text>Basta miss ko na sya.</Text>
      {data.map((user: unknown, index: number) => {
        return (
          <Text>
            {user.username} - {user.last_name}, {user.first_name}
          </Text>
        );
      })}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
