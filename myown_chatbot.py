import os
from rasa.core.channels.rasa_chat import RasaChatInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/")
MODEL_PATH = "models/20200511-190147.tar.gz"
action_endpoint = EndpointConfig(url="https://lunachatbot-prj2-actions.herokuapp.com/webhook")
agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)

class MyNewInput(RasaChatInput):
    def _check_token(self, token):
        if token == 'jackfrost':
            return {'username': 1234}
        else:
            print("Fail to check token: {}.".format(token))
            return None
        
input_channel = MyNewInput(url='https://lunachatbot-prj2.herokuapp.com')

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT',5004)))