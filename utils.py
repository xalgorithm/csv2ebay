def getheaders(data):
    data = load_template()
    df3 = pd.DataFrame(data)
    return df3
def load_template():
    f = open('csvs/headers.json')
    locdata = json.load(f)
    return locdata