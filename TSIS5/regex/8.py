import re

file = open("./row.txt", 'r', encoding='utf8')

text = file.read()

findall = re.sub(r'\w',text)
uppercase_string = ' '.join(letter.upper() for letter in findall)
print(uppercase_string)
file.close()