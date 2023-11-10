from wc_data.get_latest_data import GetData

data = GetData()
df = data.get_data()
df.to_csv("wcc.csv", index=False)