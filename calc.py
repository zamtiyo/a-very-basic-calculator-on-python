num1 = int(input("Enter a number :"))
operator = input("Enter an operator /x-+: ")
num2 = int(input("Enter a second number :"))

if operator == "x":
    print(f"The answer is {num1 * num2}")
elif operator == "+":
    print(f"The answer is {num1 + num2}")
elif operator == "-":
     print(f"The answer is {num1 - num2}")
elif operator == "/":
    print(f"The answer is {num1 / num2}")
else:
    print("Invalid")

