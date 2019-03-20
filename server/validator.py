# validate stuff
from config import Config

class Validator:

    # a command must be a list of strings
    @staticmethod
    def command(com):
        if not isinstance(com,list):
            raise TypeError('A command should be a list of strings')
        for word in com:
            if not isinstance(word,str):
                raise TypeError('A command should be a list of strings')

    @staticmethod
    def name(nm):
        if not isinstance(nm,str):
            raise TypeError('A name should be a string')
        if nm[0] < 'a' or nm[0] > 'z':
            raise NameError('A name should be start with a letter')
        # check for banned symbols
        items = Config.items() + Config.banned_symbols
        for c in nm:
            if c in items:
                raise NameError('A name should not contain a banned symbol, operator or delimiter')
