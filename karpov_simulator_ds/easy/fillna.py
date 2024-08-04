import pandas as pd
import numpy as np


def fillna_with_mean(
    df: pd.DataFrame, target: str, group: str
) -> pd.DataFrame:

    df_new = df.copy()
    df_filled = df_new[df_new[target].notna()]
    means = df_filled.groupby(group).agg(lambda x: np.floor(np.mean(x)))

    for i in range(len(df_new)):
        if pd.isna(df_new[target].iloc[i]):
            gr = df_new[group].iloc[i]
            df_new.loc[i, target] = means[target][gr]

    return df_new
