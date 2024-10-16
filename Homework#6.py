#1 решение задачи
def achivka():
    with open('achivments1.txt', 'w', encoding='utf8') as file:
        for achievement in app.get_achievements():
            comp_str = f'{asdict(achievement)}\n'
            file.write(comp_str)
    with open('achivments1.txt', "r", encoding='utf8') as file:
        achievement = file.read()
        print("Ачивки: ", achievement)

def taska():
    with open('tasks1.txt','w', encoding='utf8') as file:
        # Уточнить по этой реализации. По аналогии с ачивками не вышло реализовать,
        # из-за ошибки "TypeError: asdict() should be called on dataclass instances"
        # я вызывал функцию asdict() на объекте, который не является экземпляром таски -
        # честно говоря я ни черта не понял, что сейчас написал)
        # но задачу можно было просто записать в файлик методом file.write(f'{task}') и все)
        for task in app.get_tasks():
            if dataclasses.is_dataclass(task):
                comp_str = f'{dataclasses.asdict(task)}'
                file.write(comp_str)
            else:
                file.write(f'{task}')
    with open('tasks1.txt', 'r', encoding='utf8') as file:
        tasks = file.read()
        print("Задачи: ", tasks)


#2 решение задачи
def kostil():
    def write_achivment_and_task ():
        with open('achivments2.txt', 'w', encoding='utf8') as file:
            with redirect_stdout(file):
                print(app.get_achievements())
        with open ('tasks.txt2', 'w', encoding='utf8') as file:
            with redirect_stdout(file):
                print(app.get_tasks())

    def read_achivment_and_task ():
        with open ('achivments2.txt', 'r', encoding='utf8') as file:
            achivments = file.read()
            print("Ачивки: ", achivments)
        with open ('tasks.txt2', 'r', encoding='utf8') as file:
            tasks = file.read()
            print("Задачи: ", tasks)
    write_achivment_and_task()
    read_achivment_and_task()

# print(app.get_achievements())
# print(app.get_tasks())

achivka()
taska()
kostil()
