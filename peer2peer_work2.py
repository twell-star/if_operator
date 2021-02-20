# Задание на оператор 'if'
# При решении задачи использовал исключительно оператор 'if'
# С циклами код был бы значительно короче

cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город (Москва, Париж или Лондон): ')

message = ''    # пустая строковая переменная для формирования отчета об отсутствии введенного города в списке

if city.lower() == cities[0].lower():           # проверка первого элемента в списке 'cities'
    city_out = cities[0]                        # определение переменной города вывода для True

    if city_out == tourists[0].get('city'):     # проверка города вывода в первом справочнике списка 'tourists'
        tourist_out = tourists[0]               # определение переменной справочника с городом вывода для True

        if (tourist_out.get('user')).get('name') == users[0].get('name'):   # проверка наличия данных вывода в первом справочнике списка 'users'
            user_out = users[0]                                             # определение переменной справочника с данными юзера вывода для True   

        elif (tourist_out.get('user')).get('name') == users[1].get('name'): # проверка наличия данных вывода во втором справочнике списка 'users'
            user_out = users[1]                                             # определение переменной справочника с данными юзера вывода для True

        else:
            user_out = users[2]                                             # определение переменной справочника с данными юзера вывода для предыдущих False
            
    elif city_out ==tourists[1].get('city'):    # проверка города вывода во втором справочнике списка 'tourists'
        tourist_out = tourists[1]               # определение переменной справочника с городом вывода для True
        
        if (tourist_out.get('user')).get('name') == users[0].get('name'):   # проверка наличия данных вывода в первом справочнике списка 'users'
            user_out = users[0]                                             # определение переменной справочника с данными юзера вывода для True
            
        elif (tourist_out.get('user')).get('name') == users[1].get('name'): # проверка наличия данных вывода во втором справочнике списка 'users'
            user_out = users[1]                                             # определение переменной справочника с данными юзера вывода для True
            
        else:
            user_out = users[2]                                             # определение переменной справочника с данными юзера вывода для предыдущих False
    
    else:
        tourist_out = tourists[2]               # определение переменной справочника с городом вывода для предыдущих False
    
        if (tourist_out.get('user')).get('name') == users[0].get('name'):   # проверка наличия данных вывода в первом справочнике списка 'users'
            user_out = users[0]                                             # определение переменной справочника с данными юзера вывода для True
    
        elif (tourist_out.get('user')).get('name') == users[1].get('name'): # проверка наличия данных вывода во втором справочнике списка 'users'
            user_out = users[1]                                             # определение переменной справочника с данными юзера вывода для True
    
        else:
            user_out = users[2]                                             # определение переменной справочника с данными юзера вывода для предыдущих False
      
elif city.lower() == cities[1].lower():         # проверка второго элемента в списке 'cities'
    city_out = cities[1]                        # далее структура логических условий аналогична предыдущей ветке

    if city_out == tourists[0].get('city'):
        tourist_out = tourists[0]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

    elif city_out ==tourists[1].get('city'):
        tourist_out = tourists[1]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

    else:
        tourist_out = tourists[2]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

elif city.lower() == cities[2].lower():         # проверка третьего элемента в списке 'cities'
    city_out = cities[2]                        # далее структура логических условий аналогична предыдущим веткам

    if city_out == tourists[0].get('city'):
        tourist_out = tourists[0]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

    elif city_out ==tourists[1].get('city'):
        tourist_out = tourists[1]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

    else:
        tourist_out = tourists[2]

        if (tourist_out.get('user')).get('name') == users[0].get('name'):
            user_out = users[0]

        elif (tourist_out.get('user')).get('name') == users[1].get('name'):
            user_out = users[1]

        else:
            user_out = users[2]

else:                                           
    message = 'Указанный город не обнаружен в списке'  # определение текста сообщения, если введенный город отсутствует в списке 'cities'
    
# вывод итогового отчета

if len(message) > 0:
    print(message)
else:
    print(f"Турист {user_out.get('name')} возраст {user_out.get('age')}. Посетил город {city}")
