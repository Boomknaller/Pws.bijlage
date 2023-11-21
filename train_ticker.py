import numpy as np
import pandas as pd

from Activation import Tanh
from Dense import Dense
from Network import train, predict
from losses import mse, mse_prime

# df = pd.read_csv('alles.csv')
# df[['ticker', 'open', 'close', 'volume', 'timestamp']].to_pickle('stocks.dat')

def neural_network_afwijking(epochs=1000, dagen=3, ticker=None):
    alle_stocks = pd.read_pickle('stocks.dat')

    if ticker is None:
        ticker = alle_stocks['ticker'].sample(n=1, random_state=1).iat[0]

    stocks = alle_stocks.loc[alle_stocks['ticker'] == ticker]

    trainings_grootte = int(len(stocks) / (2 * dagen))
    trainings_data = stocks[['open', 'close', 'volume']].iloc[0:trainings_grootte * dagen]

    schaal_factor = stocks['open'].max()
    trainings_data['open'] /= schaal_factor
    trainings_data['close'] /= schaal_factor
    trainings_data['volume'] /= trainings_data['volume'].max()
    trainings_data -= 0.5

    trainings_input = np.reshape(trainings_data, (-1, dagen * 3, 1))
    trainings_output = np.reshape(stocks[['open']].iloc[dagen:dagen * len(trainings_input) + 1:dagen], (-1, 1, 1)) / schaal_factor

    network = [
        Dense(dagen*3, dagen*3),
        Tanh(),
        Dense(dagen*3, 1),
        Tanh()
    ]

    train(network, mse, mse_prime, trainings_input, trainings_output, epochs=epochs, verbose=False)

    controle_afstand = int(len(stocks)/2)
    controle_data = stocks[['open', 'close', 'volume']].iloc[controle_afstand:controle_afstand + trainings_grootte * dagen]

    controle_data['open'] /= schaal_factor
    controle_data['close'] /= schaal_factor
    controle_data['volume'] /= controle_data['volume'].max()
    controle_data -= 0.5

    controle_input = np.reshape(controle_data, (-1, dagen * 3, 1))
    controle_output = np.reshape(stocks[['open']].iloc[dagen:dagen * len(controle_input) + 1:dagen], (-1, 1, 1)) / schaal_factor

    errors = []
    for x, y in zip(controle_input, controle_output):
        errors.append((predict(network, x) - y)[0][0])

    errors = np.array(errors)

    max_error = np.abs(errors).max()
    min_error = np.abs(errors).min()
    mean_error = np.abs(errors).mean()

    return min_error, mean_error, max_error