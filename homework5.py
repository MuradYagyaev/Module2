# Модуль 2 урок №5. "Функции в Python.Функция с параметром"
def print_params(paramater1='А тут ничего не передано функции'):
    print('Первый вывод параметра:', paramater1)
    print(f'Второй вывод параметра: {paramater1}')


print_params('Эту строку я передал функции!')
print_params('Еще раз передаю строку')
print_params()
