# main server script

import sys
from config import Config
from interpreter import execute_command

def parse_command(line):
    line = line.replace('\n','').replace('\r','')
    for item in Config.items():
        line = line.replace(item,' ' + item + ' ')
    return [x for x in line.lower().split(' ') if x != '']

def main():
    print("Server started")

    for line in sys.stdin:
        print("Execute command: " + line)

        command = parse_command(line)
        execute_command(command)

        print(command)
    
        # TODO delete this if
        if line == 'EXIT\n':
            return 0
        pass

    return 0

if __name__ == '__main__':
    main()