import csv
import petl as etl
from datetime import datetime

class CsvDriver:
    def __init__(self) -> None:
        self.data_dir = 'swapp/sw_api/data/'
        self.fieldnames = [
            'name',
            'height',
            'mass',
            'hair_color',
            'skin_color',
            'eye_color',
            'birth_year',
            'gender',
            'homeworld',
            'date'
        ]
    
    def export(self, data: list) -> str:
        def generate_filename() -> str:
            return f'{datetime.now()}.csv'
        filename = generate_filename()
        with open(f'{self.data_dir}{filename}', 'x', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return filename
    
    def import_file(self, filename) -> dict:
        with open(f'{self.data_dir}{filename}', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            return list(reader)

if __name__ == '__main__':
    c = CsvDriver()
    d = c.import_file('2021-06-26 16:34:38.489373.csv')
    table = etl.fromdicts(d, header=c.fieldnames)
    print(table)
