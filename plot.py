
import matplotlib.pyplot as plt
import colorsys
from numpy import *
from elliptic_pendulum import projection


def theta_t(tSpan, thetaEval, ax, Omega0, color='b'):
    ax.plot(tSpan, thetaEval, color=color)

    # set label
    ax.set_xlabel('t', fontsize=8)
    ax.set_ylabel('theta', fontsize=8)

    # set tick size
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    ax.set_title('Omega0 = ' + str(Omega0), fontsize=8)

def phi_t(tSpan, phiEval, ax, Omega0, color='b'):
    ax.plot(tSpan, phiEval, color=color)

    # set label
    ax.set_xlabel('t', fontsize=8)
    ax.set_ylabel('phi', fontsize=8)

    # set tick size
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    ax.set_title('Omega0 = ' + str(Omega0), fontsize=8)


def x_y(x, y, ax, Omega0, color='b'):
    ax.plot(x, y, color=color)

    # set limits
    lim = max(abs(x).max(), abs(y).max()) * 1.1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    # set label
    ax.set_xlabel('x', fontsize=8)
    ax.set_ylabel('y', fontsize=8)

    # set tick size
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    ax.set_title('Omega0 = ' + str(Omega0), fontsize=8)


def threeInOne(thetaEval, phiEval, tSpan, axs, Omega0, l, color='b'):
    # calc x and y
    x, y = projection(thetaEval, phiEval, l)
    # plot 3 graphs in 1 row
    theta_t(tSpan, thetaEval, axs[0], Omega0, color)
    phi_t(tSpan, phiEval, axs[1], Omega0, color)
    x_y(x, y, axs[2], Omega0, color)