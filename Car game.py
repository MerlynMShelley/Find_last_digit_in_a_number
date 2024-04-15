command = ""
started = False
while True:
    command = input (">").lower()
    if command == "start":
        if started:
            print("The car is already started and running!")
        else:
            started = True
            print("The Car is Started ... Ready to Go!")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("The Car is stopped!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand the command!")
