import re

str = input()
regex = "^([a-zA-Z]+[0-9]*)*@[a-zA-Z]+\.[a-zA-Z]+$"
if re.fullmatch(regex, str) == None:
    print("WRONG")
else:
    print("OK")