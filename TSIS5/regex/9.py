import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

print(re.sub(r'([a-z])([A-Z])', r'\1 \2', text))
file.close()