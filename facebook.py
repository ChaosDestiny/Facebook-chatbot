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
interpreter = RasaNLUInterpreter("models/nlu/")
MODEL_PATH = "models/20200512-212705.tar.gz"
action_endpoint = EndpointConfig(url="https://lunachatbot-prj2-actions.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)
input_channel = FacebookInput(
    fb_verify="jackfrost",
    # you need tell facebook this token, to confirm your URL
    fb_secret="4ad8cdf285aeef2548b23c130cd6f56c", # your app secret
    fb_access_token="EAASmSto8E9IBAABZBgqhtuXkyV2PoCrxVoQoG2FsQC5HagM97IZA7KuQzZC48xKC7sIYPT2OZBsM2sY3bxN0RZCUutVU6g4TF8Ow5uaRq64tv6axkHuDxLVZBpTaRS95qEMhIkHnixIaIU5Ql9weuYuXOxlZAreqScqjq7AkrYwLwZDZD"
    
    # token for the page you subscribed to
)
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT',5004)))