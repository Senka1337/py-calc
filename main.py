print("Pick operation (+/-/*//)")
operation = input()
print("First num?")
num1 = int(input())
print("Second number?")
num2 = int(input())
print("The answer is:")
if operation == "+":
    print(num1+num2)
if operation == "-":
    print(num1-num2)
if operation == "*":
    print(num1*num2)
if operation == "/":
    print(num1/num2)