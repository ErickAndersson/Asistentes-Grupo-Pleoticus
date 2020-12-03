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

## update path
* update_data
  - action_update