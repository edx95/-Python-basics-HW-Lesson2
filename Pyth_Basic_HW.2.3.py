'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

customer_text = int(input('Введите месяц в виде целого числа от 1 до 12 >>>'))


if 0 >= customer_text or customer_text >= 13:
    print('А можно поточнее :(')
else:
    year_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    leto = [6, 7, 8]
    osen = [9, 10, 11]
    zima = [12, 1, 2]
    vesna = [3, 4, 5]
    month = year_dict.get(customer_text)
    if customer_text in leto:
        print(f'Вы выбрали {month}  это летний месяц!')
    elif customer_text in osen:
        print(f'Вы выбрали {month} это осенний месяц!')
    elif customer_text in zima:
        print(f'Вы выбрали {month} это зимний месяц!')
    else:
        print(f'Вы выбрали {month} это осенний месяц!')