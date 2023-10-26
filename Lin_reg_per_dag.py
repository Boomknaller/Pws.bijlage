import pandas as pd
# Gegevens omgezet in een dataframe
df = pd.read_excel('Open, close en ticker Stockpolls PWS.xlsx')
# Waarden worden op datum gesorteerd
df.sort_values(by='Date', inplace=True)
# Nieuwe kolom voor groeifactor
df['groeifactor'] = 0.0     # Begingetal 0.0
# Loop door de rijen heen om te bepalen wat de groeifactor per dag is.
for i in range(1, len(df)):
   open_value = df.at[i, 'open']
   close_value = df.at[i, 'close']

   groeifactor = open_value // close_value
   df.at[i,'groeifactor'] = groeifactor

print(df[['Date', 'groeifactor']])
df.to_excel('Bestand met groeifactoren.xlsx', index=False)
print('Done')




