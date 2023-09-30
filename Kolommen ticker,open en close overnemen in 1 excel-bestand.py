import pandas as pd

# Bronbestand wordt gelezen als dataframe
bron_excel_bestand = '6 delen samengevoegd Stockpolls PWS.xlsx'
df = pd.read_excel(bron_excel_bestand)

# Kolommen die overgenomen worden in een nieuwe bestand
colums_to_keep = ['deel_1', 'deel_2', 'deel_3', 'deel_4', 'deel_5', 'deel_6']
df = df[colums_to_keep]

# Dataframe opgeslagen in een nieuw excel bestand
nieuw_excel_bestand = '6 delen samengevoegd Stockpolls PWS(1).xlsx'
df.to_excel(nieuw_excel_bestand, index=False)

print('Datatransfer done!')