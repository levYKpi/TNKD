from prettytable import PrettyTable


def create_table():
    th = ['Module', 'Tn', 'Tmax', 'Pr1', 'Pr2','Pr3', 'Pr5', 'Pr6']
    td = ['Pr1', '20', '70', '-', '10', '20', '10', '10',
          'Pr2', '40', '100', '40', '-', '40', '10', '20',
          'Pr3', '50', '100', '50', '50', '-', '20', '20',
          'Pr5', '70', '90', '50', '20', '50', '-', '20',
          'Pr6', '30', '50', '10', '30', '30', '30',  '-']

    columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

    table = PrettyTable(th)  # Определяем таблицу.

    # Cкопируем список td, на случай если он будет использоваться в коде дальше.
    td_data = td[:]
    # Входим в цикл который заполняет нашу таблицу.
    # Цикл будет выполняться до тех пор пока у нас не кончатся данные
    # для заполнения строк таблицы (список td_data).
    while td_data:
        # Используя срез добавляем первые пять элементов в строку.
        # (columns = 5).
        table.add_row(td_data[:columns])
        # Используя срез переопределяем td_data так, чтобы он
        # больше не содержал первых 5 элементов.
        td_data = td_data[columns:]

    print(table)  # Печатаем таблицу
    return table
