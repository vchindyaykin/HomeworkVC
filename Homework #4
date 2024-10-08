# 1. Создайте класс Vehicle с базовыми-абстрактными функциями любого транспортного средства (Движение вперед, движение назад, запуск двигателя).
# Создайте 2 наследников класса Vehicle, опишитие их базовый функционал и аргументы.
# Создайте по объекту для каждого из класса-наследника. Воспользуйтесь функциями наследуемого класса и родительского

class Vehicle:
    def __init__(self, brand, color):
        self.color = color # Аргумент №1
        self.brand = brand # Аргумент №2

    # Родительские функции
    def drive_car(self):
        print(f"Машина {self.brand} {self.color} цвета 20 века едет")

    def engine_car(self):
        print (f"Машина {self.brand} {self.color} цвета 20 века завелась")

    def reverse_drive_car(self):
        print (f"Машина {self.brand} {self.color} цвета 20 века сдает задом")

    def drive_bike(self):
        print(f"Байк {self.brand} {self.color} цвета 20 века едет")

    def engine_bike(self):
        print (f"Байк {self.brand} {self.color} цвета 20 века завелась")


# Подкласс машина
class Car(Vehicle):
    def __init__(self, brand,color):
        super().__init__(brand, color)
    # Функция подкласса (чисто для примера)
    def this_car(self):
        print ("Описание действий машины:")

# Создаем объект подкласса
my_summer_car = Car("Reno Logan", "черного")
# Вывод функций
my_summer_car.this_car()
my_summer_car.engine_car()
my_summer_car.drive_car()
my_summer_car.reverse_drive_car()
# Добавляем разделение между выводами
print()


# Подкласс байк
class Bike(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
    # Функция подкласса (чисто для примера)
    def this_bike(self):
        print ("Описание действий байка:")

# Создаем объект подкласса
my_bike = Bike("Planeta 5", "красного")
# Вывод функций
my_bike.this_bike()
my_bike.engine_bike()
my_bike.drive_bike()
