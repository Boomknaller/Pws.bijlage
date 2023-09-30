import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_excel('Open, close en ticker Stockpolls PWS.xlsx')

X = df[['open']]
Y = df[['close']]

linreg = LinearRegression()

linreg.fit(X,Y)
coef = linreg.coef_
r_sq = linreg.score(X, Y)
print('R^2-waarde: ', r_sq)
print('coëfficiënt:', coef)