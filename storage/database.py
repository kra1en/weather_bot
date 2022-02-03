import sqlite3
import csv

from .storage_api import StorageAPI
from .data_type import Settlement, Coordinates

from .sql import Queries as sql


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')

    def close(self):
        self.conn.close()


class Database(Connection, StorageAPI):

    def __init__(self, csvfile):
        super(Database, self).__init__()
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql.CREAT_TABLE_QUERY)

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
            self.cursor.executemany(sql.INSERT_DATA_QUERY, records)
            self.conn.commit()

    def get_settlements(self, settlement):
        self.cursor.execute(sql.SELECT_SETTLEMENTS_QUERY, (settlement + '%',))
        result = []
        for row in self.cursor.fetchall():
            result.append(Settlement(
                id=row[0],
                name=row[1],
                region=row[2]
            ))
        return result


    def get_coordinates(self, settlement_id: int):
        self.cursor.execute(sql.GET_COORDINATS_FROM_ID, (settlement_id,))
        coord = self.cursor.fetchone()
        return Coordinates(lat=coord[0], lon=coord[1])
