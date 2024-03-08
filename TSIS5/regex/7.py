import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

def toCamel(str):
    pos = str.find("_")
    res = str[:pos] + str[pos + 1].upper() + str[pos + 2:]
    print(re.sub('_', '', res))
toCamel('alisher_baudinov')
file.close()