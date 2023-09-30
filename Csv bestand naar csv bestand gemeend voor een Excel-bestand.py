import pandas as pd

# CSV-bestand inlezen met een komma als scheidingsteken en een punt als decimaal
csv_bestand = 'alles.csv'
df = pd.read_csv(csv_bestand, delimiter=',', decimal='.')

# Komma's veranderen naar punten en punten naar komma's, behalve in kolommen met een datum
for kolom in df.columns:
    if df[kolom].dtype == 'float64':
        df[kolom] = df[kolom].apply(lambda x: str(x).replace(',', 'temp').replace('.', ',').replace('temp', '.'))

# Dataframe naar excelbestand, met komma als decimal en punt als scheidingsteken
nieuw_csv_bestand = 'Volledige database stockpolls PWS.csv'
df.to_csv(nieuw_csv_bestand, index=False, sep=',', decimal=',')
print('Done')

import pandas as pd

# CSV-bestand wordt ingelezen
csv_bestand = 'Volledige database stockpolls PWS.csv'
df = pd.read_csv(csv_bestand)

# Het aantal rijen defineren
aantal_rijen = len(df)

# Het CSV-bestand wordt in zes delen gesplitst
deel_1 = df.iloc[:aantal_rijen // 6]
deel_2 = df.iloc[aantal_rijen // 6:2 * (aantal_rijen // 6)]
deel_3 = df.iloc[2 * (aantal_rijen // 6):3 * (aantal_rijen // 6)]
deel_4 = df.iloc[3 * (aantal_rijen // 6):4 * (aantal_rijen // 6)]
deel_5 = df.iloc[4 * (aantal_rijen // 6):5 * (aantal_rijen // 6)]
deel_6 = df.iloc[5 * (aantal_rijen // 6):]

# De zes delen worden opgeslagen in een csv bestand
deel_1.to_csv('deel_1.csv', index=False)
deel_2.to_csv('deel_2.csv', index=False)
deel_3.to_csv('deel_3.csv', index=False)
deel_4.to_csv('deel_4.csv', index=False)
deel_5.to_csv('deel_5.csv', index=False)
deel_6.to_csv('deel_6.csv', index=False)

print('CSV-bestand gesplitst in zes delen')
