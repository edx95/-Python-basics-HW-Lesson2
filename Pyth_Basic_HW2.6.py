'''
# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

'''

i = 'д'
print('Добавление товаров')
y = 1
list_tuple = list()

while i == 'д':
    name = input('Введите название товара >> ')
    price = int(input('Введите цену >> '))
    count = int(input('Количество >> '))
    unit = input('Единица изменения >> ')
    product = {"Название": name, "Цена": price, "Количество": count, "Единица изменения": unit }
    my_tuple = (y, product)
    list_tuple.append(my_tuple)
    print(list_tuple)
    i = input('Введете еще один товар? (д/н) >> ').lower()
    y += 1

print('Отлично! Мы собрали данные по товарам!')

#Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#Пример:
#{
#    “название”: [“компьютер”, “принтер”, “сканер”],
#    “цена”: [20000, 6000, 2000],
#    “количество”: [5, 2, 7],
#    “ед”: [“шт.”]
#}

analitica = dict()

for x in list_tuple:
    for name, value in x[1].items():
        if name not in analitica:
            analitica.update({name: [value]})
        else:
            if value not in analitica.get(name):
                analitica.get(name).append(value)

print(f'собрана аналитика: {analitica}')