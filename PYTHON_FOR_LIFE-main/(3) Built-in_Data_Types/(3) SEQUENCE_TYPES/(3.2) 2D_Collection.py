# 2D COLLECTION AND NESTED LOOP

# In creating 2D lists, remember to add comma at the end of squared brackets because the lists is divided
# into four elements as shown below.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid, "\n")

# When you want to access inside the 2D list, add two pairs of squared brackets inside parenthesis.
# Remember, the index of first list starts at 0, and the second is the index of element inside of a list.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][0], "\n")

# You can also apply for loop in all list:

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    print(row)

for row in number_grid:
        for col in row:
            print(col)


# SAMPLE ONE
drinks = ["Water", "Juice", "Milk"]
meats = ["Chicken", "Pork", "Beef"]
fruits = ["Apple", "Banana", "Berries"]

foods = [drinks, meats, fruits]

print(foods, "\n")
print(foods[0][1])

# SAMPLE TWO
player_one = {"color": "green", "points": 5}
player_two = {"color": "yellow", "points": 10}
player_three = {"color": "red", "points": 15}

players = [player_one, player_two, player_three]

for player in players:
    print(f"Output: {player}")     


# You can create 2D tuple here:

nums = (
     (1, 2, 3),
     (4, 5, 6),
     (7, 8, 9),
     (0)
)

for row in nums:
    print(row)