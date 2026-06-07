import skfuzzy as skf
from skfuzzy.control import controlsystem as ctrls
import numpy as np 
import matplotlib.pyplot as plt 

vector = np.arange(0,101,1)

Input = ctrls.Antecedent(vector,'Heats')

Input.automf(3)

for name,term in Input.terms.items():
    mF = term.mf

    x = Input.universe

    print(x[np.argmax(mF)])
