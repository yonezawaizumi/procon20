import re
import sys

def eat_repeat(chrs, c, max):
    count = 0
    while len(chrs) > 0:
        cc = chrs.pop()
        if cc != c:
            chrs.append(cc)
            break
        count += 1
        if count > max:
            return -1
    return count 

def eat_digit(chrs, one, five, ten, mul):
    if len(chrs) == 0:
        print('empty')
        return -1
    c = chrs.pop()
    if c == one:
        v = eat_repeat(chrs, one, 2)
        if v > 0:
            return mul * (v + 1)
        elif v < 0:
            return v
        if len(chrs) == 0:
            return mul
        c2 = chrs.pop()
        if c2 == ten:
            return mul * 9
        elif c2 == five:
            return mul * 4
        else:
            chrs.append(c2)
            return mul
    elif c == five:
        v = eat_repeat(chrs, one, 3)
        if v >= 0:
            return mul * (v + 5)
        else:
            return v
    else:
        chrs.append(c)
        return 0

def eat_thousand(chrs):
    return eat_digit(chrs, 'M', '', '', 1000)

def eat_hundred(chrs):
    return eat_digit(chrs, 'C', 'D', 'M', 100)
    
def eat_ten(chrs):
    return eat_digit(chrs, 'X', 'L', 'C', 10)
    
def eat_one(chrs):
    return eat_digit(chrs, 'I', 'V', 'X', 1)

def parse(str):
    chrs = list(str)
    chrs.reverse()
    v = eat_thousand(chrs)
    if v < 0:
        return -1
    value = v
    if len(chrs) > 0:
        v = eat_hundred(chrs)
        if v < 0:
            return v
        value += v
    if len(chrs) > 0:
        v = eat_ten(chrs)
        if v < 0:
            return v
        value += v
    if len(chrs) > 0:
        v = eat_one(chrs)
        if v < 0:
            return v
        value += v
    if len(chrs) > 0:
        print('illegal ' + chrs.pop())
        return -1
    else:
        return value

for line in sys.stdin:
    mod = line.rstrip().split(None, 1)
    value = parse(mod[1])
    if value != int(mod[0]):
        print("illegal format {0} ('{1}' result {2})".format(mod[0], mod[1], value))
