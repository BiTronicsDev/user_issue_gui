import pandas as pd


class Consts:
    priority = {'3-Низкий': 0, '2-Средний': 1, '1-Высокий': 2, '0-Критический': 3}
    status = {'Отменен': 0, 'Закрыт': 1}
    obr = {'Запрос': 0, 'Инцидент': 1}
    critical = {'4-Нет': 0, "3-Базовая": 2, "2-Повышенная": 3, "1-Особая": 1}
    influence = {"4-Нет влияния": 0, "3-Малое": 1, "2-Значительное": 2, "1-Всеохватывающее": 3}
    cols = ['id', 'Тип обращения на момент подачи', 'Тип переклассификации', 'Тип обращения итоговый']
    cols2 = ['Тип обращения на момент подачи', 'Тип переклассификации', 'Тип обращения итоговый']
    map_type = {0: 'Запрос', 1: "Инцидент"}

    @staticmethod
    def get_system(df: pd.DataFrame) -> dict:
        system_l = df['Система'].unique()
        system_d = {}
        for i in range(len(system_l)):
            system_d[system_l[i]] = i
        return system_d

    @staticmethod
    def get_place(df: pd.DataFrame) -> dict:
        place_l = df['Место'].unique()
        place_d = {}
        for i in range(len(place_l)):
            place_d[place_l[i]] = i
        return place_d

    @staticmethod
    def get_func(df: pd.DataFrame) -> dict:
        func_l = df['Функциональная группа'].unique()
        func_d = {}
        for i in range(len(func_l)):
            func_d[func_l[i]] = i
        return func_d
