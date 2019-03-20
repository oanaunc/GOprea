# this file will execute commands
from validator import Validator

class Executer:

    @staticmethod
    def create_table(table_name,columns):
        Validator.name(table_name)