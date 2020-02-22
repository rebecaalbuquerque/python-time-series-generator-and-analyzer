import pandas as pd
import subprocess


def generate_ts():
    subprocess.call(['java', '-jar', 'tsimulus.jar', 'ts.json'])

    df = pd.read_csv("output\\output.csv", sep=";")
    dfs = []

    keys = df.series.value_counts().keys()

    if len(keys) > 1:
        for i in keys:
            dfs.append(df[df.series == i])
    else:
        dfs.append(df)

    return dfs
