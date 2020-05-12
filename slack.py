import os
from rasa.core.channels.slack import SlackInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/")
MODEL_PATH = "models/20200511-190147.tar.gz"
action_endpoint = EndpointConfig(url="https://lunachatbot-prj2-actions.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = SlackInput(
            slack_token="xoxb-1123791351716-1102879859463-UJs04nAg5DJMJDvikdPmvEl1",
            # this is the `bot_user_o_auth_access_token`
            slack_channel="#chatbot"
            # the name of your channel to which the bot posts (optional)
    )
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel],  int(os.environ.get('PORT', 5004)), serve_forever=True)
