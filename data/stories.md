## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## play music
* greet
    - utter_greet
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    
## play music 2
* greet
    - utter_greet
* play_music{"song": "Con cò bé bé"}
    - slot{"song": "Con cò bé bé"}
    - action_play_music
* goodbye
    - utter_goodbye
    
## tell story
* greet
    - utter_greet
* tell_story{"story": "Thạch Sanh"}
    - slot{"story": "Thạch Sanh"}
    - action_tell_story
    
## tell story
* greet
    - utter_greet
* tell_story{"story": "Tấm cám"}
    - slot{"story": "Tấm cám"}
    - action_tell_story
* goodbye
    - utter_goodbye