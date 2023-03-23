import pandas as pd

def sampling():

    df = pd.read_json("data_pp.json", orient="columns")
    df_sample = df.sample(frac=0.25, ignore_index=True)
    df_sample.reset_index(drop=True, inplace=True)
    df_sample.to_json("data_pp_sample.json")


sampling()
print("data sampled")
