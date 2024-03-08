import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

camel_case = input()

print(re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower())
file.close()