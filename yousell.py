import random


def merge_yousell(df2, df3):
    num_rows = df2.shape[0]
    for i in range(num_rows):
        # df3.loc[i, 'sku'] = "br_kn" + str(random.randint(100000, 999999))
        df3.loc[i, 'type'] = "simple"
        df3.loc[i, 'SKU'] = "br_kn" + "00" + str(i)
        df3.loc[i, 'Name'] = df2.loc[i, 'Combined']
        df3.loc[i, 'Published'] = "0"
        df3.loc[i, 'Is featured?'] = ""
        df3.loc[i, 'Visibility in catalog'] = "visible"
        df3.loc[i, 'Short description'] = df2.loc[i, 'Title']
        df3.loc[i, 'Description'] = df2.loc[i, 'Description']
        df3.loc[i, 'Tax status'] = ""
        df3.loc[i, 'Tax class'] = ""
        df3.loc[i, 'In Stock'] = "1"
        df3.loc[1, 'Stock'] = "1"
        df3.loc[1, 'Sale Price'] = str(float(df2.loc[i, 'Value']) * (75 / 100))
        df3.loc[i, 'Regular Price'] = str(float(df2.loc[i, 'Value']) * (85 / 100))
        df3.loc[i, 'Categories'] = ""
    return df3
