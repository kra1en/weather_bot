import sqlite3
import csv
from dataclasses import dataclass


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


class Database(Connection):
    
    def __init__(self, csvfile):
        super(Database, self).__init__()
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists city_inf(
            id int primary key,
            region varchar(100) not null,
            municipality varchar(100) not null,
            settlement varchar(100) not null,
            lat real not null, 
            lon real not null);""")

        with open(csvfile, 'r', newline='\n', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            recods = []
            for row in reader:
                recods.append(((row['id'], row['region'], row['municipality'], row['settlement'].lower(), row['latitude_dd'], row['longitude_dd'])))
            self.cursor.executemany("insert into city_inf (id, region, municipality, settlement, lat, lon)\
                    values (?,?,?,?,?,?)", recods)
            self.conn.commit()

    def get_settlements(self, settlement):
        self.cursor.execute("select id, settlement, municipality, region, lat, lon from city_inf where settlement like lower(?);", (settlement+'%',))
        all_result = self.cursor.fetchall()
        result = []
        for row in all_result:
            result.append(Settlement(id=row[0], name=row[1], region=row[2], municipality=row[3], lat=row[4], lon=row[5]))
        return result

