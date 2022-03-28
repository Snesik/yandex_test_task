import time


def in_dict(path):
    """
    Создаем словарь, плюсы:
    Можно сразу структурировать(слаживать такие же вхождения)
    Благодаря этому экономим место в ОЗУ
    Получаем готовый данны, которые требуется только записать в файл

    """
    all_data = dict()
    with open(path) as f:
        for line in f:
            adress = line.split(',')
            adress = adress[7] + adress[9] + adress[10] + adress[11] + adress[12] + adress[13]
            adress = adress.replace('"', ' ')
            if adress in all_data:
                all_data[adress] += 1
            else:
                all_data[adress] = 1
            """
            Уменьшаем потребление процессорного времени
            Замедляется работа, но потребление падает на несколько порядков
            Возможно добавлять или убавлять
            """
            #time.sleep(0.0001)
        return all_data


def write(all_data):
    with open('task_01\\data.txt', 'w') as f:
        for line in all_data:
            if all_data[line] > 1:
                f.write(f'{line}\n')


if __name__ == "__main__":
    all_line = in_dict('task_01\\pp-complete.csv')
    write(all_line)
