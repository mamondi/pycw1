num1 = int(input("Перше значення діапазону -> "))
num2 = int(input("Друге значення діапазону -> "))

summ = 0
amount = 0


while num1 <= num2:
    summ += num1
    amount += 1
    num1 += 1

result = summ/amount

print(f"Сумма {summ}")
print(f"Середньоарифметичне {result}")