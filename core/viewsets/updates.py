from rest_framework.response import Response
from rest_framework.views import APIView


class UpdatesAPI(APIView):
    def get(self, req):
        return Response(
            {
                "message": "The application was now on its urge.",
                "version": "0.1.1",
                # NOTE: This key gives the user to know what are the changes from different versions
                "new": {
                    # INFO: Please make the logs as this format, to prevent the misinformation
                    # Just add another version name below for additional changes.
                    "0.1.1": [
                        "Fixed Changelogs Issue",
                        "Fixed Remember Me Issue",
                        "Added Offline mode",
                        "Fixed Terms and Condition",
                        "Added Auto update",
                        "Fixed typo [department -> sex]",
                        "Added signup information verification",
                        "Added Student ID verification",
                        "Student ID Auto format [to prevent student id unformat]",
                    ],
                    "0.1.0": ["Initial Release", "Pilot Test to BSIT Dept"],
                    "0.0.1": ["flag{Di_ko_alam_kung_gusto_pa_nya_ako}"],
                },
                "link": "https://expo.dev/artifacts/eas/a1pCM5uQPNExs8VBW74pc9.apk",
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
