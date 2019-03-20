# writer class

import csv
from objects import Table
from validator import Validator
import os

class Writer:

    def __init__(self):
        self.delimiter = ','

    def new_table(self,table):
        Validator.table(table)

        if os.path.exists('goprea\\' + table.table_name + ".goprea"):
            raise SystemError('the table ' + table.table_name + ' already exists')
       
        with open('goprea\\' + table.table_name + ".goprea",'w+') as gf:
            gf.write(table.to_goprea())
        
        with open('data\\tables.csv', 'a', newline='') as csvfile:
            table_writer = csv.writer(csvfile, delimiter=self.delimiter)
            table_writer.writerow(['defaultDB',table.table_name,'table'])