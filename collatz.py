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
    count = 0
    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number //= 2
        print_sequence(number)
        count += 1
        continue
    print(f"\nReached 1 in {count} iterations.")


def print_sequence(number):
    global prefix
    global prefix_count
    print(f"{prefix * prefix_count} {number}")
    prefix_count += 1


gather_input()
