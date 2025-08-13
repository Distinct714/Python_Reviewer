# While Loop ( ITERATION )

# While Loop is a structure that allows to loop through or repeatedly and execute a block of codes in multiple times.
# It is a statement that will execute a block of code, as long as it's condition remains True.
# Otherwise, it will stop executing the block of codes if it false.
# As with for loops, the initial while loop statement must be followed by a colon : symbol.

# In the right side of a while loop is called flag. A flag in Python acts as a signal to the program to determine whether or 
# not the program as a whole or a specific section of the program should run.
# In other words, you can set the flag to True or anything and the program will run continuously until any type of event makes it False. 
# Then the program, loop, or whatever you're using a flag for will stop.
while True:
   print("test")
   break

# In general, use for loops when you already know the number of iterations, and 
# while loops when there is a condition that needs to be met.

# You can use some python operators in the flag of a function.
name = input("Enter Your Name: ")

while not name == "q":
    print(f"Your output is {name}")
    name = input("Call it quit?: ")
print("Done")

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
# Below the print(i) is called counter, where a variable keeps track the number of iterations. Counters help you avoid infinite loops.
# Remember to increment i, or else the loop will continue forever.
# Without counter, the code will run forever or as what we called infinite loops.
i = 10

while i > 0:
    print(f"Next number is: {i}")
    i -= 2
    if i == 2:
       print("Last Number is: 2")
       break
print("Done")


# You can apply else statement here and run a block of code once when the condition no longer is true:
i = 1

while i <= 15:
  print(i)
  i += 1
else:
  print("i is no longer less than 15")

# SAMPLE ONE
sentence = "Guido van Rossum is the creator of Python. Correct? "
active = True

while active:
  message = input(sentence)
  if message == "q":
    active = False
  else:
    print(message)


# SAMPLE TWO
current_number = 0

while current_number <=20:
   current_number += 1
   if current_number % 2 == 0:
      continue
   print(current_number)


# SAMPLE THREE
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Black"]

while "Black" in colors:
   colors.remove("Black")
print(colors)


# SAMPLE FOUR
release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon!")

  else:
    print("Available now!")
  
  # Increment current_date by one
  current_date += 1
