import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('output(AAPL)0).csv', parse_dates=['Date'])

# Replace commas with dots in the columns containing numbers
columns_to_convert = ['open', 'close', 'high', 'low', 'volume']

for column in columns_to_convert:
    data[column] = data[column].replace(',', '.', regex=True).astype(float)

# Optional: Save the modified dataframe to a new CSV file
data.to_csv('aangepast_bestand.csv', index=False)

