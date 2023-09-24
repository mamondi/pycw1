num1 = data1 = int(input("Початок діапазону: "))
num2 = data2 = int(input("Кінець діапазону: "))


print("Всі числа діапазону.")
while num1 < num2:
    print(num1)
    num1 += 1

num1 = data1
num2 = data2

print("Всі числа діапазону в спадному порядку.")
num3 = max(num1, num2)
num4 = min(num1, num2)

num1 = data1
num2 = data2

while num3 >= num4:
    print(num3)
    num3 -= 1

num1 = data1
num2 = data2

print("Всі числа діапазону, кратні 7.")
while num1 < num2:
    if num1 % 7==0:
        print(num1)
    num1 += 1

num1 = data1
num2 = data2

num5 = 0
while num1 < num2:
    if num1 % 5==0:
        num5 += 1
    num1 += 1
print("Кількість чисел, кратних 5: ", num5)
