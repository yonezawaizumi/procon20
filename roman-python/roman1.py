import re
import sys

def eat_thousand(chrs):
    if len(chrs) == 0:
        print('empty')
        return -1
    c = chrs.pop()
    if c != 'M':
        chrs.append(c)
        return 0
    if len(chrs) == 0:
        return 1000
    c2 = chrs.pop()
    if c2 != 'M':
        chrs.append(c2)
        return 1000
    if len(chrs) == 0:
        return 2000
    c3 = chrs.pop()
    if c3 != 'M':
        chrs.append(c3)
        return 2000
    if len(chrs) == 0:
        return 3000
    c4 = chrs.pop()
    if c4 != 'M':
        chrs.append(c4)
        return 3000
    print('too many M')
    return -1

def eat_hundred(chrs):
    if len(chrs) == 0:
        print('empty')
        return -1
    c = chrs.pop()
    if c == 'C':
        if len(chrs) == 0:
            return 100
        c2 = chrs.pop()
        if c2 == 'M':
            return 900
        elif c2 == 'D':
            return 400
        elif c2 == 'C':
            if len(chrs) == 0:
                return 200
            c3 = chrs.pop()
            if c3 != 'C':
                chrs.append(c3)
                return 200
            if len(chrs) == 0:
                return 300
            c4 = chrs.pop()
            if c4 != 'C':
                chrs.append(c4)
                return 300
            print('too many C')
            return -1
        else:
            chrs.append(c2)
            return 100
    elif c == 'D':
        if len(chrs) == 0:
            return 500
        c2 = chrs.pop()
        if c2 == 'C':
            if len(chrs) == 0:
                return 600
            c3 = chrs.pop()
            if c3 != 'C':
                chrs.append(c3)
                return 600
            if len(chrs) == 0:
                return 700
            c4 = chrs.pop()
            if c4 != 'C':
                chrs.append(c4)
                return 700
            if len(chrs) == 0:
                return 800
            c5 = chrs.pop()
            if c5 != 'C':
                chrs.append(c5)
                return 800
            print('too many C')
            return -1
        else:
            chrs.append(c2)
            return 500
    else:
        chrs.append(c)
        return 0
    
def eat_ten(chrs):
    if len(chrs) == 0:
        print('empty')
        return -1
    c = chrs.pop()
    if c == 'X':
        if len(chrs) == 0:
            return 10
        c2 = chrs.pop()
        if c2 == 'C':
            return 90
        elif c2 == 'L':
            return 40
        elif c2 == 'X':
            if len(chrs) == 0:
                return 20
            c3 = chrs.pop()
            if c3 != 'X':
                chrs.append(c3)
                return 20
            if len(chrs) == 0:
                return 30
            c4 = chrs.pop()
            if c4 != 'X':
                chrs.append(c4)
                return 30
            print('too many X')
            return -1
        else:
            chrs.append(c2)
            return 10
    elif c == 'L':
        if len(chrs) == 0:
            return 50
        c2 = chrs.pop()
        if c2 == 'X':
            if len(chrs) == 0:
                return 60
            c3 = chrs.pop()
            if c3 != 'X':
                chrs.append(c3)
                return 60
            if len(chrs) == 0:
                return 70
            c4 = chrs.pop()
            if c4 != 'X':
                chrs.append(c4)
                return 70
            if len(chrs) == 0:
                return 80
            c5 = chrs.pop()
            if c5 != 'X':
                chrs.append(c5)
                return 80
            print('too many X')
            return -1
        else:
            chrs.append(c2)
            return 50
    else:
        chrs.append(c)
        return 0
    
def eat_one(chrs):
    if len(chrs) == 0:
        print('empty')
        return -1
    c = chrs.pop()
    if c == 'I':
        if len(chrs) == 0:
            return 1
        c2 = chrs.pop()
        if c2 == 'X':
            return 9
        elif c2 == 'V':
            return 4
        elif c2 == 'I':
            if len(chrs) == 0:
                return 2
            c3 = chrs.pop()
            if c3 != 'I':
                chrs.append(c3)
                return 2
            if len(chrs) == 0:
                return 3
            c4 = chrs.pop()
            if c4 != 'I':
                chrs.append(c4)
                return 3
            print('too many I')
            return -1
        else:
            chrs.append(c2)
            return 1
    elif c == 'V':
        if len(chrs) == 0:
            return 5
        c2 = chrs.pop()
        if c2 == 'I':
            if len(chrs) == 0:
                return 6
            c3 = chrs.pop()
            if c3 != 'I':
                chrs.append(c3)
                return 6
            if len(chrs) == 0:
                return 7
            c4 = chrs.pop()
            if c4 != 'I':
                chrs.append(c4)
                return 7
            if len(chrs) == 0:
                return 8
            c5 = chrs.pop()
            if c5 != 'I':
                chrs.append(c5)
                return 8
            print('too many I')
            return -1
        else:
            chrs.append(c2)
            return 5
    else:
        chrs.append(c)
        return 0

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
    value = parse(mod[1] if len(mod) > 1 else "")
    if value != int(mod[0]):
        print("illegal format {0} ('{1}' result {2})".format(mod[0], mod[1], value))
 