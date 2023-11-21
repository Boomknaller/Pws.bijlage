import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

# De dataset wordt ingelezen
data = pd.read_csv('koersen AAPL.csv', parse_dates=['Date'])
data.set_index('Date', inplace=True)

# Feature Engineering
data['lag_1'] = data['close'].shift(1)
data['dayofyear'] = data.index.dayofyear

# Verwijder rijen met ontbrekende gegevens
data.dropna(inplace=True)

# Extra kenmerken
features = ['dayofyear', 'lag_1']

# Split de trainingsset
train_size = int(len(data) * 0.8)
train, test = train_test_split(data, test_size=0.2, shuffle=False)

# Laad XGBoost en pas het model toe
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(train[features], train['close'])

# Voorspellingen voor de testset
test_forecast = model.predict(test[features])

# Werkelijke waarden voor de testset
y_true_test = test['close'].values

# Bereken de RMSE voor de testset
rmse_test = sqrt(mean_squared_error(y_true_test, test_forecast))
print(f'Testset Root Mean Squared Error (RMSE): {rmse_test}')

# Voorspellingen voor de gehele dataset
forecast = model.predict(data[features])

# Haal de werkelijke waarden uit de dataset
y_true = data['close'].values

# Bereken de RMSE voor de gehele dataset
rmse = sqrt(mean_squared_error(y_true, forecast))
print(f'Root Mean Squared Error (RMSE) voor de gehele dataset: {rmse}')

# Plot de voorspellingen
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['close'], label='Werkelijke gegevens', color='blue')
plt.plot(test.index, test_forecast, label='XGBoost Testvoorspelling', color='red')
plt.plot(data.index, forecast, label='XGBoost Voorspelling', color='orange')

# Voorspelling met input voor aantal voorspelde dagen
num_forecast_days = int(input("Het aantal dagen die je wilt voorspellen: "))
future_dates = pd.date_range(start=data.index[-1], periods=num_forecast_days, freq='D')[1:]
future_data = pd.DataFrame(index=future_dates)
future_data['dayofyear'] = future_data.index.dayofyear
future_data['lag_1'] = data['close'].shift(1)[-1]

# Voorspelling voor toekomstige data
extended_forecast = model.predict(future_data[features])

# Sinusvormige flux toevoegen
sinusoidal_factor = 10
sinusoidal_pattern = sinusoidal_factor * np.sin(np.arange(num_forecast_days) * (2 * np.pi / 365))

# Het zorgt dat de lengtes matchen
if len(extended_forecast) > len(sinusoidal_pattern):
    extended_forecast = extended_forecast[:-1]
else:
    sinusoidal_pattern = sinusoidal_pattern[:-1]

extended_forecast_with_fluctuation = extended_forecast + sinusoidal_pattern

print(f'Laatste voorspelde waarde: {extended_forecast_with_fluctuation[-1]}')  # Print de laatste voorspelde waarde
plt.plot(future_data.index, extended_forecast_with_fluctuation, label='Uitgebreide voorspelling met fluctuatie', linestyle='dashed', color='green')

plt.title('XGBoost Voorspelling')
plt.xlabel('Datum')
plt.ylabel('Slotkoers')
plt.legend()
plt.show()


