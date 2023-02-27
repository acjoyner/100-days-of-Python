# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data.to_dict())
#
#
# temp_list = data["temp"].to_list

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = data["Primary Fur Color"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count= len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count= len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")