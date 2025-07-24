# PYTHON MATCH CASE STATEMENT

# Unlike traditional if-elif-else chains, which can become unwieldy with complex conditions, 
# the match-case statement provides a more elegant and flexible solution.
def check_number(x):
    match x:
        case 5:
            print("It's 5")
        case 10:
            print("It's 10")
        case _:
            print("A number must be 5 and 10 only")

check_number(10)
check_number(30)

# MAKING A CALCULATOR USING MATCH CASE STATEMENT WITH TRY-EXCEPT 
while True:
    try:
        value1 = float(input("Enter Your Number:"))
        operator = input("Enter Your Operator:")
        value2 = float(input("Enter Another Number:"))

        match operator:
            case "+":
                print(value1 + value2)
            case "-":
                print(value1 - value2)

            case "*":
                print(value1 * value2)

            case "^":
                print(value1 ** value2)

            case "/":
                print(value1 / value2)

            case "//":
                print(value1 // value2)

            case "%":
                print(value1 % value2)

            case _:
                print("InvaLid Operator")
    except:
        print("Input Number Only.")

    retry = input("Continue? Enter Yes or No only.")
    if retry == "No":
        break
    else:
        continue
        
