#Print how many are even numbers.
def even_count():
    number = []
    
    for i in range(10):
        while True:
            try:
                num = int(input(f'Enter a number: '))
                number.append(num)
                break
            except ValueError:
                print("Error. Enter an integer.")
    even_count_1 = sum(1 for number in num if num % 2 == 0)
    print(f"there are {even_count_1} number/s.")

even_count()