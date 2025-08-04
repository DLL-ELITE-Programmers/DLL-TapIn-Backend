from rest_framework.response import Response
from rest_framework.views import APIView


class UpdatesAPI(APIView):
    def get(self, req):
        return Response(
            {
                "message": "Thie update was created for test",
                "version": "0.1.1",
                # NOTE: This key gives the user to know what are the changes from different versions
                "new": {
                    "0.1.1": [
                        "Walang bago, ikaw pa rin",
                        "Added Auto update",
                        "Fixed typo [department -> sex]",
                        "Added signup information verification",
                        "Added Student ID verification",
                        "Added some buttons [for test]",
                    ]
                },
                "link": "https://expo.dev/artifacts/eas/8oazocEofsg4jBBnkzfSuB.apk",
                # NOTE: This key is very important for future updates
                # TODO: Just add one if the update is required to the specific version
                # given to the application. This is to make the least version of require
                # version, meaning, not the actual version but only the required version
                "require": -1,
            }
        )


class TermsAndCondition(APIView):
    def get(self, req):
        return Response(
            {
                "message": "success",
                "terms": {
                    "intro": "DLL TapIn is an attendance monitoring system developed under DLL BSIT Department. We (as developers) wanted to know you as you use this application, you're agreed with our terms and conditions, as well as how we use the data and information gather from the application",
                    "sub": {
                        "Liability": "We (the developers) are the liable once all the information are leaked, but we are not the liable one once your account was hacked. It's everyone's responsible to also protect their own as their own security",
                        "Data Gathering": "We (as developers) wanted you to know that the we gather data to monitor each activities for improvement, this is to let know the organizers (organization officers) how do they improve an event they created. Also we use the data for statistical studies, such as which course, year and section, as well as organizations are active in each events.",
                        "End-User Agreement": "You (as student) must know these terms as you must not have complains regarding to the information given.",
                        "Feedback": "Any kind of problem, issues, as well as the design problem must be reported as part of the development. We will value your insights and suggestions. We prefer to gather negative feedback, but use appropiate words and prevent vulgar words.",
                        "Staffs": "You (as event organizer, administrator, adviser) must know what must be done by the attendees (students). Don't use the system for non-ethical purpose.",
                    },
                },
            }
        )
