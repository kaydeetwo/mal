import re

mal = []

class Reader:
    def __init__(self, tokens, position):
        self.tokens = tokens
        self.position = position

    def next(self):
        token = self.tokens[self.position]
        self.position += 1
        return token

    def peek(self):
        return self.tokens[self.position]

    def print(self, type):
        print(type)
        # print('TOKENS')
        # print(self.tokens)
        print('Current token: ', self.tokens[self.position])
        

              
def read_str(string):
    reader = Reader(tokenize(string),0)
    # print(reader.tokens)
    return read_form(reader)


def read_form(reader):

    if reader.peek() == '(':
        reader.next()
        # reader.print("rf_lpf")
        return read_list(reader)
    else:
        # reader.print("rf_nlpf")
        return read_atom(reader)


def read_list(reader):
    itemlist = []
    while 1:
        temp = read_form(reader)
 #       reader.print("rl")
        if temp == ')':
            break;
        else:
            itemlist.append(temp)
            if reader.position == len(reader.tokens):
                break;
        reader.next()
    # print('rl_itemlist:', itemlist)
    return itemlist


def read_atom(reader):
   # reader.print("ra")
    if reader.peek().isnumeric():
        return int(reader.peek())
    else:
        return str(reader.peek())

    assert False, "Unreachable (probably invalid input string)."
    return


def tokenize(string):
    tknarray = []
    prev_string = ''
    # print(string)
    
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
        semitext = re.match(";.*", string)
        if semitext != None:
            tknarray.append(semitext.group())
            string = string[len(semitext.group()):]

        # print("MID:" + string)
        # match the double quote string, and throw error if no closing quote
        if len(string) > 0 and string[0] == '"':
            dblquote = re.match('"(?:\\.|[^\\"])*"?', string)
            dblstring = dblquote.group()
            if dblquote != None and dblstring[len(dblstring)-1] == '"':
                tknarray.append(dblstring)
                string = string[len(dblstring):]
            else:
                print('Missing double quote...')
                print('Segment: <start>' + dblstring + '<end>')
                break;

        # match the special characters
        specchar = re.match("[\[\]{}()'`~^@]", string)
        if specchar != None:
            tknarray.append(specchar.group())
            string = string[len(specchar.group()):]

        nonspecchar = re.match('[^\s\[\]{}(\'"`,;)]*', string)
        nscstring = nonspecchar.group()
        if nonspecchar != None and len(nscstring) > 0:
            tknarray.append(nonspecchar.group())
            string = string[len(nonspecchar.group()):]

        # Check if functions are not tokenizing any further,
        # throw error if matches prior cycle

        # print('MID:' + string + '\n')

        if len(string) > 0:
            if string == prev_string:
                assert False, "Stuck processing tokens."
        else:
                break
        prev_string = string

    return tknarray

