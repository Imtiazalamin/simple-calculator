# python program to create a simple calculator
# 3 step a amader project hobe
#  1. function for operation
#  2. user input
#  3. print result


#step 1 create function

# function to add two numbers
def  add(num1,num2):
    return num1 + num2

# function to subtraction two number
def sub(num1,num2):
    return num1 - num2

# function to multiply two number
def multiply(num1,num2):
    return num1 * num2

# function to divide two number
def divide(num1,num2):
    return num1 / num2

# function to average two number
def avg(num1,num2):
    return (num1 + num2)/2

# user input
print("please select a operation:\n " \
      "1. ADDITION\n " \
      "2. substraction\n " \
      "3. multiplication\n" \
      "4.division\n " \
      "5.average\n ")

select = int(input('Select a operation from 1,2,3,4,5:'))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# step-3 print the result
if select == 1:
    print(number1, "+", number2, "= ", add(number1,number2))

elif select == 2:
    print(number1, "-", number2, "= ", sub(number1,number2))

elif select == 3:
    print(number1, "*", number2, "= ", multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "= ", divide(number1,number2))

elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2" "= ", avg(number1, number2))

else:
    print("Invalid operation! please try Again! ")