import pandas as pd
from catboost import CatBoostClassifier
from NeuralData.consts import Consts
from sklearn.preprocessing import LabelEncoder


class ShishkaClassifier:
    def __init__(self, dataframe: pd.DataFrame):
        self.model: CatBoostClassifier = CatBoostClassifier()
        self.model.load_model("NeuralData/files/issue_model")
        self.df = dataframe.copy()
        self.start_cols = self.df.columns

    @staticmethod
    def get_requalification_type(ticketStartType, ticketFinalType):
        if ticketStartType == ticketFinalType:
            return 0
        return 2 if ticketStartType == "Инцидент" else 1

    @staticmethod
    def set_requal(df: pd.DataFrame, ans: list) -> pd.DataFrame:
        df['Тип обращения итоговый'] = ans
        df['Тип обращения итоговый'] = df['Тип обращения итоговый'].map(Consts.map_type)
        df['Тип переклассификации'] = df.apply(
            lambda row: ShishkaClassifier.get_requalification_type(row['Тип обращения на момент подачи'], row['Тип обращения итоговый']),
            axis=1)
        return df

    def _set_date(self) -> None:
        self.df['Дата обращения'] = pd.to_datetime(self.df['Дата обращения'])
        self.df['Дата закрытия обращения'] = pd.to_datetime(self.df['Дата закрытия обращения'])
        self.df['range_time'] = self.df['Дата закрытия обращения'] - self.df['Дата обращения']
        self.df['Крайний срок'] = pd.to_datetime(self.df['Крайний срок'])
        self.df['time_to_solve'] = (self.df['Крайний срок'] - self.df['Дата обращения'])
        self.df['range_time'] = self.df['range_time'].dt.total_seconds() / 3600
        self.df['time_to_solve'] = self.df['time_to_solve'].dt.total_seconds() / 3600
        self.df['range_time'] = self.df['range_time'].fillna(-1)
        self.df['time_to_solve'] = self.df['time_to_solve'].fillna(-1)

    def _encode_labels(self) -> None:
        label_encoder = LabelEncoder()
        label_encoder2 = LabelEncoder()
        labels = label_encoder.fit_transform(self.df['Содержание'])
        labels2 = label_encoder2.fit_transform(self.df[self.df.columns[9]])
        self.df['numeric_sod'] = labels
        self.df['numeric_ans'] = labels2

    def reformat_df(self) -> None:
        self.df['Приоритет'] = self.df['Приоритет'].map(Consts.priority)
        self.df['Статус'] = self.df['Статус'].map(Consts.status)
        self.df['Тип обращения на момент подачи'] = self.df['Тип обращения на момент подачи'].map(Consts.obr)
        self.df['Тип обращения итоговый'] = self.df['Тип обращения итоговый'].map(Consts.obr)
        self.df['Критичность'] = self.df['Критичность'].map(Consts.critical)
        self.df['Влияние'] = self.df['Влияние'].map(Consts.influence)
        self.df['koef'] = self.df['Критичность'] * self.df['Влияние']
        self.df['Система'] = self.df['Система'].map(Consts.get_system(self.df))
        self.df['Место'] = self.df['Место'].map(Consts.get_place(self.df))
        self.df['Функциональная группа'] = self.df['Функциональная группа'].map(Consts.get_func(self.df))
        self._encode_labels()
        self._set_date()

    def predict(self) -> list:

        test = self.df[["numeric_sod", "numeric_ans", 'Тип обращения на момент подачи', 'Приоритет',
                        'Влияние', 'range_time', 'time_to_solve', 'Система', 'Место',
                        'Функциональная группа', 'koef']]
        test.to_csv("files/testing.csv", index=False)
        ans: list = self.model.predict(test)
        return ans
