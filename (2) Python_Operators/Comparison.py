
# COMPARISON OR RELATIONAL OPERATORS

# <, >, <=, >= and == are comparison operators use in comparing variables.
# != is another operator for not equal.

# IF-ELIF-ELSE STATEMENTS FUNCTION

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(5,7,9))


num: int = 10

if num >= 5:
    print("Yes")
else:
    print("No")


# TERNARY OPERATOR (Conditional Expressions)

# The ternary operator in Python is simply a shorter way of writing an if and if...else statements.
# true_value if condition - else false_value

def max_nums(nums1, nums2):
    return nums1 if nums1 >= nums2 else nums2

print(max_nums(19,13))
