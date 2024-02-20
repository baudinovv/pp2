import json

file = open("sample-data.json")

data_json = file.read()
data = json.loads(data_json)
print("Interface Status \n" + "================================================================================\n DN                                                 Description           Speed    MTU  \n -------------------------------------------------- --------------------  ------  ------\n" + data["imdata"][0]["l1PhysIf"]["attributes"]["dn"] + "                              " + data["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"] + " " + data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])
print(data["imdata"][1]["l1PhysIf"]["attributes"]["dn"] + "                              " + data["imdata"][1]["l1PhysIf"]["attributes"]["fecMode"] + " " + data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])
print(data["imdata"][2]["l1PhysIf"]["attributes"]["dn"] + "                              " + data["imdata"][2]["l1PhysIf"]["attributes"]["fecMode"] + " " + data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])
