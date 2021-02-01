"""
Главный модуль программы.
Точка старта.
"""
import loader
import sorting
import click

BUBBLE = 'b'
INSERT = 'i'
SELECTION = 'S'

'''
source, filename = parse_cmd()
if source == KEYBOARD:
    unsorted_data = load_from_input()
else:
    unsorted_data = load_from_file(filename)
'''


@click.command()
@click.option('--filename', default=None,
                help='Имя файла с сортированными данными.')
@click.option('--algorithm', default=BUBBLE,
                help='Алгоритм сортировки.')
def sorter(filename, algorithm):
    ''' Простая утилита для сортировки чисел
    '''
    allowed_algorithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in allowed_algorithms:
        print('Неправельно введено имя алгоритма.')
        print('Правельные варианты: ', allowed_algorithms)
        exit(1)

    print(filename, algorithm)
    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)

    if algorithm == BUBBLE:
        result = sorting.bubble_sort(unsorted_data)
    elif algorithm == INSERT:
        result = sorting.insert_sort(unsorted_data)
    elif algorithm == SELECTION:
        result = sorting.selection_sort(unsorted_data)

    print('Несортированный массив: ', *unsorted_data)
    print('Сортированный массив: ', *result)


if __name__ == '__main__':
    sorter()
