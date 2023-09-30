import pandas as pd

from sklearn import linear_model
import numpy as np
#dsd

linreg = linear_model.LinearRegression()


df = pd.read_csv('alles.csv')
X = df[['open']]
Y = df[['close']]

linregab = linreg.fit(X, Y)
coef = linreg.coef_(X, Y)
r_sq = linreg.score(X, Y)
print ('coefficient '+str(r_sq))
print ('coefficient '+str(coef))