from prompt_toolkit import PromptSession
import sys
from reader import read_str

def READ(param):
    return param

def EVAL(param):
    return param

def PRINT(param):
    return param

def rep(param):
    return PRINT(EVAL(READ(param)))

def response(code, text):
    print(f"[{code}] {text}")

session = PromptSession()


if __name__ == '__main__':
    # print('Squid LISP REPL')
    # print('Ctrl-D to exit')
    # while 1:
    #     try:
    #         input = session.prompt('user> ') 
    #         response("OUT", rep(input))
    #     except:
    #         response("EXIT", "Quitting")
    #         exit(0)

    print(read_str('(+ 2 (* 3 4 ) )'))
