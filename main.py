from absl import app
from absl import flags
import numpy as np
import matplotlib.pyplot as plt

FLAGS = flags.FLAGS
flags.DEFINE_float("elasticity", 100, "Elasticity of the string.")
flags.DEFINE_float("ball_mass_kg", 0.1, "Ball mass in kilograms.")
flags.DEFINE_string("out_path", "", "Where to save the figure.")

# Variables
L0 = 1.5
t = 10
ugaoUStepenima = 30

# Constants
g = 9.81
dt = 1e-3
n = 1000*t

def main(unused_argv):
    # Starting point
    teta = np.deg2rad(ugaoUStepenima)
    r = L0
    x = r*np.sin(teta)
    y = -r*np.cos(teta)
    X = np.zeros(n,float); X[0]=x
    Y = np.zeros(n,float); Y[0]=y
    vx = 0
    vy = 0

    # Creating an array of positions
    for i in range(1,n):
        ax = -FLAGS.elasticity * (r - L0) * x / (FLAGS.ball_mass_kg * r)
        ay = -FLAGS.elasticity * (r - L0) * y/ (FLAGS.ball_mass_kg * r) - g
        vx += ax * dt 
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        X[i] = x
        Y[i] = y
        r = np.sqrt(x * x + y * y)

    # Ploting
    plt.figure()
    plt.plot(X,Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(FLAGS.out_path)

if __name__ == '__main__':
  app.run(main)