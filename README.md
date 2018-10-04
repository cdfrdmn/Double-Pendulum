# Double Pendulum

This program simulates motion of a double pendulum system, by solving 4 first-order differential equations using the Runge-Kutta method.

## Getting Started

### Prerequisites

## Running the program

Once you have a copy of this program on your local machine, run the python file. The function ```doublePendulum``` has 4 arguments: 
1. length - the length of both pendulum rods (in m)
2. theta1 - the initial angle of the upper pendulum rod (in radians)
3. theta2 - the initial angle of the lower pendulum rod (in radians)
4. tmax - the length of time that the motion is simulater over (in seconds)

In your console, enter

```
doublePendulum(length, theta1, theta2, tmax)
```

replacing each argument with the value of your choice. e.g., for rod lengths of 0.5 m, an upper rod initial angle of 0.1 rad, a lower rod initial angle of 1.5 rad and a simulation time of 10 seconds, the command would be:

```
doublePendulum(0.5, 0.1, 1.5, 10)
```

The program will output two graphs:
* The angle (in radians) of each pendulum rod against time
* The angular velocity (in radians per second) of each pendulum rod against time

## How does it work?
