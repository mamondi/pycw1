num1 = int(input("Введіть довжину лінії -> ")) #Користувач вводить із клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані горизонтальну лінію із введеного символу, вказаної довжини.
num2 = input("Введіть символ -> ")

for i in range(num1):
    print(num2, end="")

