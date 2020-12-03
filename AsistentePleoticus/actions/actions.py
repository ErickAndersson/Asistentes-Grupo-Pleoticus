# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,AllSlotsReset
from rasa_sdk.events import UserUtteranceReverted
import requests
import json


# Tareas por hacer  = To do
# En curso          = In progress
# Finalizada        = Done
class ActionGetTarea(Action):

    def name(self) -> Text:
        return "action_get_tarea"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tiene_tarea = tracker.get_slot('tarea')
        sender = tracker.sender_id
        if not tiene_tarea:
            sender = tracker.sender_id
            url = 'https://diseno2020.herokuapp.com/api/jira/user/issues?username='+sender
            x = requests.get(url)
            y = json.loads(x.text)
            tareas = y['issues']
            tarea=''
            if len(tareas) != 0: #pedir tarea y que no haya ninguna
                for i in range(0,len(tareas)):
                    if tareas[i]['fields']['status']['name']=='Tareas por hacer': 
                        descripcion = tareas[i]['fields']['description']
                        prioridad = tareas[i]['fields']['priority']['name']
                        switcher = {
                            "Low"    :  "Baja",
                            "Medium" :  "Media",
                            "High"   :  "Alta",
                            "Highest":  "Muy alta"
                        }
                        prioridad = switcher.get(prioridad)
                        dispatcher.utter_message(text = tarea)
                        return [SlotSet('tarea', True),SlotSet('cantidad_tareas',tracker.get_slot('cantidad_tareas')+1.0),SlotSet('descripcion_tarea',descripcion),SlotSet('prioridad_tarea',prioridad)]
                if tarea=='':
                    dispatcher.utter_message(text='No tengo tareas pendientes para asignarte, podés descansar')
            else:
                dispatcher.utter_message(text='No tenés tareas asignadas')
            
            return []
        else:
            ##tomar tarea en progreso
            dispatcher.utter_message(text="Ya tenés una tarea asignada, si la terminaste, avisame")
            return []



class ActionTareaFinalizada(Action):

    def name(self) -> Text:
        return "action_tarea_finalizada"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tiene_tarea = tracker.get_slot('tarea')
        if tiene_tarea:
            cantidad_tareas = tracker.get_slot('cantidad_tareas')
            if cantidad_tareas > 1.0:
                dispatcher.utter_message(text='Tomate un descanso, en un rato volvé')
                return [AllSlotsReset()]
            else:
                dispatcher.utter_message(text='Buenisimo, seguí asi')
                return [SlotSet('tarea', False)]
        else:
            dispatcher.utter_message(text="No tenés ninguna tarea asignada, podés pedirme una")
            return []


class ActionDescripcionTarea(Action):

    def name(self) -> Text:
        return "action_descripcion_tarea"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tiene_tarea = tracker.get_slot('tarea')
        if tiene_tarea:
            dispatcher.utter_message(text = tracker.get_slot('descripcion_tarea'))
        else:
            dispatcher.utter_message(text='No tenés una tarea asignada')
        return []


class ActionPrioridadTarea(Action):

    def name(self) -> Text:
        return "action_prioridad_tarea"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tiene_tarea = tracker.get_slot('tarea')
        if tiene_tarea:
            dispatcher.utter_message(text = 'La prioridad de tu tarea es '+tracker.get_slot('prioridad_tarea'))
        else:
            dispatcher.utter_message(text='No tenés una tarea asignada')
        return [] 


class ActionPermisoHablar(Action):

    def name(self) -> Text:
        return "action_permiso_hablar"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender = tracker.sender_id
        dispatcher.utter_message(text = '!p_' + sender + ' es tu turno de hablar')
        return []         


class ActionEvento(Action):

    def name(self) -> Text:
        return "action_evento"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dia = tracker.get_slot('dia')
        horas = tracker.get_slot('horas')
        duracion = tracker.get_slot('duracion')
    
        if duracion != "None" and "hora" in duracion:        
            switcher = {
                    "una hora" : "60",
                    "dos horas" : "120",
                    "tres horas" : "180",
                    "cuatro horas" : "240",
                    "1 hora" : "60",
                    "2 horas" : "120",
                    "3 horas" : "180",
                    "4 horas" : "240"
                    }            
            duracion = switcher.get(duracion)
        
        if duracion != "None" and "minuto" in duracion:   
            switcher = {
                    "un" : "1",
                    "dos" : "2",
                    "tres" : "3",
                    "cuatro" : "4",
                    "cinco" : "5",
                    "seis" : "6",
                    "siete" : "7",
                    "ocho" : "8",
                    "nueve" : "9"
                    }   
            duracion = duracion.replace(" minutos", "")  
            duracion = duracion.replace(" minuto", "")
            duracion = switcher.get(duracion, duracion)

        horas = horas.replace("h","")  # para cuando toma por ejemplo: a las 11h
        if horas != "None" and len(horas)>2 and not ":" in horas:        
            switcher = {
                    "ocho" : "08:00",
                    "nueve" : "09:00",
                    "una" : "13:00",
                    "dos" : "14:00",
                    "tres" : "15:00",
                    "cuatro" : "16:00",
                    "cinco" : "17:00",                        
                    "seis" : "18:00"
                    }            
            horas = switcher.get(horas)
        
        if horas != "None" and len(horas)<2 and not ":" in horas:
            switcher = {
                    "1" : "13:00",
                    "2" : "14:00",
                    "3" : "15:00",
                    "4" : "16:00",
                    "5" : "17:00",
                    "6" : "18:00",
                    "7" : "19:00",                        
                    "8" : "20:00",
                    "9" : "21:00"           
                    }            
            horas = switcher.get(horas)    

        if ":" in horas:
            switcher = {
                    "01" : "13",
                    "02" : "14",
                    "03" : "15",
                    "04" : "16",
                    "05" : "17",
                    "06" : "18"
                    }
            hora = horas[:2]
            horas = str(switcher.get(hora, hora)) + horas[2:]
        else:
            if horas != "None":
                horas = horas + ":00"                
                    
        dispatcher.utter_message(text= '!c_evento:' + tracker.get_slot('evento') + '_dia:' + dia + '_horario:' + horas + '_duracion:' + duracion)            
        return[SlotSet('evento', "None"),SlotSet('dia', "hoy"),SlotSet('horas', "None"),SlotSet('duracion', "None")]



class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_default", tracker,
                                  silent_fail=True)

        return [UserUtteranceReverted()]


 
