import pandas as pd

excel_bestand = pd.read_excel('C:\\Users\\badrc\\PycharmProjects\\PWS_2_Badr_Jasper\\Open^J close en ticker Stockpolls PWS (-----).xlsx')

excel_bestand.to_csv('Open , close en ticker.csv', index=False)

print('Done!')