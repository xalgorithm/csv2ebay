import random
def merge_ebay(df2, df3):
    num_rows = df2.shape[0]
    for i in range(num_rows):
        df3.loc[i, 'sku'] = "br_kn" + str(random.randint(100000, 999999))
        df3.loc[i, 'title'] = df2.loc[i, 'Combined']
        df3.loc[i, 'upc'] = df2.loc[i, 'Barcode'].astype(str)
        df3.loc[i, 'category_id'] = "259104"
        df3.loc[i, 'item_description'] = df2.loc[i, 'Description']
        df3.loc[i, 'price_ebay'] = str(float(df2.loc[i, 'Value'])*(80/100))
        df3.loc[i, 'condition'] = "1000"
        df3.loc[i, 'condition_description'] = "NM 9+"
        df3.loc[i, 'shipping_cost'] = "6.00"
        df3.loc[i, 'ebay_shipfrom_zipcode'] = "93635"
        df3.loc[i, 'item_weight_oz'] = "6.00"
        df3.loc[i, 'item_dimensions_length'] = "12.75"
        df3.loc[i, 'item_dimensions_width'] = "7.75"
        df3.loc[i, 'item_dimensions_height'] = "0.75"
        df3.loc[i, 'image_url'] = "http://epyc.xalg.im/"
        df3.loc[i, 'auto_synced_qty'] = "1"
        df3.loc[i, 'activate_ebay'] = "1"
    return df3