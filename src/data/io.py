import json
import pandas as pd
import os
from src.const.data_dir import CSV
import datetime


def get_file_name(symbol, interval):
    return "{}_{}".format(symbol, interval)


class Save:
    @staticmethod
    def save_file(data, path, name):
        if isinstance(data, pd.DataFrame):
            data.to_csv(os.path.join(path, name + '.csv'))
        elif isinstance(data, list):
            with open(os.path.join(path, name + '.json'), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


class Load:
    @staticmethod
    def load_file(file_path: str):
        file_name, ext = os.path.splitext(file_path)
        if ext == '.csv':
            df = pd.read_csv(file_path, index_col=0)
            df['Open time'], df['Close time'] = pd.to_datetime(
                df['Open time']), pd.to_datetime(df['Close time'])
            df.set_index('Open time', inplace=True)
            return df

    @staticmethod
    def load_file_from_tuple(symbol, interval):
        file_name = get_file_name(symbol, interval)
        file_path = os.path.join(CSV, file_name + '.csv')
        df = pd.read_csv(file_path, index_col=0)
        df['Open time'], df['Close time'] = pd.to_datetime(
            df['Open time']), pd.to_datetime(df['Close time'])
        df.set_index('Open time', inplace=True)
        return df


if __name__ == '__main__':
    df = Load.load_file(
        'F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_1d.csv')
    print(df.head())
