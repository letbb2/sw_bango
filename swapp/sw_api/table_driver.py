import petl as etl
from .csv_driver import CsvDriver

class Table:
    def __init__(self, filename: str) -> None:
        self.csv = CsvDriver()
        self.fieldnames = self.csv.fieldnames
        self.data = self.csv.import_file(filename)
    
    def print_table(self):
        table = etl.fromdicts(self.data, header=self.fieldnames)
        return table
    
if __name__ ==  '__main__':
    t = Table('2021-06-26 16:34:38.489373.csv')
    t.print_table()