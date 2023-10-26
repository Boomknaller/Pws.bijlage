import pandas as pd
from sklearn.linear_model import LinearRegression
# Gegevens worden omgezet in een dataframe
df = pd.read_excel('Open, close en ticker Stockpolls PWS.xlsx')
# De X-as en Y-as defineren met de juiste kolom
X = df[['open']] # Onafhankelijke waarde
Y = df[['close']] # Afhankelijke waarde
# Plot een lineaire regressiemodel
linreg = LinearRegression()
# Past model in data
linreg.fit(X,Y)
coef = linreg.coef_              # Richtingscoëfficiënt
r_sq = linreg.score(X, Y)        # R^2-waarde
print('R^2-waarde: ', r_sq)
print('coëfficiënt:', coef)