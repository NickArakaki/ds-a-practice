from datetime import datetime

date = "01-01-2023"
time = "16:00"

print(datetime.strptime(f'{date} {time}', "%d-%m-%Y %H:%M"))
