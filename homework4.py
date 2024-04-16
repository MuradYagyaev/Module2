# Модуль 2 урок №4. "Цикл for. Элементы списка. Полезные функции в цикле."
car_models = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
# for i in car_models:
#     print(f'Я езжу на автомобиле марки {i}')
#     cars_count += 10
for i in range(car_models.__len__()):
    print(f'Я езжу на автомобиле марки {car_models[i]}')
    cars_count += 10
    print(f'cars_count = {cars_count}')
