num1 = int(input("Початок діапазону: "))
num2 = int(input("Кінець діапазону: "))

while num1 <= num2:
    print(num1, end="\f")
    if num1 % 15==0:
        print("| Fizz Buzz")
    elif num1 % 3==0:
        print("| Fizz")
    elif num1 % 5==0:
        print("| Buzz")

    else:
        print("  -")
    num1 += 1