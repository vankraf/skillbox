# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(months[month-1] if 1 <= month <=12 else "номер месяца некорректен - сообщить об этом")
