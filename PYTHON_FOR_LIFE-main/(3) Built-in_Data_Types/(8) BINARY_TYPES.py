# BINARY TYPES

# There are 8 bits in a byte. Bits either consist of a 0 or a 1

# byte      - It can be interpreted in different ways, like binary octal or hexadecimal
x = b"Hello"
print(x)

# Bytearray - It allows modification in a set of bytes.
bytesArr = bytearray(b'\x00\x0F')

bytesArr[0] = 255
bytesArr.append(255)
print(bytesArr)

# Another Sample
y = bytearray(9)
print(y)

# memoryview - It is used to create a memory view object that allows us to access and manipulate the 
# internal data of an object without copying it
z = memoryview(bytes(4))
print(z)
