# 1. Имеется поле 3x3 необходимо реализовать возможность отрисовки на нём квадрата. Если квадрат занимает всё поле,
# то центр необходимо оставить пустым
field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
middle_x = int(len(field)/2)
middle_y = int(len(field[0])/2)

for x in range(3):
    for y in range(3):
        if x == middle_x and y == middle_y:
            field[x][y] = ' '
        else:
            field[x][y] = '*'

for line in field:
    print(line)

# 2. Написать свой декоратор для любой функции в client
import time

def test_time(func):    
    def jopper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы функции: {dt} сек")
        return result

    return jopper
# Данный декоратор также дублируется в HomeWork#4.lib.client.client.py. Также добавил задержку по времени в функцию create_task для наглядности отработки декоратора

# 3. Необходимо написать функцию, которая разбивает предложения на слова и возвращает список слов.
# Далее необходимо написать под неё декоратор, который форматирует список слов в верхний регистр и возвращает их
print("Пока только делаю задачку, в процессе")
