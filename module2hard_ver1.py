# Дополнительное практическое задание по модулю: "Базовые структуры данных."

# Поиск максимального значения первого числа
def max_first(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(n // 2 + 1)

# Поиск пароля для числа
def find_password(n):
    password = ''
    for i in range(1, max_first(n)):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password


# Вывод всех найденных значений
for i in range(3, 21):
    print(f'{i} - {find_password(i)}')
