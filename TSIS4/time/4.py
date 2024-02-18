import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

diff = int(yesterday.strftime("%H")) * 3600
print(diff)