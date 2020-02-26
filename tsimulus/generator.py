import pandas as pd
import subprocess


def generate_ts(new_file=True):
    if new_file:
        subprocess.call(['java', '-jar', 'tsimulus.jar', 'ts.json'])

    df = pd.read_csv("output\\output.csv", sep=";", parse_dates=[0])
    dfs = []

    if "series" in df.columns:
        keys = df.series.value_counts().keys()

        for i in keys:
            dfs.append(df[df.series == i])

    else:
        dfs.append(df)

    return dfs
