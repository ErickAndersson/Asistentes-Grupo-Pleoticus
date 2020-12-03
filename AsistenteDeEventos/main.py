
import json
import requests

url = 'https://botdisenio.herokuapp.com/webhooks/my_connector/webhook/' ##change rasablog with your app name

url2 = 'https://asistente-eventos.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name

def response(mensaje,datos):
    myobj = {
    "message": str(mensaje),
    "sender": "usuario",
    "metadata":{
                "name": str(datos)
            }
    }
    request_response = requests.post(url, json = myobj)
    return request_response

respuesta=response("hi",None).text
respuesta=json.loads(respuesta)
respuesta=respuesta[0]['text']
while(respuesta!='Ok'):
    print(respuesta)
    myobj = {
    "message": respuesta,
    "sender": "bot",
    }
    respuesta_2=requests.post(url2,json=myobj).text
    respuesta_2=json.loads(respuesta_2)
    print(respuesta_2)
    respuesta=response(respuesta_2[0]['custom']['message'],respuesta_2[0]['custom']['metadata']).text
    respuesta=json.loads(respuesta)
    respuesta=respuesta[0]['text']
