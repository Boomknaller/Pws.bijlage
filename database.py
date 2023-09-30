from polygon import RESTClient
import pandas as pd
from IPython.display import display
import sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

# Functie data_Ophalen is om data op te halen en op te slaan
def data_Ophalen(api_key, z):
    client = RESTClient(api_key)
# Data wordt opgehaald voor de gegeven datum en opslagen in een (df) dataframe
    resp_generator = client.get_grouped_daily_aggs(date=z, locale='us', market_type='stocks')
    df = pd.DataFrame(resp_generator)
    display(df)                                                          # Data wordt weergegeven in Ipython
    df.to_csv(f'{z}.csv')                                                # Dataframe wordt opgeslagen als een csv bestand

# Functie om datum bij te werken
def update_date(date, days):
    new_date = date + timedelta(days=days)                               # Datum en het aantal opgegeven dagen samen gebracht
    new_date_str = new_date.strftime('%Y-%m-%d')                         # Datum heeft format 'Year-Month-Day'
    return new_date_str

if __name__ == "__main__":
    api_key = "icjXXqxEtJ8FGdGebhw3y36fpe3I0_DU"                         # Toegewezen Api key
    days_to_iterate = 730                                                # Aantal dagen die een lus doorloopt
    current_date = datetime(year=2023, month=8, day=30)                  # Begindatum van opgevraagde gegevens
# Iteratie over de opgegeven aantal dagen
    for _ in range(days_to_iterate):
        current_date_str = current_date.strftime('%Y-%m-%d')             # indeling van de huidige datum
        data_Ophalen(api_key, current_date_str)                          # Data ophalen en opslaan
        current_date_str = update_date(current_date, 1)                  # Datum wordt per dag bijgewerkt
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d')   # Functie wordt omgezet in een Python object
        time.sleep(13)                                                   # Iteratie heeft een cooldown van 13 seconden
    else:
        sys.exit()                                                       # Script eindigt