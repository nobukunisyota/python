#!/usr/bin/env python 

import os
import pandas as pd
import click

PRODUCT_COLUMN_NAME = '利用店名・商品名'
MONEY_COLUMN_NAME = '利用金額'

# CSVファイル名一覧取得
def load_files(dirname):
    return os.listdir(os.path.join(os.getcwd(), dirname))

# 出力ファイル名を決定する
def decide_output_filename(filename):
    date = int(filename[5:11])
    return "ExpensesReport_{}.csv".format(date)

# CSV読み込み
def load_csv(filename):
    df = pd.read_csv(filename, encoding='utf-8')
    return df.loc[:, [PRODUCT_COLUMN_NAME, MONEY_COLUMN_NAME]]

# データフレームを集計・加工する
def adjust_dataframe(df):
    df = df.dropna()
    df = df.groupby(PRODUCT_COLUMN_NAME)[MONEY_COLUMN_NAME].sum().astype('int')
    df.sort_values(ascending=False)
    df.loc['Total'] = df.sum()
    return df

# CSV出力する
def df_to_csv(df, output):
    df.to_csv(output, encoding='utf-8')

@click.command()
@click.option('-d', 'dirname')
def cmd(dirname):
    file_list = load_files(dirname)
    for file in file_list:
        output = decide_output_filename(file)
        filename = os.path.join(dirname, file)
        df = load_csv(filename)
        adjusted_df = adjust_dataframe(df)
        df_to_csv(adjusted_df, output)

def main():
    cmd()

if __name__ == '__main__':
    main()