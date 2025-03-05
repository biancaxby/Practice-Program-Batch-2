#Print how many are even numbers.
def even_count():
    num = []
    
    for i in range(10):
        while True:
            try:
                number = int(input(f'Enter a number: '))
                num.append(number)
                break
            except ValueError:
                print("hah")

even_count_1 = sum(1 for n in num if n % 2 == 0)

print(f"there are {even_count_1} number/s.")

even_count()