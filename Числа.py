
a = True
magic_number = 7
print("угадайте загаданное число")
while a:
    number = int(input("Введите число:"))
    print("Значение number: ", number)
    if magic_number == number:
        print("Поздравляем! Вы угадали загаданное число!")
        a = False

print("Программа завершена")