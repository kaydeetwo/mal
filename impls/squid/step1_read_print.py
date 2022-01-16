from prompt_toolkit import PromptSession
import sys
from reader import read_str
from printer import pr_str

def READ(reader):
    return read_str(reader)

def EVAL(param):
    return param

def PRINT(string):
    return pr_str(string)

def rep(param):
    return PRINT(EVAL(READ(param)))

def response(code, text):
    print(f"[{code}] {text}")

session = PromptSession()


#if __name__ == '__main__':
    # print('Squid LISP REPL')
    # print('Ctrl-D to exit')
    # while 1:
    #     try:
    #         input = session.prompt('user> ') 
    #         response("OUT", rep(input))
    #     except:
    #         response("EXIT", "Quitting")
    #         exit(0)

#    print(READ('123 '))
# print(PRINT(READ('( + 2 (* 3 4) ) ')))

# print(read_str('(2 + 4 * 5)'))   
