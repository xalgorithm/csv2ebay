def merge_whatnot(df2, df3):
    num_rows = df2.shape[0]
    for i in range(num_rows):
        df3.loc[i, 'Category'] = "Comics & Manga"
        df3.loc[i, 'Sub Category'] = "Modern Age Comics"
        df3.loc[i, 'Title'] = df2.loc[i, 'Combined']
        df3.loc[i, 'Description'] = df2.loc[i, 'Description']
        df3.loc[i, 'Quantity'] = "1"
        df3.loc[i, 'Type'] = "Auction"
        df3.loc[i, 'Price'] = "5"
        df3.loc[i, 'Shipping Profile'] = "4-7 oz (Comic, Fat Pack, T-Shirt)"
    return df3