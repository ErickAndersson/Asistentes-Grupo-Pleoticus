# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionGetUser(Action):

    def name(self) -> Text:
        return "action_get_users"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myobj = {
            "message": "Enviado",
            "sender": "usuario",
            "metadata":{
                "name": ""
            }
        }
        dispatcher.utter_message(json_message=myobj)
        return []

class ActionTimeRead(Action):

    def name(self) -> Text:
        return "action_time_read"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myobj = {
            "message": "Enviado",
            "sender": "usuario",
            "metadata":{"nombre":"TiempoLecturaUserStory","Items":[{"user_id": "Bruno","value": "20"},{"user_id": "Matias","value": "25"}]}
        }
        dispatcher.utter_message(json_message=myobj)
        return []

class ActionEndUserStorie(Action):

    def name(self) -> Text:
        return "action_end_user_storie"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myobj = {
            "message": "Enviado",
            "sender": "usuario",
            "metadata":{"nombre":"TiempoTrabajoUserStory","Items":[{"user_id": "Bruno","value": "20"},{"user_id": "Matias","value": "25"}]}
        }
        dispatcher.utter_message(json_message=myobj)
        return []

class ActionGetResources(Action):

    def name(self) -> Text:
        return "action_get_resources"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myobj = {
            "message": "No lo tengo",
            "sender": "usuario",
            "metadata":""
        }
        dispatcher.utter_message(json_message=myobj)
        return []

class ActionMeetParticipants(Action):

    def name(self) -> Text:
        return "action_meet_participants"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myobj = {
            "message": "Enviado",
            "sender": "usuario",
            "metadata":{"nombre":"ParticipacionesMeetings","Items":[{"user_id": "Bruno","value": "64"},{"user_id": "Matias","value": "23"}]}
        }
        dispatcher.utter_message(json_message=myobj)
        return []        