import random


def input_numb():
    """
    Get 6 numbers from keyboard
    :return:
    """
    chosen_numbers = []
    while len(chosen_numbers) < 6:
        try:
            numbers = int(input("Choose 6 numbers between 1 and 49: "))
            if numbers not in chosen_numbers and 0 < numbers <= 49:
                chosen_numbers.append(numbers)
            sorted_numbers = sorted(chosen_numbers)
        except ValueError:
            print("Only numbers!")
    return sorted_numbers


def random_choice():
    """
    Computer choose 6 random numbers
    :return:
    """
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    """
    Main function, compare user numbers with computer numbers
    :return:
    """
    user_numbers = input_numb()
    print(f"Your numbers: {user_numbers}")

    computer_numbers = random_choice()
    print(f"Computer numbers: {computer_numbers}")

    hits = 0
    for number in user_numbers:
        if number in computer_numbers:
            hits += 1
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
