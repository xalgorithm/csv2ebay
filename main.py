import json.decoder
from builtins import print
import pandas as pd
import ebay as e
import whatnot as w
import yousell as y
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--service', help='Sellers service')
args = parser.parse_args()
service = args.service

df1 = pd.read_csv('csvs/clz.csv')


def pull_new_data(df1):
    df2 = pd.DataFrame(data=df1)
    return df2


def convert_to_json():
    try:
        if service == 'ebay':
            df3 = pd.read_csv('csvs/ebay.csv')
            return df3
        elif service == 'whatnot':
            df3 = pd.read_csv('csvs/whatnot.csv')
            return df3
        elif service == 'yousell':
            df3 = pd.read_csv('csvs/yousell.csv')
            return df3
        else:
            print('No service selected')
    except json.decoder.JSONDecodeError:
        print('Error converting to json')


def route_service():
    if service == 'ebay':
        e.merge_ebay(df2, df3)
        return df3
    elif service == 'whatnot':
        w.merge_whatnot(df2, df3)
        return df3
    elif service == 'yousell':
        y.merge_yousell(df2, df3)
        return df3


def combine_fields(df2):
    df2['Combined'] = df1['Imprint'].astype(str) + ' ' + df1['Series'].astype(str) + ' ' + df1['Issue'].astype(str)
    df2['Combined'] = df2['Combined'].str.replace('nan', '')
    df2['Description'] = df1["Full Title"].astype(str) + " " + df1['Variant'].astype(str) + " " + df1[
        'Variant Description'].astype(str)
    df2['Description'] = df2['Description'].str.replace('nan', '')
    return df2


def to_csv():
    if service == 'ebay':
        df3.to_csv('output_ebay.csv', index=False)
    elif service == 'whatnot':
        df3.to_csv('output_whatnot.csv', index=False)
    elif service == 'yousell':
        df3.to_csv('output_yousell.csv', index=False)


if __name__ == '__main__':
    df2 = pull_new_data(df1)
    df2 = combine_fields(df2)
    df3 = convert_to_json()
    df4 = route_service()
    to_csv()
