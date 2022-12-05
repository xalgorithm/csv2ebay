import json.decoder

import pandas as pd


def loadTemplate():
    f = open('headers.json')
    data = json.load(f)
    return data


def combineImprint():
    df1 = pd.read_csv('clz-update.csv')
    df2 = pd.DataFrame
    df2['Combined'] = df1['Imprint'].astype(str) + "-" + df1["Series"].astype(str)
    df2['Description'] = df1["Full Title"].astype(str) + " " + df1['Variant'].astype(str) + " " + df1[
        'Variant Description'].astype(str)
    return df2


def combineAll(df2, data):
    # df4 = pd.DataFrame(data=)
    pass


if __name__ == '__main__':
    df2 = combineImprint()
    data = loadTemplate()
    combineAll(df2, data)

    print(df2)
