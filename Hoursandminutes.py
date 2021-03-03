#Given the integer N the number of minutes that is passed since midnight- how many hours and minutes are displaced on the 24 hour digital clock? The program should print two munbers the numbers of hours (between 0 and 23) and the number of minutes( between 0 and 59).
time=int(input("enter the number of minutes passed since midnight"))
hours_passed=time/60
minutes_passed=time%60
print(f"It has passed {hours_passed} hours and {minutes_passed} minutes since midnight")
N=int(input("enter the number of minutes passed since midnight"))
hours=(N/60)
minutes=(N%60)
print(f"The hours is {hours}")
print(f"The minutes is {minutes}")
print(f"Its {hours}:{minutes} now")

