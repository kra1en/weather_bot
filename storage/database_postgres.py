from .data_type import Settlement, Coordinates
from .database_api import DatabaseAPI


class DatabasePostgres(DatabaseAPI):

    def __init__(self, port, db_name, csvfile):
        super(DatabasePostgres, self).__init__()

        # self.cursor.executemany(Queries.INSERT_DATA_QUERY, extract(csvfile))
        # self.conn.commit()

    def get_settlements(self, settlement) -> list[Settlement]:
        pass

    def get_coordinates(self, settlement_id: int) -> Coordinates:
        pass
