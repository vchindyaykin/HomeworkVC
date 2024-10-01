# 1. Создайте класс с базовыми-абстрактными функциями. Класс должен иметь аргументы. Настройте поведение экземпляра
# класса с помощью дандер методов

class Character:
    def __init__(self, c_name, c_type, c_class):
        self.c_name = c_name
        self.c_type = c_type
        self.c_class = c_class

    def describe(self):
        print(f"Имя персонажа: {self.c_name}, Расса персонажа: {self.c_type}, Класс персонажа: {self.c_class}")

c_name = input("Введите имя персонажа: ")
c_type = input("Введите рассу персонажа: ")
c_class = input("Введите класс персонажа: ")

hero = Character(c_name, c_type, c_class)

hero.describe()

# 2. Дано целое число x, вернуть x с обратными цифрами
# Пример 1:
#  Вход: x = 123
#  Выход: 321
#
# Пример 2:
# Вход: x = -123
# Выход: -321
#
# Пример 3:
# Вход: x = 120
# Выход: 21

def reverse_integer():
    x = int(input("Введите целое число: "))

    #Проверяем, отрицательное ли число
    if x < 0:
        negative = True
        x = -x #Делаем положительным
    else:
        negative = False

    #Превращаем число в строку
    x_str = str(x)

    #Убираем нудли в конце
    if x_str.endswith('0'):
        while x_str.endswith('0'):
            x_str = x_str[:-1]

    #Переворачиваем строку с помощью среза
    reversed_str = x_str[::-1]

    #Превращаем строку обратно в число
    reversed_num = int(reversed_str)

    #Возвращаем отрицательный знак
    # Если исходное число было отрицательным
    if negative:
        return -reversed_num
    # Если исходное число было положительным
    else:
        return reversed_num

result = reverse_integer()
print("Ваше перевернутое число: ", result)



# 3. Напишите функцию, принимающую в качестве аргументов 2 списка. Функция должна соединить и отсортировать их.
#
# Пример 1:
# Вход: список1 = [1,2,4], список2 = [1,3,4]
#  Выход: [1,1,2,3,4,4]
#
# Пример 2:
# Ввод: список1 = [], список2 = []
#  Вывод: []
#
# Пример 3:
# Ввод: список1 = [], список2 = [0]
#  Вывод: [0]

#Функция ввода значений в списки
def input_list(prompt):
    user_input = input(prompt)
    # Обработка введеных значений в список чисел
    return [int(x) for x in user_input.split(',') if x.strip().isdigit()]

#Функция объединения списка
def merge_and_sort_list(list1, list2):
    #Объединяем оба списка
    merged_list = list1 + list2
    # Сортируем объединённый список
    sorted_list = sorted(merged_list)
    return sorted_list

list1 = input_list("Введите значения через запятую для 1 списка: ")
list2 = input_list("Введите значения через запятую для 2 списка: ")

result = merge_and_sort_list(list1, list2)
print(result)

