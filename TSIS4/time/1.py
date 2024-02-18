import datetime

today = datetime.datetime.now()
fivedaysago = datetime.timedelta(days=5)

print(today - fivedaysago)