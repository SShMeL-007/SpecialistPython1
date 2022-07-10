# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
def S(a, b):
    return a * b

is_repeat_needed = True
while is_repeat_needed:
    nxm = input("Введите размеры прямоугольника, следующим видом: 12x5 - ")
    nm = nxm.split("x")
    if len(nm) == 1:
        print("Не найден разделитель")
    elif len(nm) > 2:
        print("Чисел слишком много")
    else:
        try:
            print(int(S(int(nm[0]), int(nm[1])) / S(int(nm[1]), int(nm[1]))))
        except BaseException as ex:
            print(ex)
        else:
            is_repeat_needed = False
