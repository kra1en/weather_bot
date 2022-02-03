import sqlite3
import csv
from dataclasses import dataclass

from .storage_api import StorageAPI


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')

    def close(self):
        self.conn.close()


@dataclass
class Settlement:
    id: int
    name: str
    region: str
    municipality: str
    lat: float
    lon: float


class Database(Connection, StorageAPI):

    def __init__(self, csvfile):
        super(Database, self).__init__()
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.CREAT_TABLE_QUERY)

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
            self.cursor.executemany(self.INSERT_DATA_QUERY, records)
            self.conn.commit()

    def get_settlements(self, settlement):
        self.cursor.execute(self.SELECT_SETTLEMENTS_QUERY, (settlement + '%',))
        result = []
        for row in self.cursor.fetchall():
            result.append(Settlement(
                id=row[0],
                name=row[1],
                municipality=row[2],
                region=row[3],
                lat=row[4],
                lon=row[5]
            ))
        return result

    CREAT_TABLE_QUERY = """
                create table if not exists city_info(
                id int primary key,
                region varchar(100) not null,
                municipality varchar(100) not null,
                settlement varchar(100) not null,
                lat real not null, 
                lon real not null);
        """
    INSERT_DATA_QUERY = """
            insert into city_info (id, region, municipality, settlement, lat, lon) 
            values (?,?,?,?,?,?);
        """
    SELECT_SETTLEMENTS_QUERY = """
            select c1.id, c1.settlement, c1.municipality, c1.region, c1.lat, c1.lon 
            from city_info c1 
            join city_info c2 on c1.id = c2.id group by c1.settlement, c1.region
            having c1.settlement like lower(?);
        """
