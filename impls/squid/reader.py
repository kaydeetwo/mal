import re
    
class Reader:
    def __init__(self):
        self.Tokens = []
        self.position = 0

    def next():
        token = Tokens[position]
        position += 1
        return token

    def peek():
        return Tokens[position]

def read_str():
    return


def tokenize(string):
    x = 0
    t = 0
    tknarray = []

    # keep cycling until the string is consumed
    while len(string) > 0:
        
        # match whitespace and move string pointer   
        wspace = re.match("[\s,]*", string)
        if wspace != None:
            string = string[len(wspace.group()):]

        tildeat = re.match("~@", string)
        if tildeat != None:
            tknarray.append(tildeat.group())
            string = string[len(tildeat.group()):]
            
        # match the semicolon starting text
        semitext = re.match(";.*",string)
        if semitext != None:
            tknarray.append(semitext.group())
            string = string[len(semitext.group()):]

#        print("MID: " + string)
#        print(tknarray)
        
        if len(string) > 0 and string[0] == '"':
            dblquote = re.match('"(?:\\.|[^\\"])*"?', string)
            dblstring = dblquote.group()
            if dblquote != None and dblstring[len(dblstring)-1] == '"':
                tknarray.append(dblstring)
                string = string[len(dblstring):]
            else:
                print('Missing double quote...')
                break;
        
    return tknarray

