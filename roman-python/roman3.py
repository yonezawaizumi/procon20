import re
import sys

r = re.compile("""^(M{0,3})(CM|DC{0,3}|CD|C{0,3})(XC|LX{0,3}|XL|X{0,3})(IX|VI{0,3}|IV|I{0,3})$""")

def parse_thousand(str):
    return len(str) * 1000

def parse_hundred(str):
    if not str:
        return 0
    elif str == 'CM':
        return 900
    elif str == 'CD':
        return 400
    elif str[0] == 'D':
        return 500 + (len(str) - 1) * 100
    else:
        return len(str) * 100

def parse_ten(str):
    if not str:
        return 0
    elif str == 'XC':
        return 90
    elif str == 'XL':
        return 40
    elif str[0] == 'L':
        return 50 + (len(str) - 1) * 10
    else:
        return len(str) * 10

def parse_one(str):
    if not str:
        return 0
    elif str == 'IX':
        return 9
    elif str == 'IV':
        return 4
    elif str[0] == 'V':
        return 5 + len(str) - 1
    else:
        return len(str)

def parse(str):
    if len(str) == 0:
        return -1
    m = r.match(str)
    if m is None:
        return -1
    else:
        return parse_thousand(m.group(1)) + \
            parse_hundred(m.group(2)) + \
            parse_ten(m.group(3)) + \
            parse_one(m.group(4))
    

for line in sys.stdin:
    mod = line.rstrip().split(None, 1)
    value = parse(mod[1] if len(mod) > 1 else "")
    if value != int(mod[0]):
        print("illegal format {0} ('{1}' result {2})".format(mod[0], mod[1], value))
