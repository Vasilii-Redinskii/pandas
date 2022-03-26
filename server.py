# Импортируем библиотеку pandas
from pprint import pprint

import pandas


def get_password(object_list, login):
    """Функция находит значение ключа password из списка object_list

    :param object_list: список словарей со структурой login-password
    :param login: искомый login"""

    # Объявляем переменную для хранения найденного значения
    value = False
    for element in object_list:
        # Итерируемся по каждому элементу из переданного списка object_list.
        if element['login'] == login:
            # Если значение по ключу login равен искомому параметру, то передаем в value значение ключа password
            value = str(element['password'])
            break

    # Возвращаем найденное значение, если ничего не нашли - возвращаем False
    return value


# Читаем файл эксель и результат передаем в переменную excel_data
# Переменная excel_data имеет тип <class 'pandas.core.frame.DataFrame'>
excel_data = pandas.read_excel('data.xlsx', sheet_name='users', engine='openpyxl')

# Преобразуем переменную excel_data в словарь с помощью метода to_dict()
# Результат передаем в переменную excel_data_dict
excel_data_dict = excel_data.to_dict(orient='records')

# Просим юзера ввести имя пользователя и пароль
user_name = input('Введите имя пользователя: ')
user_password = input('Введите пароль: ')

# Получаем пароль для введенного юзера. Если такого юзера нет, то будет False
password = get_password(excel_data_dict, user_name)

if password and user_password == password:
    # Если имя пользователя и пароль совпадают - выдаем данные о продажах
    sales_data = pandas.read_excel('data.xlsx', sheet_name='sales', engine='openpyxl')
    print('Вам доступны данные о продажах:')
    print(sales_data)
else:
    # Если имя пользователя и пароль не совпадают - выдаем сообщение об ошибке
    print('Имя пользователя или пароль введены не верно')

