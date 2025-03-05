#Print the result of the first number minus all of the remaining numbers.
total = 0
num = int(input('type in number: '))
for i in range(1,4):
    total += int(input(f'enter a number: '))
    x = num - total


print(x)


