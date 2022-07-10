# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
nxm = input("Введите размеры прямоугольника, следующим видом: 12x5 - ")
nm = nxm.split("x")
try:
    print(int(nm[0])*int(nm[1])/int(nm[1])**2)
except BaseException as ex:
    print(ex)
