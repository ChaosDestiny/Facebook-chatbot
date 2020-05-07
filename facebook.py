# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:40:40 2020

@author: hung.td170078
"""


from rasa.core.channels.facebook import FacebookInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import os
from rasa.core.utils import EndpointConfig
# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu")
MODEL_PATH = "models/core"
action_endpoint = EndpointConfig(url="https://luna-chatbot-prj2.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter)
input_channel = FacebookInput(
    fb_verify="jackfrost",
    # you need tell facebook this token, to confirm your URL
    fb_secret="4ad8cdf285aeef2548b23c130cd6f56c", # your app secret
    fb_access_token="EAASmSto8E9IBAKxskZCOy6SrnRvEQHCAXzZBw2XGMRcv2kA4mj8GFwEUKtlREYgd6Fmx8YtLpZAAZBmnMRVDxUgNvA3JO4TZBs7ZAtbnJab6mcCp7prVfEk6aZCNwlLs4DdCZBRH8Fo3J0qvq73icLhFWKjxcEAGI9TElWuXGNQHiwZDZD"
    # token for the page you subscribed to
)
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT',5004)), serve_forever=True)