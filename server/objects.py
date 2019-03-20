# file with DB object types
from validator import Validator
import abc

class Gopreable(abc.ABC):

    # returns a query string that can create the object 
    @abc.abstractmethod
    def to_goprea(self):
        pass

class Table(Gopreable):

    def __init__(self,table_name,columns):
        Validator.name(table_name)
        Validator.columns(columns)
        self.table_name = table_name
        self.columns = columns

    def to_goprea(self):
        query = "create table " + self.table_name + " ( "
        
        for t in self.columns:
            query += t[0] + " " + t[1] + ", "

        query = query[:-2] + " )"

        return query
