# with open("G:/AI/Python/Code/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for row in data:
#         print(row)

import csv

with open("G:/AI/Python/Code/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
            
    print(temperature)
