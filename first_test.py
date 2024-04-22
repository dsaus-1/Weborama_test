import csv, os


class ParserFile:


    def __init__(self, filename):
        self.filename = filename
        self.counter_dict = None


    def file_reader(self):
        '''
        Обрабатывает CSV файл с id во втором столбце. 
        Возвращает словарь в котором ключем является id,
        а значением кол-во повторений данного id 
        '''

        try:
            with open(self.filename, 'r+') as file:
                file_r = csv.reader(file)
                header = next(file_r)

                self.counter_dict = dict()
                for line in file_r:
                    if line[1] in self.counter_dict:
                        self.counter_dict[line[1]] += 1
                    else:
                        self.counter_dict[line[1]] = 1

                return self.counter_dict

        except FileNotFoundError as e:
            raise e


    def repetition_rate(self):
        '''
        Принимает словарь с ключем id и кол-вом повторений в значении.
        Возвращает словарь с частотой повторений уникальных id в ключе и 
        количеством в значении
        '''
        if self.counter_dict == None:
            self.file_reader()

        rate_dict = dict()
        for value in self.counter_dict.values():
            if value in rate_dict:
                rate_dict[value] += 1
            else:
                rate_dict[value] = 1
        return rate_dict
        

    def recurring_id(self, count=3):
        '''
        Принимает обязательный аргумент - словарь с ключем id и кол-вом повторений в значении,
        необязательный аргумент - число.
        Возвращает список id повторяющийся "count" раз, по умолчанию равен 3.
        '''
        if self.counter_dict == None:
            self.file_reader()

        return [id_ for id_, value in self.counter_dict.items() if value == count]
