<<<<<<< HEAD
# Melbourne House Price Predictor (Malvern East Focus)

A guided ML engineering starter project to predict property sale prices in the Melbourne metro area, with an initial focus on Malvern East and neighbouring suburbs. Built as a clean, portfolio-ready repository with a reproducible baseline model and space for iterative improvement.

## Quick Start

1. **Create & activate a virtual environment**
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Download data**
   - Primary property-level dataset: export the **Melbourne Housing Market** CSV from Kaggle and save it to `data/raw/melbourne_housing.csv`.
   - (Optional) External suburban medians: download the latest **Victorian Property Sales Report (VPSR)** suburb medians (Excel/CSV) and place in `data/external/vpsr/` for feature augmentation later.

3. **Run the baseline notebook**
   - Open `notebooks/02_baseline_model.ipynb`, run all cells. This will:
     - Load & filter for Malvern East area
     - Build a preprocessing + model pipeline
     - Train/test split
     - Evaluate with MAE/RMSE
     - Save the model to `models/baseline.joblib`

4. **(Alt) Run as a script**
   ```bash
   python -m src.models.train_baseline --config config/params.yaml
   ```

5. **Next steps**
   - Enrich features (suburb medians by quarter, distance-to-CBD, time on market, etc.)
   - Try stronger models (XGBoost/LightGBM), cross-validation, hyperparameter search
   - Add experiment tracking (MLflow) and tidy visualizations for the report

## Repository Layout

```
melbourne-house-price-predictor/
├── config/params.yaml            # Data paths, features, model settings
├── data/
│   ├── raw/                      # melbourne_housing.csv goes here
│   ├── processed/                # cleaned, model-ready parquet/csv
│   └── external/                 # VPSR & other external datasets
├── models/                       # saved models (ignored by git)
├── notebooks/
│   ├── 01_eda.ipynb              # first-look EDA & data quality checks
│   └── 02_baseline_model.ipynb   # preprocessing + baseline regressor
├── reports/figures/              # charts (ignored by git)
├── src/
│   ├── data/make_dataset.py      # raw -> processed
│   ├── features/build_features.py# feature creation utilities
│   ├── models/train_baseline.py  # script version of baseline
│   └── utils/data_loading.py     # robust CSV reading, date parsing
├── tests/                        # simple smoke tests
├── .gitignore
├── requirements.txt
└── README.md
```

## Notes

- The baseline model uses scikit-learn's `ColumnTransformer` for preprocessing and a `RandomForestRegressor` for a strong, explainable baseline.
- The config file controls the focus suburbs, target, and features so you can expand to all of Melbourne (or Australia) later with minimal code changes.
- Keep large files out of Git; this repo is structured to be shareable on GitHub without including raw data.

---

*Built with ❤️ by Byte for Forge.*
=======
# ML HousePricePredictor
Predict house prices given features like rooms, sq footage,neighborhood
Using an Ai model to teach myself the basics of ML engineering concepts
>>>>>>> 3d2f22fff081875a176e3b453b98a7712334f8ae
