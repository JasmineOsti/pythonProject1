print("type help")
help=input('enter command')

command= input("enter").lower()
if command== help:
    print("start - to start car \n stop - to stop the care \n quit- to quit")
elif command== 'start':
    print("the car has started")
elif command== 'stop':
    print("the car has stopped")
elif command== 'quit':
    print("Game Over")
else:
    print("enter a valid input")

