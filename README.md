# Double Pendulum

This program simulates motion of a double pendulum system, by solving 4 first-order differential equations using the Runge-Kutta method. 

The user can input the desired masses and rod lengths of both the upper and lower pendulums, and two graphs are outputted: the angle, and angular velocity of both pendulums over time.

NOTE: This pendulum model assumes:
* The pendulum rods are inextensible, massless, and taught
* No air resistance

## Getting Started

### Prerequisites
* Python development environment

To run this program, you must set up a Python development environment on your machine:
* Go to the Python website (https://www.python.org/getit/). Download and install the latest version.

Once Python is installed on your machine, simply download the files from this repository!


## Running the program

Once you have a copy of this program on your local machine, navigate to the program directory and run the python file. (If you do not know how to do this, see https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs)


The function ```doublePendulum``` takes 7 arguments: 
1. *mass1* - the mass of the upper pendulum bob (in kg)
2. *mass2* - the mass of the lower pendulum bob (in kg)
3. *len1* - the lengths of the upper pendulum rod (in m)
4. *len2* - the length of the lower pendulum rod (in m)
5. *theta1* - the initial angle of the upper pendulum rod (in radians)
6. *theta2* - the initial angle of the lower pendulum rod (in radians)
7. *tmax* - the length of time that the motion is simulater over (in seconds)

In your console, enter

```
doublePendulum(mass1, mass2, len1, len2, theta1, theta2, tmax)
```

replacing each argument with the value of your choice. e.g.,

```
doublePendulum(2, 1, 0.5, 0.5, 0.5, -0.2, 10)
```

The program will output two graphs:
* The angle of each pendulum against time
* The angular velocity of each pendulum against time
