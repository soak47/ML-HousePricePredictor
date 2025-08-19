import pandas as pd

def load_melbourne_csv(path: str) -> pd.DataFrame:
    # Kaggle dataset uses mixed date formats; ensure parse with dayfirst True
    df = pd.read_csv(path)
    # Normalize column names if needed (strip spaces etc.)
    df.columns = [c.strip().replace(' ', '') for c in df.columns]
    # Parse Date if present
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        df['Year'] = df['Date'].dt.year
        df['Quarter'] = df['Date'].dt.to_period('Q').astype(str)
        df['Month'] = df['Date'].dt.month
    return df
