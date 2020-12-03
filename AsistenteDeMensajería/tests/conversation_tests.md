#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hola
  - utter_greet
* mood_great: bien
  - utter_happy

## happy path 2
* greet: hola
  - utter_greet
* mood_great: excelente
  - utter_happy
* goodbye: chau
  - utter_goodbye

## sad path 1
* greet: buen dia
  - utter_greet
* mood_unhappy: mal
  - utter_cheer_up
  - utter_did_that_help
* affirm: si
  - utter_happy

## sad path 2
* greet: buenas tardes
  - utter_greet
* mood_unhappy: no muy bien
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## sad path 3
* greet: hola
  - utter_greet
* mood_unhappy: muy mal
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## say goodbye
* goodbye: chau!
  - utter_goodbye


## happy path
* greet: hola
  - utter_greet
* bot_animus: bien y vos?
  - utter_animus
  - utter_help