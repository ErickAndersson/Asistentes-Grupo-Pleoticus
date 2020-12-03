import requests
import json
'''
url = 'https://asistente-comp.herokuapp.com/webhooks/rest/webhook'
#url= 'https://diseno2020.herokuapp.com/api/jira/user/issues?username=farodriguez@alumnos.exa.unicen.edu.ar' ##change rasablog with your app name
myobj = {
    "sender":"farodriguez@alumnos.exa.unicen.edu.ar",
    "message":"que debo hacer ahora?",
}

x = requests.post(url, json=myobj)

print(x.text)

for issue in tarea:
    if issue['status.name']=='to do':
        print(issue['status']['name'])
        break
print(tarea)
'''
url = 'https://diseno2020.herokuapp.com/api/jira/user/issues?username=viviantjuaneliel@gmail.com'
x = requests.get(url)


y = json.loads(x.text)

tareas = y['issues']

print(tareas[0]['fields']['summary'])
print(tareas[0]['fields']['description'])
print(tareas[0]['fields']['project']['name'])
print(tareas[0]['fields']['status']['name'])

            
