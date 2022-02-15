from .data_type import Settlement, Coordinates
from .database_sqlite import DatabaseSQLite
from .database_postgres import DatabasePostgres


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Storage(metaclass=Singleton):
    SQLITE = 'sqlite'
    POSTGRESQL = 'postgresql'
    DB_NAME = 'weather_bot'
    DB_PORT = '5432'
    DATA = 'data.csv'

    def __init__(self, database=SQLITE, in_memory=True, db_name=DB_NAME, db_port=DB_PORT, source_file=DATA):
        if database == self.SQLITE:
            if in_memory:
                self.__db = DatabaseSQLite(':memory:', csvfile=source_file)
            else:
                self.__db = DatabaseSQLite(db_name, csvfile=source_file)
        elif database == self.POSTGRESQL:
            self.__db = DatabasePostgres(db_name=db_name, port=db_port, csvfile=source_file)
        else:
            raise ValueError("Неизвестная база данных")

    def get_settlements(self, settlement) -> list[Settlement]:
        return self.__db.get_settlements(settlement)

    def get_coordinates(self, settlement_id: int) -> Coordinates:
        return self.__db.get_coordinates(settlement_id)
