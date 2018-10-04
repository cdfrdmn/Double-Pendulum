# @author: Callum Friedman

from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt


grav = 9.81

def doublePendulum(length, theta1, theta2, tmax):

    start       = 0.0 # start time
    end         = tmax # time for simulation to run for
    steps       = 100000 # the number of time steps
    stepsize    = (end - start)/steps # the interval between each calculation
    omega1      = 0.0 # initial angular velocity of theta1
    omega2      = 0.0 # initial angular velocity of theta2

    # Get set of equidistant time points
    tpoints = np.arange(start, end, stepsize)

    # prepare lists to keep resulting positions and velocities
    omega1points    = []
    omega2points    = []
    theta1points    = []
    theta2points    = []

    def omega1_prime(omega1, omega2, theta1, theta2):
        # 1st order differential eqn for the ANGULAR VELOCITY of the UPPER pendulum
        dif = theta1 - theta2
        return (-omega1**2*np.sin(dif)*cos(dif)-omega2**2*sin(dif)-grav/length*(+2*sin(theta1)-sin(theta2)*cos(dif)))/(2-(cos(dif))**2)

    def omega2_prime(omega1, omega2, theta1, theta2):
        # 1st order differential eqn for the ANGULAR VELOCITY of the LOWER pendulum
        dif = theta1 - theta2
        return (0.5*omega2**2*sin(dif)*cos(dif)+omega1**2*sin(dif)+ grav/length*(sin(theta1)*cos(dif)-sin(theta2)))/(1-0.5*cos(dif)**2)

    for t in tpoints:

        omega1points.append(omega1)
        omega2points.append(omega2)
        theta1points.append(theta1)
        theta2points.append(theta2)

        omega1 += stepsize*omega1_prime(omega1, omega2, theta1, theta2)
        omega2 += stepsize*omega2_prime(omega1, omega2, theta1, theta2)
        theta1 += stepsize * omega1
        theta2 += stepsize * omega2

    plt.plot(tpoints, theta1points)
    plt.plot(tpoints, theta2points)
    plt.ylabel('Angle (rad)')
    plt.xlabel('Time (s)')
    plt.title('Position of Double Pendulum')
    plt.savefig('Angle.pdf')
    plt.show()

    plt.plot(tpoints, omega1points)
    plt.plot(tpoints, omega2points)
    plt.ylabel('Angular Velocity (rad/s)')
    plt.xlabel('Time (s)')
    plt.title('Angular Velocity of Double Pendulum')
    plt.savefig('Angular velocity.pdf')
    plt.show()
