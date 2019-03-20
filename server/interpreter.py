# interpret and execute commands
from config import Config
from validator import Validator

# TODO
def pre_parse(command):
    return command

# TODO
# evaluate a command
# @param func will be the function that we need to call
# @param args will be the arguments of the function to call
def evaluate(command,index,func,args):
    None

def execute_command(command):
    # check if is a valid command
    Validator.command(command)
    evaluate(command,0,'',[])



