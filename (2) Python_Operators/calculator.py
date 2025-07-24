# Better Calculator using Conditional Functions with TRY AND EXCEPT FUNCTION

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

            case "":
                print("InvaLid Operator")

    except:
        print("Input Number Only.")

    retry = input("Continue? Enter Yes or No only.")
    if retry == "No":
        break
    else:
        continue