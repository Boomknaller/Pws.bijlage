import pandas as pd
from datetime import datetime, timedelta
class Format:
    # Aantal_bestanden = 730

    # Datum = datetime(2021, 8, 16)

    def __init__(self):
        self.data = pd.DataFrame()

    def laad_bestanden(self, aantal_bestanden):
        for datum in (
                datetime(2021, 8, 16) + timedelta(days)
                for days in range(aantal_bestanden)
        ):
            self.laadBestandMetDatum(datum)

        self.save_data('alles.csv')

    def laadBestandMetDatum(self, datum):
        filename = self.maak_bestandsnaam(datum)
        data = self.lees_data(filename)

        print(filename)

        if not self.data.empty:
            self.data = pd.concat([self.data, data])
        else:
            self.data = data

    def maak_bestandsnaam(self, datum):
        datum_str = datum.strftime('%Y-%m-%d')
        bestandsnaamstr = f'{datum_str}.csv'   # str(datum_str + '.csv')
        return bestandsnaamstr
    def lees_data(self, filename):
        # Door delimeter worden er kolommen gemaakt en de decimal is voor de komma's bij de integers
        df = pd.read_csv(filename, delimiter=',', decimal='.')
        df['Date'] = filename.strip(".csv")
        return df

    def save_data(self, filename):
         self.data.to_csv(filename)

    # def bestands_veranderen(self, Datum):
    #     Datum = Datum + timedelta(1)
    #     Datum = Datum.strftime('%Y%m%d')
    #     return Datum
    #
    # for x in range(aantal_bestanden):
    #     Datum = bestands_veranderen(Datum)
    #     Datum = str(Datum)
    #
    #     df = pd.read_csv(Datum + '.csv')
    #     df['Date'] = Datum
    #     df.to_csv(f'{Datum}.csv')
    #
    #     print(df.to_string()

if __name__ == "__main__":
    format = Format()
    format.laad_bestanden(aantal_bestanden=772)