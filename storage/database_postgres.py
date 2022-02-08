import csv

from .data_type import Settlement, Coordinates
from .database_api import DatabaseAPI


class DatabasePostgres(DatabaseAPI):

    def __init__(self, port, db_name, csvfile):
        super(DatabasePostgres, self).__init__()
        with open(csvfile, 'r', newline='\n', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            records = []
            for row in reader:
                records.append((
                    row['id'],
                    row['region'].lower(),
                    row['municipality'].lower(),
                    row['settlement'].lower(),
                    row['latitude_dd'],
                    row['longitude_dd']
                ))
            # self.cursor.executemany(Queries.INSERT_DATA_QUERY, records)
            # self.conn.commit()

    def get_settlements(self, settlement) -> list[Settlement]:
        pass

    def get_coordinates(self, settlement_id: int) -> Coordinates:
        pass
