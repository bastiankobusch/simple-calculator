print("Simple Calculator")
print()
#User input
num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

#Perform calculation
if operator == "+":
    result = num1 + num2
    print()    
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print()  
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print()  
    print(round(result, 3)) 

elif operator == "/":
    result = num1 / num2
    print()  
    print(round(result, 3))

else:
    result = "Error"

input("\n\n\nPress Enter to exit.")