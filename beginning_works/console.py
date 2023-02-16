#!/usr/bin/python3
'''
  The Console :)
'''

import cmd


class HbnbCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''
          Exits the Command Interpreter :)
        '''
        return True

    def do_EOF(self, line):
        '''
          Handles End Of File character :)
        '''
        print()
        return True

    def emptyline(self):
        '''
          Does nothing when the Enter Key
          is pressed :)
        '''
        pass


if __name__ == '__main__':
    HbnbCommand().cmdloop()
