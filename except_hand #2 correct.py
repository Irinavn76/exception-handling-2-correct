try: # Запрашиваем ввод двух чисел
    number1 = int(input("Введите число: "))
    number2 = int(input("Введите число: "))
    print("Введенное число:", number1)
    print("Введенное число:", number2)
    result = number1 / number2
except ValueError: # Исключение ошибки введения не числового значения
    print("Ошибка: введено не число")
except ZeroDivisionError: # Исключение ошибки введения ноля
    print("Ошибка: деление на ноль")
else: # Блок выполняется при отсутствии ошибок
    print(f"Результат: {result}")
finally: # Завершение работы программы
    print("Завершение программы")
