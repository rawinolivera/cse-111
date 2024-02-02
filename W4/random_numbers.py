import random

def append_random_numbers(number_list, quantity = 1):
    for _ in range (quantity):
        number_list.append(round(random.uniform(0, 100), 1))

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)




if __name__ == "__main__":
    main()