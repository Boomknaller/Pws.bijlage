import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

# Laad de dataset
data = pd.read_csv('koersen AAPL.csv', parse_dates=['Date'])
data.set_index('Date', inplace=True)

# Functie om RMSE te berekenen
def calculate_rmse(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = sqrt(mse)
    return rmse

# ARIMA model met parameters
best_rmse = float('inf')
best_params = None

# Parameter afstemmen
for p in range(3):
    for d in range(2):
        for q in range(3):
            for P in range(2):
                for D in range(2):
                    for Q in range(2):
                        try:
                            model = SARIMAX(data['close'], order=(p, d, q), seasonal_order=(P, D, Q, 12))
                            arima_fit = model.fit(disp=False)

                            # Trainingset gespiltst
                            train_size = int(len(data) * 0.8)
                            train, test = data.iloc[:train_size], data.iloc[train_size:]

                            # Voorspellingen voor testset
                            arima_pred = arima_fit.predict(start=len(train), end=len(train) + len(test) - 1, typ='levels')
                            rmse = calculate_rmse(test['close'], arima_pred)

                            if rmse < best_rmse:
                                best_rmse = rmse
                                best_params = (p, d, q, P, D, Q)

                        except Exception as e:
                            print(f"Error: {e}")
                            continue

print(f'Beste  ARIMA Parameters: {best_params}')
print(f'Beste ARIMA RMSE: {best_rmse}')

# Hier worden de parameters gebruikt voor dit model
best_model = SARIMAX(data['close'], order=best_params[:3], seasonal_order=(best_params[3], best_params[4], best_params[5], 12))
best_arima_fit = best_model.fit(disp=False)

# Voorspellingen voor testset
arima_pred = best_arima_fit.predict(start=len(train), end=len(train) + len(test) - 1, typ='levels')

# Print de gecaluleerde RMSE voor de beste ARIMA model in de testset
test_rmse = calculate_rmse(test['close'], arima_pred)
print(f'RMSE voor de testset: {test_rmse}')

# Input voor het aantal dagen die je wilt voorspellen
num_forecast_days = int(input("Het aantal dagen die je wilt voorspellen: "))
future_dates = pd.date_range(start=data.index[-1], periods=num_forecast_days, freq='D')[1:]

# Voorspellingen voor toekomstige data
future_pred = best_arima_fit.get_forecast(steps=len(future_dates)).predicted_mean

# Het toevoegen van noise in toekomstige voorspellingen
np.random.seed(42)
noise = np.random.normal(scale=0.1, size=len(future_pred))
future_pred_with_noise = future_pred * (1 + noise)

# Plot voor voorspellingen
plt.plot(data.index, data['close'], label='Historical Data')
plt.plot(test.index, arima_pred, label='ARIMA Test Prediction', color='red')
plt.plot(future_dates, future_pred_with_noise, label=f'ARIMA + Future Prediction with Noise ({num_forecast_days} days)', linestyle='dashed', color='green')
plt.legend()

# Print de laatste waarde die voorspeld is
print(f'Laast voorspelde waarde: {future_pred_with_noise.iloc[-1]}')

plt.show()
