import matplotlib.pyplot as plt
import numpy as np
from elliptic_pendulum import *
import json
from plot import *

# import constants from config.json
with open('config.json') as f:
    consts = dict(json.load(f))

# calc derived quantities
consts['omega0'] = np.sqrt(consts['g'] / consts['l']) # angular frequency for 2D small angle pendulum
consts['T'] = 2 * np.pi / consts['omega0'] # period of the small angle 1D pendulum

row = len(consts['Omega0'])
tSpan = np.linspace(0, consts['numOfPeriods'] * consts['T'], 10000)

fig, axs = plt.subplots(row, 3, figsize=(9, 9))
for i in range(row):
    Omega0 = consts['Omega0'][i]
    thetaEval = solver2(theta_double_dot, consts['theta0'], consts['theta_dot0'], tSpan, Omega0, consts['omega0'])
    phiEval = solver1(phi_dot(thetaEval, Omega0), consts['phi0'], tSpan)
    color = colorsys.hsv_to_rgb(i/row, 1, 1)
    threeInOne(thetaEval, phiEval, tSpan, axs[i], Omega0, consts['l'], color)

plt.show()
plt.savefig('output/plot.png')
