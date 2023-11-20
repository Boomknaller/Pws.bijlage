from train_ticker import neural_network_afwijking
import pandas as pd

epochs = 1000
tickers = ['GOOGL', 'AAPL', 'MSFT', 'META', 'TSLA', 'AMZN']
afwijkingen = pd.DataFrame(index=range(len(tickers)), columns=['epochs', 'ticker', 'min', 'mean', 'max'])

for (i, t) in enumerate(tickers):
    errors = neural_network_afwijking(epochs=epochs, ticker=t)
    afwijkingen.iloc[i]['epochs'] = epochs
    afwijkingen.iloc[i]['ticker'] = t
    afwijkingen.iloc[i]['min'] = errors[0]
    afwijkingen.iloc[i]['mean'] = errors[1]
    afwijkingen.iloc[i]['max'] = errors[2]

afwijkingen.to_excel('afwijkingen-tickers.xlsx')
