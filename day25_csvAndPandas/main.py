# with open("weather_data.csv") as file1:
#     data = file1.readlines()


# import csv

# with open("weather_data.csv") as file1:
#     data = csv.reader(file1)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# Challenge: calculate the average temperature
# Alternative 1: "by hand":

temp_list = data["temp"].to_list()

print(sum(temp_list) / len(temp_list))


# Alternative 2: the real one
print(data["temp"].mean())

# Challenge 2: what was the max temp

print(data["temp"].max())

# The notation data.temp is valid:
print(data.temp)

# getting rows is similar to data.table
print(data[data["day"] == "Monday"])
print(data[data.day == "Monday"])

monday = data[data.day == "Monday"]
print(monday.temp)

# Challenge 3: convert temps to fahrenheit

# data.fahrenheit = 1.8 * data.temp + 32 ## generates an error because creating new attributes is not allowed.
# the correct code is:

data["fahrenheit"] = 1.8 * data.temp + 32

print(data)

# Creating a data frame from a dictionary

students_dictionary = {"Name": ["Amy", "John", "Susan"],
                       "Scores": [74, 73, 81]
                       }

students_data = pandas.DataFrame(students_dictionary)
print(students_data)
print(type(students_data))
students_data.to_csv("students_data.csv")
