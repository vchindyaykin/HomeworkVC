# 1. На ввод подаётся произвольный символ. Необходимо вывести его 5 раз,
# но начиная с новой строки,
# к предыдущей строке прибавляется ещё 1 такой же символ.
# Пример:

# *
# **
# ***
# ****
# *****

char = input('Введите символ: ')
for i in range(1, 6):
    print(char * i)


# 2. На ввод подаётся число от 1 до 12. Необходимо вывести название месяца по его номеру.
# >> 3
# Март

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
}
month_number = input('Введите номер месяца: ')