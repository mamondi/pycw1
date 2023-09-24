num1 = int(input("Початок діапазону: "))
num2 = int(input("Кінець діапазону: "))

while num1 <= num2:
    print(num1, end="\f")
    if num1 % 3==0:
        print("Fizz", end=' ')
    if num1 % 5==0:
        print("Buzz", end=' ')
    num1 += 1
    print()