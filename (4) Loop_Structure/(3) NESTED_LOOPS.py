# NESTED LOOPS

# Nested loops, a concept where one loop operates within another, are crucial in programming.
# The first element in a variable is called outer loop iterations and 
# will end after all elements in inner loop iterations are called.
# Each iterations of the outer loop runs along the inner loop entirely.

# List with Nested loops 
foods = ["Pizza with", "Burrito with", "Burger with"]
drinks = ["Coffee", "Juice", "Softdrink"]

for food in foods:
    for drink in drinks:
        print(food, drink)


# You can also combined range and list here:
drinks = ["Coffee", "Juice", "Softdrink"]

for drink in drinks:
    for i in range(3):
        print(drink)


# Three iterations in outer loop
for x in range(3):
    for y in range(1, 5):
          print(y, end=" ")
    print()
    

# Multiplication Table Sample
print("-" * 20)
for a in range(1, 11): 
     for b in range(1, 11):
           print(f"{a} x {b} = {a * b}")
print("-" * 20)


# ROWS AND COLUMNS
rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))
symbols = input("Enter any Symbols: ")

for c in range(rows):
    for d in range(columns):
        print(symbols, end="")
    print()


# COMBINING FOR AND WHILE LOOPS AT THE SAME TIME
list1 = ['I am ', 'You are ']
list2 = ['good', 'bad', 'neutral']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to iterate through a list1.
for item in list1:
    # Printing outside inner loop
    print("start outer for loop ")

    # Initialize counter i with 0
    i = 0

    # Running inner While loop to iterate through a list2. It must have a condition, not list.
    while(i < list2_size):
        print(item, list2[i])   # Printing inside inner loop
        i += 1                 # Incrementing the value of i

    # Printing outside inner loop
    print("end for loop ")

# Use nested for loops instead of this.

# ADDING ELEMENTS TO THE EMPTY LIST WITH FOR LOOP
aliens =[]
for alien_number in range(5):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
# ================================================================
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = '10'
    
    for alien in aliens[:5]:
        print(alien)
# ================================================================
    print("...")
    print(f"Total number of aliens: {len(aliens)}")
