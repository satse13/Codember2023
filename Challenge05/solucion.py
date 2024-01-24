import re

def userChek(info): 
    fields = info.split(',')
    rules = {
        0: str.isalnum,
        1: str.isalnum,
        2: lambda s: re.match(r"[^@]+@[^@]+\.[^@]+", s) is not None,
        3: str.isdigit,
        4: lambda s: isinstance(s, str)
    }

    for i, field in enumerate(fields):
        if i in rules and not rules[i](field):
            return fields[1][0]

    return ""

solucion = ""

with open("Challenge05/input.txt", "r") as f:
    for line in f: 
        solucion += userChek(line)

print(solucion)