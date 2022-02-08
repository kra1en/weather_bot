import os
import sqlite3
import csv

from .database_api import DatabaseAPI
from .data_type import Settlement, Coordinates
from .sql import Queries


class DatabaseSQLite(DatabaseAPI):

    def __init__(self, db_name, csvfile):
        super(DatabaseSQLite, self).__init__()
        is_file = os.path.isfile(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(Queries.CREAT_TABLE_QUERY)
        if not is_file:
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
            self.cursor.executemany(Queries.INSERT_DATA_QUERY, records)
        self.conn.commit()

    def get_settlements(self, settlement):
        self.cursor.execute(Queries.SELECT_SETTLEMENTS_QUERY, (settlement + '%',))
        result = []
        for row in self.cursor.fetchall():
            result.append(Settlement(
                id=row[0],
                name=row[1],
                region=row[2]
            ))
        return result

    def get_coordinates(self, settlement_id: int):
        self.cursor.execute(Queries.GET_COORDINATS_FROM_ID, (settlement_id,))
        coord = self.cursor.fetchone()
        return Coordinates(lat=coord[0], lon=coord[1])
