import numpy as np
from Layer import Layer
from Dense import Dense
from Activation import Tanh
from Network import train, predict
from losses import mse, mse_prime
import pandas as pd
from IPython.display import display

# network
network = [
    Dense(9, 9),
    Tanh(),
    Dense(9, 1),
    Tanh()
]

P = [
    [[0, 0, 0],  #1
     [0, 1, 0],
     [0, 0, 0]],
    [[1, 0, 0],  #2
     [0, 0, 0],
     [0, 0, 1]],
    [[0, 0, 1],  #2
     [0, 0, 0],
     [1, 0, 0]],
    [[1, 0, 0],  #3
     [0, 1, 0],
     [0, 0, 1]],
    [[0, 0, 1],  #3
     [0, 1, 0],
     [1, 0, 0]],
    [[1, 0, 1],  #4
     [0, 0, 0],
     [1, 0, 1]],
    [[1, 0, 1],  #5
     [0, 1, 0],
     [1, 0, 1]],
    [[1, 1, 1],  #6
     [0, 0, 0],
     [1, 1, 1]],
    [[1, 0, 1],  #6
     [1, 0, 1],
     [1, 0, 1]],
]

Q = [1, 0, 0, 1, 1, 0, 1, 0, 0]

X = np.reshape(P, (9, 9, 1))
Y = np.reshape(Q, (9, 1, 1))

# train
train(network, mse, mse_prime, X, Y)  # , epochs=10000, learning_rate=0.1)


pass

# T = [[0,1,0,
#       1,0,1,
#       0,1,0],
#      [0,0,0,
#       1,1,1,
#       0,0,0],
#      [0,1,0,
#       1,1,1,
#       0,1,0]]
# # predict /
# Z =
# predict(network,[Z])
