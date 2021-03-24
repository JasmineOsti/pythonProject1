#product=1
#num=int(input("enter a number"))
#for i in range(1,num+1):
#    product= product*i
#print(product)
def sum():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    answer=num1+num2
    print(f'the sum of {num1} and {num2} is {answer}')

def sub():
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    answer = num1 - num2
    print(f'the substraction of {num1} and {num2} is {answer}')

def mul():
    num1=int(input("enter the first number:"))
    num2=int(input("Enter the second number:"))
    answer=num1*num2
    print(f'the multiplication of {num1} and {num2} is {answer}')
def div():
    num1=int(input("enter the first number:"))
    num2=int(input("Enter the second number:"))
    answer=num1/num2
    print(f'the division of {num1} and {num2} is {answer}')
sum()
sub()
mul()
div()\

def sum(a,b):
    c=a+b
    print(f"the sum of {a} and {b} is {c}")
a=int(input("enter first number:"))
b = int(input("enter second number:"))
sum(a,b)


