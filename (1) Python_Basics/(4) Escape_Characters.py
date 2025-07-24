# ESCAPE CHARACTERS

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# Whitespace is a non-printing characters and its include spaces, tabs, newlines and other characters that create space in text.

# You can also use double backslash \\ to insert one backslash.
phrase1 = "I am Unknown\\Guy."
print(phrase1)

# \n function is a special character that is used when we need to end the current line and start a new line.
# It is used to create a new line in the string or file.
phrase2 = "I am\nUnknown Guy."
print(phrase2)

# \' or \" function is a special character used to insert single or double quotation in a string value.
quotes = "It\'s Distinct."
print(quotes) 

phrase3 = "I am \"Unknown\" Guy."
print(phrase3)

# \t function is a special character that allows inserting a space or tab between two or more words.
phrase4 = "It was\tDISTINCT."
print(phrase4)

# \b function is a special character that represents the backspace character. 
phrase5 = 'Hey \bDistinct.'
print(phrase5)

# \r    Carriage Return: A special character that is used to move the cursor to the beginning of the line, 
#       effectively "returning" it to the start.
phrase6 = "Do some\rwork!"
print(phrase6)

# \f    Form Feed: A special character in the ASCII character set that has a few specific uses.
phrase7 = "Do some work!\fADVICE:"
print(phrase7)

# \ooo  Octal value: A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

# \xhh  Hex value: A backslash followed by an 'x' and a hex number represents a hex value:
txt2 = "\x48\x65\x6c\x6c\x6f"
print(txt2) 
