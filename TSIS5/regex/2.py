import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

print(re.findall(r'ab{2,3}', text))
file.close()