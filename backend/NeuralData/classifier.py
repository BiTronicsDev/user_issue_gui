import os

import pandas as pd
from catboost import CatBoostClassifier
from NeuralData.consts import Consts
from sklearn.preprocessing import LabelEncoder


class ShishkaClassifier:
    def __init__(self, dataframe: pd.DataFrame):
        self.model: CatBoostClassifier = CatBoostClassifier()
        self.path = os.getcwd()
        self.model.load_model("NeuralData/files/issue_model")
        self.df = dataframe.copy()
        self.start_cols = self.df.columns

    @staticmethod
    def get_requalification_type(ticketStartType, ticketFinalType) -> int:
        """
        The get_requalification_type function takes two arguments:
            ticketStartType - the type of ticket at the start of its lifecycle (e.g. Инцидент)
            ticketFinalType - the type of ticket at the end of its lifecycle (Заявка на услугу)

        :param ticketStartType: Determine the type of ticket that was created
        :param ticketFinalType: Determine the type of requalification
        :return: The type of the requalification
        :doc-author: zayycev22
        """
        if ticketStartType == ticketFinalType:
            return 0
        return 2 if ticketStartType == "Инцидент" else 1

    @staticmethod
    def set_requal(df: pd.DataFrame, ans: list) -> pd.DataFrame:
        """
          The set_requal function takes a dataframe and a list of answers as input.
          It then sets the 'Тип обращения итоговый' column to the list of answers,
          maps it to its corresponding value in Consts.map_type, and then creates a new column called 'Тип переклассификации'.
          The values in this new column are determined by applying ShishkaClassifier's get_requalification_type

          :param df: pd.DataFrame: Pass the dataframe to the function
          :param ans: list: Set the 'тип обращения итоговый' column
          :return: A dataframe with the requalification type column
          :doc-author: zayycev22
        """
        df['Тип обращения итоговый'] = ans
        df['Тип обращения итоговый'] = df['Тип обращения итоговый'].map(Consts.map_type)
        df['Тип переклассификации'] = df.apply(
            lambda row: ShishkaClassifier.get_requalification_type(row['Тип обращения на момент подачи'], row['Тип обращения итоговый']),
            axis=1)
        return df

    def _set_date(self) -> None:
        """
          The _set_date function sets the date to datetime format, then creates new columns
          range_time and time_to_solve and calculate them
          :return: None
          :doc-author: zayycev22
        """
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
        """
          The _encode_labels set text of columns Содержание and Решение to numeric and write it to columns
          numeric_sod and numeric_ans
          :return: None
          :doc-author: zayycev22
        """
        label_encoder = LabelEncoder()
        label_encoder2 = LabelEncoder()
        labels = label_encoder.fit_transform(self.df['Содержание'])
        labels2 = label_encoder2.fit_transform(self.df[self.df.columns[9]])
        self.df['numeric_sod'] = labels
        self.df['numeric_ans'] = labels2

    def reformat_df(self) -> None:
        """
          The reformat_df function reformat data in dataframe for catboostmodel
          :return: None
          :doc-author: zayycev22
        """
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
        """
          The predict function use pretrained catboost model to predict if issue will be requalified
          :return: list of predicted answers
          :doc-author: zayycev22
        """
        test = self.df[["numeric_sod", "numeric_ans", 'Тип обращения на момент подачи', 'Приоритет',
                        'Влияние', 'range_time', 'time_to_solve', 'Система', 'Место',
                        'Функциональная группа', 'koef']]
        ans: list = self.model.predict(test)
        return ans
