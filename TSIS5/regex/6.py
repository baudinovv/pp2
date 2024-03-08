import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

print(re.sub(r',.', ';' ,text))
file.close()