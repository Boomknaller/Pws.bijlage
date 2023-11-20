import pandas as pd

data1 = pd.read_csv('aangepast_bestand.csv', thousands=',', parse_dates=['Date'])
data2 = pd.read_csv('output(AAPL).csv', parse_dates=['Date'])

samengevoegd_data = pd.concat([data1, data2], ignore_index=True)

samengevoegd_data = samengevoegd_data[['open', 'close', 'high', 'low', 'volume', 'Date']]

samengevoegd_data.to_csv('koersen AAPL.csv', index=False)