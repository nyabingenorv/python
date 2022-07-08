asset = """

            _      
           | |     
   ___ __ _| | ___ 
  / __/ _` | |/ __|
 | (_| (_| | | (__ 
  \___\__,_|_|\___|
                   
                   

"""

def calculator(num1,num2,o):
    if o == "+":
        return num1 + num2
    elif o == "-":
        return num1 - num2
    elif o == "/":
        return num1 / num2
    elif o == "*":
        return num1 * num2
print(asset)
print("WELCOME TO THE CALCULATOR")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
op = input("enter operator either (+ - / * )")

print(f"the answer is {calculator(num1,num2,op)}")
