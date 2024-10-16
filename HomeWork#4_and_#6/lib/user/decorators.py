import time #импортируем модуль для декоратора домашки
class Decs:

    @staticmethod  # используем staticmethod, т.к. внутри нашего декоратора, мы не обращаемся к атрибутам и методам класса
    def log_create_task(fn):  # Объявляем название для декоратора
        # fn является create_task (см. файл client, 11-12 строки)
        def wrapper(*args, **kwargs):
            # Метод wrapper принимает на вход позиционные(*args) и именованные аргументы(**kwargs)
            # для последующего взаимодействия с ними и передачи их в нашу функцию
            print('Вызван метод для добавления задачи: ', {**kwargs}.get('name'))
            fn(*args, **kwargs)
            # В данном случае, мы кладём аргументы переданные в вызове метода create_task в вызов переданной функции
            # Ниже как раз и представлены переданные аргументы, они в таком же виде, передаются в fn
            # name='test',
            # priority='medium',
            # deadline=datetime.datetime(
            #         year=2024,
            #         month=10,
            #         day=1,
            #         hour=19,
            #         minute=0,
            # )
        return wrapper  # Тут как раз мы и возвращаем функцию-обёртку

    #Декоратор для домашки #5
    def test_time(func):
        def jopper(*args, **kwargs):
            st = time.time()
            result = func(*args, **kwargs)
            et = time.time()
            dt = et - st
            print(f"Время работы функции: {dt} сек")
            return result

        return jopper
