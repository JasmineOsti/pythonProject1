#N students take K apples and istributes them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the number N and K. It should print the two answers for the question above.
students=int(input("enter the number of students:"))
apple=int(input("enter the number of apples:"))
std_apple= apple//students
rem= apple%students
print("the students get{std_apple} and the remaining apples are {rem}")