"""
Загрузка данных.
"""
def load_from_input() -> list:
    '''Получение данных через input
    :return: список несортированных данных'''
    while True:
        try:
            raw_list = input('Введие числа разделенные пробелом: ')
            result = [int (i) for i in raw_list.split()]
        except ValueError:
            print('Вы ввели неправельное число')
        else:
            return result
def load_from_file(filename: str) -> list:
    '''Получение данных из файла
    :param filename: имя фйла
    :return: список несортированных данных'''
    ...
