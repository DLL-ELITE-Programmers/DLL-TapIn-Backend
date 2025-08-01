import pandas as pd
from django.db import IntegrityError
from django.test import TestCase
from rest_framework.views import APIView, Response

from Accounts.models import User
from Departments.models import Department
from Events.models import Event, Participant

# Create your tests here.


def dept():
    data = pd.read_csv("backup_data/Export/dept.csv", sep=";")
    # id;department_id;department_name
    for _, row in data.iterrows():
        deptm = Department(
            department_id=row["department_id"], department_name=row["department_name"]
        )
        deptm.save()
        print(row["department_id"])
    return Response({"message": "done"})


def event():
    data = pd.read_csv("backup_data/Export/event.csv", sep=";")
    # event_id;event_name;event_description;event_venue
    for _, row in data.iterrows():
        eve = Event(
            event_id=row["event_id"],
            event_name=row["event_name"],
            event_description=row["event_description"],
            event_venue=row["event_venue"],
        )
        eve.save()
        print(row["event_id"])
    return Response({"message": "done"})


def participants():
    # id;time_in;event_id;participant_id;time_out
    data = pd.read_csv("backup_data/Export/paticipants.csv", sep=";")
    for _, row in data.iterrows():
        part = Participant(
            time_in=pd.to_datetime(row["time_in"], errors="coerce"),
            event_id=row["event_id"],
            participant_id=row["participant_id"],
        )
        part.save()
        print(row["event_id"])
    return Response({"message": "done"})

    pass


class UserTest(APIView):
    def get(self, req):
        return participants()

        tables = [
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joinedid",
            "middle_name",
            "sex",
            "verified",
            "department_id",
        ]
        data = pd.read_csv("backup_data/Export/accounts.csv", sep=";")

        for _, row in data.iterrows():
            try:
                middle_name = ""
                if row["middle_name"] != "null":
                    middle_name = row["middle_name"]

                user = User(
                    username=row["username"],
                    # last_login=pd.to_datetime(row["last_login"], errors="coerce"),
                    is_superuser=row["is_superuser"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    is_staff=row["is_staff"],
                    is_active=row["is_active"],
                    # date_joined=pd.to_datetime(row["date_joined"], errors="coerce"),
                    id=row["id"],
                    middle_name=middle_name,
                    sex=row["sex"],
                    verified=row["verified"],
                    department_id=row["department_id"],
                )
                user.password = row["password"]
                user.save()
                print(f"Saved: {row['username']}")
            except IntegrityError as e:
                print(e)
                # return Response({"error": str(e)})
        return Response({"message": "Done"})
