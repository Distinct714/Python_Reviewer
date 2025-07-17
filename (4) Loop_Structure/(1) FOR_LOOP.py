# For Loop ( ITERATION )

# For loop is a function that allows to loop over a sequence or same instructions with specific or limited number of times.
# It also used to repeat a specific block of code in known number of times.
# Its also iterate over items of a collection (sequence) so that they appear on console.

# The initial loop statement must be followed by a colon : symbol. This signals the start of the iteration block.
# Beside the 'for' takes items in iterable object one by one and beside the 'in' is an iterable object.

# The following will print vertically:

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for phrase in "Joshua Restaurant":      
    print(phrase)

# If you want to print horizontal, use end="".This defines what is printed at the end of the line of statement.
for phrase2 in "Joshua Restaurant\n":
    print(phrase2, end="")

# Adding f-string inside a for loop:
foods = ["Pizza", "Burrito", "Burger"]

for food in foods:
    print(f"I like {food}.")

# You can also apply other functions or methods here.


# Creating Triangle using For Loop and Range:
x = 8

for i in range(0, x):
    print("*" * i)


# Applying Conditional statements
foods = ["Pizza", "Burrito", "Burger"]

for index in range(3):
    if index == 0:
        print("First Choice")
    else:
        print("Second Choice")


# Using Range and length in for loop:
foods = ["Pizza", "Burrito", "Burger"]

for a in range(len(foods)):
    print(foods[a])

# ANOTHER SAMPLE (Use List Comprehension instead of this)
squares = []
for num in range(1, 11):
    num = num**2
    squares.append(num)
    print(squares)


# LOOP STATEMENTS

# The break statement is used to interrupt or stop loop when some conditions are met.
# The else block will NOT be executed if the loop is stopped by a break statement.
number = [1, 2, 3, 1, 4, 5, 6, 2, 2]

for i in number:
    if i == 2:
        print(i)
        break
print("\n")

# The continue statement is used to skip the current iteration of a loop when a certain condition is true.
# It will move to the next iteration without existing the loop.
numbers = [1, 2, 3, 1, 4, 5, 6, 2, 2]

for i in numbers:
    if i > 2:
        continue
    print(i)

# Same in having an assignment operators:
number = [1, 2, 3, 1, 4, 5, 6, 2, 2]
counter = 0

for i in number:
    if i == 2:
        counter += 1
print(counter)

print("\n")

# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.
# This will act as a placeholder.
for i in [1, 2, 3]:
    pass

# enumerate
letters = ["a", "b", "c"]

for n, m in enumerate(letters):
    print(n, ":", m)
