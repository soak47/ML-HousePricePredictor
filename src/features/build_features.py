import pandas as pd
from typing import List

def subset_focus_area(df: pd.DataFrame, focus_suburbs: List[str]) -> pd.DataFrame:
    if 'Suburb' in df.columns:
        return df[df['Suburb'].isin(focus_suburbs)].copy()
    return df

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Keep rows with target present
    if 'Price' in df.columns:
        df = df[df['Price'].notnull()].copy()
    # Optional: drop extreme outliers (top/bottom 0.5%)
    if 'Price' in df.columns:
        low, high = df['Price'].quantile([0.005, 0.995])
        df = df[(df['Price'] >= low) & (df['Price'] <= high)].copy()
    return df
