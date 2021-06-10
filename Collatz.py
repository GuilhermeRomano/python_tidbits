import os


def collatz(number: int):
    if number % 2 == 0:
        quotient = number//2
        print(quotient)
        return quotient
    else:
        alternate = 3 * number + 1
        print(alternate)
        return alternate


number_input = None
while not isinstance(number_input, int):
    try:
        number_input = int(input("Enter number:\n"))
    except ValueError:
        os.system("cls")
        print("Insert a valid value.")

while number_input != 1:

    number_input = int(collatz(number_input))
