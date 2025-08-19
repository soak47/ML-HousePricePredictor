import os, yaml, pandas as pd
from src.utils.data_loading import load_melbourne_csv
from src.features.build_features import subset_focus_area, basic_clean

def main():
    with open('config/params.yaml', 'r') as f:
        cfg = yaml.safe_load(f)

    df = load_melbourne_csv(cfg['data_path'])
    df = subset_focus_area(df, cfg.get('focus_suburbs', []))
    df = basic_clean(df)

    os.makedirs('data/processed', exist_ok=True)
    out_path = 'data/processed/melbourne_clean.parquet'
    df.to_parquet(out_path, index=False)
    print(f"Wrote {len(df):,} rows -> {out_path}")

if __name__ == '__main__':
    main()
