import random


def merge_yousell(df2, df3):
    num_rows = df2.shape[0]
    for i in range(num_rows):
        df3.loc[i, 'Temp'] = ""
        df3.loc[i, 'Type'] = "simple"
        df3.loc[i, 'SKU'] = "br_kn" + "00" + str(i)
        df3.loc[i, 'Name'] = df2.loc[i, 'Combined']
        df3.loc[i, 'Published'] = "0"
        df3.loc[i, 'Is featured?'] = ""
        df3.loc[i, 'Visibility in catalog'] = "visible"
        df3.loc[i, 'Short description'] = df2.loc[i, 'Title']
        df3.loc[i, 'Description'] =  df2.loc[i, 'Description']
        df3.loc[i, 'Date sale price starts'] = ""
        df3.loc[i, 'Date sale price ends'] = ""
        df3.loc[i, 'Tax status'] = "taxable"
        df3.loc[i, 'Tax class'] = ""
        df3.loc[i, 'In stock?'] = 1
        df3.loc[i, 'Stock'] = 1
        df3.loc[i, 'Low stock amount'] = ""
        df3.loc[i, 'Backorders allowed?'] = ""
        df3.loc[i, 'Sold individually?'] = ""
        df3.loc[i, 'Weight (kg)'] = ""
        df3.loc[i, 'Length (cm)'] = ""
        df3.loc[i, 'Width (cm)'] = ""
        df3.loc[i, 'Height (cm)'] = ""
        df3.loc[i, 'Allow customer reviews?'] = ""
        df3.loc[i, 'Purchase note'] = ""
        df3.loc[i, 'Sale price'] = ""
        df3.loc[i, 'Regular price'] = str(float(df2.loc[i, 'Value']) * (90 / 100))
        df3.loc[i, 'Categories'] = "RAW, MODERN AGE"
        df3.loc[i, 'Tags'] = ""
        df3.loc[i, 'Shipping class'] = ""
        df3.loc[i, 'Images'] = ""
        df3.loc[i, 'Parent'] = ""
        df3.loc[i, 'Upsells'] = ""
        df3.loc[i, 'Cross-sells'] = ""
        df3.loc[i, 'Position'] = ""
        df3.loc[i, 'Meta: scd_other_options'] = "s:0:""";""
        df3.loc[i, 'Attribute 1 name'] = "Publisher"
        df3.loc[i, 'Attribute 1 value(s)'] = df2.loc[i, 'Publisher']
        df3.loc[i, 'Attribute 1 visible'] = 1
        df3.loc[i, 'Attribute 1 global'] = 1
        df3.loc[i, 'Attribute 2 name'] = "Estimated Grade"
        df3.loc[i, 'Attribute 2 value(s)'] = "NM-/NM+"
        df3.loc[i, 'Attribute 2 visible'] = 1
        df3.loc[i, 'Attribute 2 global'] = 1
        df3.loc[i, 'Attribute 3 name'] = ""
        df3.loc[i, 'Attribute 3 value(s)'] = ""
        df3.loc[i, 'Attribute 3 visible'] = ""
        df3.loc[i, 'Attribute 3 global'] = ""
        df3.loc[i, 'Attribute 4 name'] = ""
        df3.loc[i, 'Attribute 4 value(s)'] = ""
        df3.loc[i, 'Attribute 4 visible'] = ""
        df3.loc[i, 'Attribute 4 global'] = ""
    return df3
