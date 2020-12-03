## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_help

## happy path
* greet
  - utter_greet
* bot_animus
  - utter_animus
  - utter_help

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_help

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_help
* deny
  - utter_goodbye

## info path
* bot_info
  - utter_info
  - utter_anything_else
* deny
  - utter_goodbye

## where am i path
* where_am_i
  - utter_location
  - utter_anything_else
* deny
  - utter_goodbye
  
## system info path
* system_info
  - utter_info_system
  - utter_anything_else
* deny
  - utter_goodbye

## where_to_go
* where_to_go
  - utter_where_to_go
  - utter_anything_else
* deny
  - utter_goodbye
  
## how to play path
* how_to_play
  - utter_how_to_play  
  - utter_anything_else
* deny
  - utter_goodbye

## take break
* task_finished
  - action_tarea_finalizada

## progress path
* how_to_progress
  - action_get_tarea
  - utter_anything_else
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## daily_scrum path
* daily_scrum
  - utter_daily1
  - utter_daily2
  - utter_anything_else
* deny
  - utter_goodbye

## scrum_works path
* scrum_works
  - utter_scrum_works
  - utter_anything_else
* deny
  - utter_goodbye

## product_backlog path
* product_backlog
  - utter_product_backlog
  - utter_anything_else
* deny
  - utter_goodbye

## sprint_backlog path
* sprint_backlog
  - utter_sprint_backlog
  - utter_anything_else
* deny
  - utter_goodbye

## sprint_review path
* sprint_backlog
  - utter_sprint_backlog
  - utter_anything_else
* deny
  - utter_goodbye

## scrum_master path
* scrum_master
  - utter_scrum_master
  - utter_anything_else
* deny
  - utter_goodbye

## product_owner path
* product_owner
  - utter_product_owner
  - utter_anything_else
* deny
  - utter_goodbye

## sprint_planning path
* sprint_planning
  - utter_sprint_planning
  - utter_anything_else
* deny
  - utter_goodbye

## sprint_retrospective path
* sprint_retrospective
  - utter_sprint_retrospective
  - utter_anything_else  
* deny
  - utter_goodbye

## thanks path
* thanks
  - utter_thanks  
  
## task_description path
* task_description
  - action_descripcion_tarea
  
## task_story_points path
* task_story_points
  - utter_prueba_task_story_points

## task_priority path
* task_priority
  - action_prioridad_tarea

## aviso_reunion path
* aviso_reunion
  - utter_aviso_reunion

## inicio_reunion path
* inicio_reunion
  - utter_inicio_reunion

## descansar path
* descansar
  - utter_descansar  

## trabajo path
* trabajo
  - utter_trabajo

## evento_reunion path
* evento_reunion
  - action_evento

## evento_trabajo path
* evento_trabajo
  - action_evento

## evento_descanso path
* evento_descanso
  - action_evento

## daily_sin_problemas path
* permiso_hablar
  - action_permiso_hablar
  - utter_primera_pregunta_daily
* respuesta_daily_pasado
  - utter_segunda_pregunta_daily
* respuesta_daily_presente
  - utter_tercera_pregunta_daily 
* respuesta_negativa
  - utter_finalizo_bien
  - utter_termino

## daily_con_problemas path
* permiso_hablar
  - action_permiso_hablar
  - utter_primera_pregunta_daily
* respuesta_daily_pasado
  - utter_segunda_pregunta_daily
* respuesta_daily_presente
  - utter_tercera_pregunta_daily 
* respuesta_positiva
  - utter_finalizo_mal
  - utter_termino

## daily_con_problemas_2 path
* permiso_hablar
  - action_permiso_hablar
  - utter_primera_pregunta_daily
* respuesta_daily_pasado
  - utter_segunda_pregunta_daily
* respuesta_daily_presente
  - utter_tercera_pregunta_daily 
* affirm
  - utter_preguntar_problema
* respuesta_positiva
  - utter_finalizo_mal  
  - utter_termino