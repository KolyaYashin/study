import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:

    def elastic_for_unit(df_sku):
        df_sku.loc[:, 'sku'] = [1] * len(df_sku)
        x = df_sku[['sku', 'price']]
        y = np.log(df_sku['qty'] + 1)
        lin = LinearRegression()
        lin.fit(x, y)
        lin.predict(x)
        return r2_score(y, lin.predict(x))

    df = df.copy()
    elastics = pd.DataFrame()
    elastics['sku'] = df['sku'].unique()
    elastics['elasticity'] = 1.0
    for i in range(len(df['sku'].unique())):
        df_skuf = df[df['sku'] == df['sku'].unique()[i]]
        elastics.loc[i, 'elasticity'] = elastic_for_unit(df_skuf)

    return elastics
