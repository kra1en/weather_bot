import csv


def extract(filename):
    records = []
    with open(filename, 'r', newline='\n', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append((
                row['id'],
                row['region'].lower(),
                row['municipality'].lower(),
                row['settlement'].lower(),
                row['latitude_dd'],
                row['longitude_dd']
            ))
    return records
