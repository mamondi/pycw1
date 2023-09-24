num1 = float(input("Початок діапазону: "))
num2 = float(input("Кінець діапазону: "))

while num1 < num2:
    if num1 % 7==0:
        print(num1)
    num1 += 1
print(num1)