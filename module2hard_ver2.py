# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Вариант получился не очень из-за результата None, которое возвращает функция find_pair,
# если не ставить - return '', а ставить дополнительное условие в find_password усложняет функцию

# Поиск максимального значения первого числа
def max_first(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(n // 2 + 1)

# Поиск пары чисел, удовлетворяющих условию
def find_pair(number, first_num, second_num):
    if number % (first_num + second_num) == 0:
        return str(first_num) + str(second_num)
    else:
        return ''

# Поиск пароля для числа
def find_password(number):
    password = ''
    for i in range(1, max_first(number)):
        for j in range(i + 1, number):
            password += find_pair(number, i, j)
    return password


# Вывод всех найденных значений
for i in range(3, 21):
    print(f'{i} - {find_password(i)}')
