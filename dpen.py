# @author: Callum Friedman

from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt


grav = 9.81

def doublePendulum(mass1, mass2, len1, len2, theta1, theta2, tmax):

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

    def omega1_prime(mass1, mass2, len1, len2, omega1, omega2, theta1, theta2):
        # 1st order differential eqn for the angular velocity of the UPPER pendulum
        dif = theta1 - theta2

        numerator   = -(grav*((2*mass1)+mass2)*sin(theta1)) - (mass2*grav*sin(theta1 - (2*theta2))) - (2*sin(dif)*mass2*(((omega2**2)*len2) + ((omega1**2)*len1*cos(dif))))
        denominator = len1*((2*mass1) + mass2 - (mass2*(cos((2*theta1) - (2*theta2)))))

        omega1prime = numerator/denominator

        return omega1prime

    def omega2_prime(mass1, mass2, len1, len2, omega1, omega2, theta1, theta2):
        # 1st order differential eqn for the angular velocity of the LOWER pendulum
        dif = theta1 - theta2

        numerator   = 2*sin(dif)*(((omega1**2)*len1*(mass1+mass2)) + (grav*(mass1+mass2)*cos(theta1)) + ((omega2**2)*len2*mass2*cos(dif)))
        denominator = len2*((2*mass1) + mass2 - (mass2*cos((2*theta1) - (2*theta2))))

        omega2prime = numerator/denominator

        return  omega2prime

    for t in tpoints:

        omega1points.append(omega1)
        omega2points.append(omega2)
        theta1points.append(theta1)
        theta2points.append(theta2)

        omega1 += stepsize*omega1_prime(mass1, mass2, len1, len2, omega1, omega2, theta1, theta2)
        omega2 += stepsize*omega2_prime(mass1, mass2, len1, len2, omega1, omega2, theta1, theta2)
        theta1 += stepsize * omega1
        theta2 += stepsize * omega2

    plt.figure(figsize=(12,6))

    plt.subplot(2, 1, 1)
    plt.plot(tpoints, theta1points, label='Upper')
    plt.plot(tpoints, theta2points, label='Lower')
    plt.ylabel('Angle (rad)')
    plt.xlabel('Time (s)')
    plt.title('Position of Double Pendulum')
    plt.legend()
    #plt.savefig('Angle.pdf')
    
    plt.subplot(2, 1, 2)
    plt.plot(tpoints, omega1points, label='Upper')
    plt.plot(tpoints, omega2points, label='Lower')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.xlabel('Time (s)')
    plt.title('Angular Velocity of Double Pendulum')
    #plt.savefig('Angular velocity.pdf')
    plt.tight_layout()
    plt.legend()
    plt.show()
