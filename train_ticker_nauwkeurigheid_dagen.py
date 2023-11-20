from train_ticker import neural_network_afwijking
import pandas as pd

dagen = [2, 3, 4, 5]
epochs = 1000
afwijkingen = pd.DataFrame(index=range(len(dagen)), columns=['dagen', 'epochs', 'min', 'mean', 'max'])

for (i, d) in enumerate(dagen):
    errors = neural_network_afwijking(dagen=d)
    afwijkingen.iloc[i]['dagen'] = d
    afwijkingen.iloc[i]['epochs'] = epochs
    afwijkingen.iloc[i]['min'] = errors[0]
    afwijkingen.iloc[i]['mean'] = errors[1]
    afwijkingen.iloc[i]['max'] = errors[2]

afwijkingen.to_excel('afwijkingen-dagen.xlsx')
