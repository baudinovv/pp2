import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

print(re.findall(r'\b[a-z]+_[a-z]+\b', text))
file.close()