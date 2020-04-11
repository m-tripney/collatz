prefix = "."
prefix_count = 1


def gather_input():
    try:
        user_input = int(input("Please choose an integer greater than 1:  "))
        if user_input >= 1 and type(user_input) == int:
            collatz(user_input)
        else:
            print("** Number must be greater than 1!")
            gather_input()
    except ValueError:
        print("** Please enter an integer.")
        gather_input()


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        print(number)
        collatz(number)
        break


def print_sequence(number):
    global prefix
    global prefix_count
    print(f"{prefix * prefix_count} {number}")
    prefix_count += 1


gather_input()
