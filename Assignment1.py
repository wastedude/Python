num1 = int(input(print("Enter a number:")))
num2 = int(input(print("Enter another number:")))

operation = input(print("What operation would you want to do to them(+,x,/,-): "))

if operation == '+':
    total = num1+num2
    print(total)

elif operation == "x":
    total = num1*num2
    print(total)

elif operation == "/":
    total = num1/num2
    print(total)

elif operation == "-":
    total = num1-num2
    print(total)
