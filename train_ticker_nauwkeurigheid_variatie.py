from train_ticker import neural_network_afwijking
import pandas as pd

epochs = [1000]*20
afwijkingen = pd.DataFrame(index=range(len(epochs)), columns=['epochs', 'min', 'mean', 'max'])

for (i, e) in enumerate(epochs):
    errors = neural_network_afwijking(epochs=e)
    afwijkingen.iloc[i]['epochs'] = e
    afwijkingen.iloc[i]['min'] = errors[0]
    afwijkingen.iloc[i]['mean'] = errors[1]
    afwijkingen.iloc[i]['max'] = errors[2]

afwijkingen.to_excel('afwijkingen-variatie.xlsx')
