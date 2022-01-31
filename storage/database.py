import sqlite3
import csv


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')

    def close(self):
        self.conn.close()


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
                recods.append(((row['id'], row['region'], row['municipality'], row['settlement'], row['latitude_dd'], row['longitude_dd'])))
            self.cursor.executemany("insert into city_inf (id, region, municipality, settlement, lat, lon)\
                    values (?,?,?,?,?,?)", recods)
            self.conn.commit()
