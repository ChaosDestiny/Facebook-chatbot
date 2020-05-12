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
  - utter_suggest_song
* deny
  - utter_goodbye
  
## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_suggest_song
* affirm
    - action_play_music
* play_music{"song": "1 phút"}
    - slot{"song": "1 phút"}
    - action_play_music
    - utter_did_that_help
* affirm
    - utter_happy

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
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ask_play_again
    
## play music 2
* greet
    - utter_greet
* play_music{"song": "Con cò bé bé"}
    - slot{"song": "Con cò bé bé"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* goodbye
    - utter_goodbye
 
## play music 3
* greet
    - utter_greet
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* deny
    - utter_goodbye

## play music 4
* play_music
    - action_play_music
* play_music{"song": "Fly away"}
    - slot{"song": "Fly away"}
    - action_play_music
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ask_play_again
* affirm
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action   
    
## play music 5
* greet
    - utter_greet
* play_music{"song": "Faded"}
    - slot{"song": "Faded"}
    - action_play_music
    - utter_ask_play_again
* deny
    - utter_ask_action
* tell_story
    - action_tell_story
* tell_story{"story": "Cô bé lọ lem"}
    - slot{"story": "Cô bé lọ lem"}
    - action_tell_story
    
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