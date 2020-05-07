# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import webbrowser
import urllib.request
from bs4 import BeautifulSoup

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionPlayMusic(Action):
    
    def name(self) -> Text:
        return "action_play_music"
    
    def url_search(self, search_string, max_search):
        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
        url = 'https://www.youtube.com' + vid['href']          
        return url
    
    def run(self, dispatcher, tracker, domain):
        
        song = tracker.get_slot('song')
        if (song != None):
            query = urllib.parse.quote(song)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
            url = 'https://www.youtube.com' + vid['href']
            webbrowser.open(url)
            dispatcher.utter_message(text="Here your are.")
        else:
            dispatcher.utter_message(text="What song do you want to listen to?")
        return [SlotSet("song", None)]
