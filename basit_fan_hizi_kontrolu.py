import skfuzzy 
from skfuzzy.control import controlsystem
import numpy as np 

space = np.arange(0,101,1)

heats = controlsystem.Antecedent(space,"Heats")
speed = controlsystem.Consequent(space,"Speeds")

heats['low'] = skfuzzy.trimf(heats.universe,[0,0,20])
heats['mid'] = skfuzzy.trimf(heats.universe,[10,20,30])
heats['high'] = skfuzzy.trimf(heats.universe,[20,30,40])

speed['low'] = skfuzzy.trimf(speed.universe,[0,0,50])
speed['mid'] = skfuzzy.trimf(speed.universe,[25,50,75])
speed['high'] = skfuzzy.trimf(speed.universe,[50,100,100])

rule_1 = controlsystem.Rule(
    heats['low'],
    speed['low']
)
rule_2 = controlsystem.Rule(
    heats['mid'],
    speed['mid']
)
rule_3 = controlsystem.Rule(
    heats['high'],
    speed['high']
)

system = controlsystem.ControlSystem(rules=[rule_1,
                                     rule_2,
                                     rule_3])

heat = 25

control_system = controlsystem.ControlSystemSimulation(system)

control_system.input['Heats'] = heat

control_system.compute()

print(control_system.output['Speeds'])
