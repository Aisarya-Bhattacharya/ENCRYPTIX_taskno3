print("A program to create a calculator")

def addition(x,y):
    add=x+y
    return add
def subtraction(x,y):
    subtract=x-y
    return subtract
def multiplication(x,y):
    multiply=x*y
    return multiply
def division(x,y):
    if y !=0:
        divide=x/y
        return divide
    else:
        return("invalid")

num1= float(input("Enter 1st number:"))
num2= float(input("Enter 2nd number:"))
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
n= int(input("enter 1/2/3/4"))

if n==1:
    add=addition(num1,num2)
    print("The sum is:",add)

elif n==2:
    subtract= subtraction(num1,num2)
    print("The subtraction is:",subtract)

elif n==3:
    multiply= multiplication(num1,num2)
    print("The multipliation is:",multiply)

elif n==4:
    divide= division(num1,num2)
    print("The division is:", divide)

else:
    print("Invalid choice")
