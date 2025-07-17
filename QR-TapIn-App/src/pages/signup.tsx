import { Switch, Text, View } from "react-native";
import Input from "../widgets/input";
import Btn from "../widgets/button";
import Spinner from "../widgets/dropdown";
import { useEffect, useState } from "react";
import { get_unauth } from "../../utils/access";

interface dept {
  department_id: string;
  department_name: string;
}

export default function SignUp() {
  const [department, setDepartment] = useState<dept[]>([
    {
      department_name: "Test",
      department_id: "HIHI",
    },
  ]);

  useEffect(() => {
    (async () => {
      const response = await get_unauth("department");
      // const transformedArray = response.map((obj) => {
      //   // Create a new object to avoid modifying the original directly
      //   const newObj = { ...obj };
      //
      //   // Check if the old key exists in the current object
      //   if (newObj.hasOwnProperty("department_id")) {
      //     // Assign the value of the old key to the new key
      //     newObj["value"] = newObj["deparment_id"];
      //     newObj["label"] = newObj["department_name"];
      //     // Delete the old key
      //     delete newObj["department_id"];
      //     delete newObj["department_name"];
      //   }
      //   return newObj;
      // });
      setDepartment(response);
    })();
  }, []);

  return (
    <View className="flex-1 justify-center items-center p-4">
      <View className="gap-2 w-full px-10 bg-slate-200 items-center justify-center p-4 rounded-md">
        <Text className="text-3xl font-bold">Sign Up</Text>
        <Text>Don't have an account yet?</Text>{" "}
        <Text className="underline">Baka di pa pa talaga nag eexists</Text>
        <Spinner
          data={department}
          valueField="department_name"
          labelField="department_name"
          label="Department"
        />
        <Input label="First Name" />
        <Input label="Middle Name" />
        <Input label="Last Name" />
        <Input label="Email" />
        <Input label="Password" password={true} />
        <View className="flex flex-row justify-between items-center w-full">
          <View className="flex flex-row items-center">
            <Switch value={false} />
            <Text>Remember me</Text>
          </View>
        </View>
        <Btn>Log in</Btn>
      </View>
    </View>
  );
}
