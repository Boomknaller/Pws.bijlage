import numpy as np
from Layer import Layer
from Dense import Dense
from Activation import Tanh
from Network import train, predict
from losses import mse, mse_prime
import pandas as pd
from IPython.display import display

# df = pd.read_csv("alles.csv")
# nameAndOpen = df[['ticker','open', 'close']]
# display(nameAndOpen)
# display(nameAndOpen.loc[(df['ticker']=='CTT')])
# row_count = len(nameAndOpen.loc[(df['ticker']=='CTT')])
# print(row_count)
row_count = 6

# network
network = [
     Dense(3,4),
     Tanh(),
     Dense(4,1),
     Tanh()
     # Dense(row_count,row_count),
     # Dense(row_count,row_count)
     ]

X = np.reshape(np.arange(60), (20, 3, 1))
Y = np.reshape((np.arange(20)+1) % 2, (20, 1, 1))

# train
train(network, mse, mse_prime, X, Y) # , epochs=10000, learning_rate=0.1)
