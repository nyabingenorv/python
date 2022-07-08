def calculator(num1,num2,o):
    if o == "+":
        return num1 + num2
    elif o == "-":
        return num1 - num2
    elif o == "/":
        return num1 / num2
    elif o == "*":
        return num1 * num2
    
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
op = input("enter operator either + - / * ")

print(calculator(num1,num2,op))