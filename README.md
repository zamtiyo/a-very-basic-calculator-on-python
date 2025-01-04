so this is my first python project so im sorry if theres any mistake because im still learning and im also a begginer 
also i need some feedback from you guys so that i can became a better programmer

this is the code:

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

