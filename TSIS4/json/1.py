import json

file = open("sample-data.json")

data_json = file.read()
data = json.loads("data_json")
print(data["totalCount"])