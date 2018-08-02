import sys
sys.dont_write_bytecode = True

import sys
import agent
import environment as env
import tensorflow as tf
import hyperparameters.setups as setups

game = 'CarRacing'

environment = env.env_dict[game](type="TwoCurve", seed=5)
control = agent.DQN_Agent(environment=environment, model_name=sys.argv[1], **setups.setup_dict[game]['general'])
control.set_training_parameters(**setups.setup_dict[game]['training'])
control.train()
# control.load("/phome/pgerber/Documents/RL-2018/src/DQN_Agent/models/Car_TwoCurve/data.chkp-540")
print(control.test_Q(5, visualize=True))