import pandas

squirrel_color = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_color)

summary_color = squirrel_color.groupby(["Primary Fur Color"]).size() # this is a Series

# to rename the column:

# squirrel_color.groupby(["Primary Fur Color"]).size().reset_index(name = "Cantidad") # this preserves the name of the first column

# Alternatively:
# summary_color = squirrel_color["Primary Fur Color"].value_counts() # This too, is a Series

# To rename the column:
# squirrel_color["Primary Fur Color"].value_counts().reset_index(name = "efsf") # this sets the name of the count column, bu the first column is called "index"

# If I wanted a data frame, then I'll need as_index = False:
# summary_color = squirrel_color(["Primary Fur Color"], as_index = False).size()

summary_color.to_csv("summaryColor.csv")
