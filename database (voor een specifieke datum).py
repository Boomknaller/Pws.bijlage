from datetime import datetime
import pandas as pd
from IPython.display import display
from polygon import RESTClient


# Functie om data op te halen en op te slaan
def data_Ophalen(api_key, z):
    client = RESTClient(api_key)
    resp_generator = client.get_grouped_daily_aggs(date=z, locale='us', market_type='stocks')
    df = pd.DataFrame(resp_generator)
    display(df)
    df.to_csv(f'{z}.csv')


if __name__ == "__main__":
    api_key = "icjXXqxEtJ8FGdGebhw3y36fpe3I0_DU"

    # Invoer voor een datum
    date_input = input("Voer de gewenste datum in (YYYY-MM-DD): ")

    try:
        specific_date = datetime.strptime(date_input, '%Y-%m-%d')  # Datum wordt omgezet naar een datetime object
        specific_date_str = specific_date.strftime('%Y-%m-%d')  # Datum wordt ingeldeeld als string
        data_Ophalen(api_key, specific_date_str)

    except ValueError:
        print("Ongeldige datumindeling. Gebruik het formaat YYYY-MM-DD.")
