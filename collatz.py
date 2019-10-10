prefix = "."
prefix_count = 1


def gather_input():
    try:
        user_input = int(input("Please choose a number greater than 1:  "))
        if user_input:
            collatz(user_input)
        else:
            print("** Number must be greater than 1!")
            gather_input()
    except ValueError:
        print("** Please enter an integer.")
        gather_input()


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print_sequence(number)
        collatz(number)
    elif number != 1:
        number = 3 * number + 1
        print_sequence(number)
        collatz(number)


def print_sequence(number):
    global prefix
    global prefix_count
    print(f"{prefix * prefix_count} {number}")
    prefix_count += 1


gather_input()
