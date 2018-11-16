#!/usr/bin/python3

class InGameSecond:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        try:
            s = int(self.value)
            return s % 4
        except ValueError:
            print("Please enter a valid number.\n")

    def to_password(self):
        switch = {
            0: self.zero,
            1: self.one,
            2: self.two,
            3: self.three,
        }

        method = switch.get(self.calculate())
        
        if not method:
            raise NotImplementedError("You just fucked up the program with some weird shit buddy.")

        return method()

    def zero(self):
        return "The password is MAKO (5)."

    def one(self):
        return "The password is KING (2)."

    def two(self):
        return "The password is BEST (1)."

    def three(self):
        return "The password is BOMB (4)."


def passList():
    for x in range(61):
        if x % 4 == 0:
            print(str(x).zfill(2),'MAKO')

        if x % 4 == 1:
            print(str(x).zfill(2),'KING')
        
        if x % 4 == 2:
            print(str(x).zfill(2),'BEST')

        if x % 4 == 3:
            print(str(x).zfill(2),'BOMB')


def checkInput(userInput):
    if userInput not in ("input", "list", "quit"):
        return False

    return True


def main():
    value = True
    
    while value == True:
        userInput = input("Please type input, list, or quit: ").lower()
        
        if checkInput(userInput) == True:
            value = False
        else:
            continue

        if userInput == "quit":
            exit()

        if userInput == "list":
            passList()

        if userInput == "input":
            timeInput = input("Please type in-game second: ")
            time = InGameSecond(timeInput)
            print(time.to_password())
    else:
        exit()

main()