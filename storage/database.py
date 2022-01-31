import sqlite3


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')

    def close(self):
        self.conn.close()


class Database(Connection):
    def __init__(self):
        super(Database, self).__init__()
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists city_inf(
            id int primary key,
            region varchar(100) not null,
            municipality varchar(100) not null,
            settlement varchar(100) not null,
            lat real not null, 
            lon real not null);""")

        with open('data.csv', 'r', newline='\n') as file:
            ...