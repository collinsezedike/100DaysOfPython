import pandas

# data = []
# with open("weather_data.csv") as chart:
#     for row in chart.readlines():
#         data.append(row.strip())
# print(data)

# import csv
#
# with open("weather_data.csv") as chart:
#     data = csv.reader(chart)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

#
# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # to get the average temperature
# # with Python functions
# avg = sum(temp_list) / len(temp_list)
# print(round(avg, 2))
# # with pandas functions
# print(data["temp"].mean())
#
# # to find the maximum temperature
# print(data["temp"].max())
#
#
# # get data columns
# print(data["condition"])
# # or
# print(data.condition)
#
# # get data row
# print(data[data.day == "Monday"])
#
# # print row with the highest temperature
# print(data[data.temp == data.temp.max()])
#
# # get a item under a category in a row
# monday = data[data.day == "Monday"]
# mon_temp_in_F = int(monday.temp) * 9 / 5
# print(mon_temp_in_F)
#
# # create a data frame from scratch
# data_dict = {
#     "students":  ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_column = data["Primary Fur Color"]
grey_fur_count = len(data[fur_column == "Gray"])
red_fur_count = len(data[fur_column == "Cinnamon"])
black_fur_count = len(data[fur_column == "Black"])

data_dict = {
    "Fur Colour": ["grey", "red", "black"],
    "Count": [grey_fur_count, red_fur_count, black_fur_count]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")
