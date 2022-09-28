import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

sum_of_squirrels = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
new_data = pandas.DataFrame(sum_of_squirrels)
new_data.to_csv("Sum_of_squirrels")

