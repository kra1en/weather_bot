import os
import sqlite3

from .database_api import DatabaseAPI
from .data_type import Settlement, Coordinates
from .sql import Queries
from .extract_data import extract


class DatabaseSQLite(DatabaseAPI):

    def __init__(self, db_name, csvfile):
        super(DatabaseSQLite, self).__init__()
        is_file = os.path.isfile(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(Queries.CREAT_TABLE_QUERY)
        if not is_file:
            self.cursor.executemany(Queries.INSERT_DATA_QUERY, extract(csvfile))
        self.conn.commit()

    def get_settlements(self, settlement):
        self.cursor.execute(Queries.SELECT_SETTLEMENTS_QUERY, (settlement.lower() + '%', '% ' + settlement.lower() + '%', '%-' + settlement.lower() + '%'))
        result = []
        for row in self.cursor.fetchall():
            result.append(Settlement(
                id=row[0],
                name=row[1],
                region=row[2]
            ))
        return result

    def get_coordinates(self, settlement_id: int):
        self.cursor.execute(Queries.GET_COORDINATES_BY_ID_QUERY, (settlement_id,))
        coord = self.cursor.fetchone()
        return Coordinates(lat=coord[0], lon=coord[1])
