import pandas as pd

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df['Money_Value'].fillna(value=df['Money_Value'].median(), inplace=True)
    return df

def drop_columns(df: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:
    return df.drop(columns=cols_to_drop)
