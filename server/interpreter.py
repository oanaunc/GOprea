# interpret and execute commands
from config import Config
from validator import Validator

def execute_command(command):
    # check if is a valid command
    Validator.command(command)

