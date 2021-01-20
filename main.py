"""
Главный модуль программы.
Точка старта.
"""
import loader
import click

BUBBLE ='bubble'
INSERT = 'insert'
SELECTION = 'SELECTION'

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
               help = 'Алгоритм сортировки.')
def sorter(filename, algorithm):
    '''Простая утилита для сортировки чисел.
    '''
    print(filename, algorithm)
    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)

    allowed_algotithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in [BUBBLE, INSERT, SELECTION]:
        print('Неправельно введено имя алгоритма.')
        exit(1)
if __name__ == '__main__':
    sorter()
