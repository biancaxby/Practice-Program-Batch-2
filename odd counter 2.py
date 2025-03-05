def count_odd_numbers():
    numbers = []

    # Prompt user to input 10 numbers
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Count odd numbers
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    print(f"You entered {odd_count} odd number(s).")

# Call the function
count_odd_numbers()
