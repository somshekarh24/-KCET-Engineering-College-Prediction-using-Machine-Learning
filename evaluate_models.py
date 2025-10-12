import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import os

# Dataset paths
datasets = {
    "CSE_GM": r"Data_set\CSE_GM_dataset.csv",
    "CSE_OBC": r"Data_set\CSE_OBC_dataset(1).csv",
    "CSE_SC": r"Data_set\CSE_SC_dataset(1).csv",
    "ISE_GM": r"Data_set\ISE_GM_DATA(1).csv",
    "ISE_OBC": r"Data_set\ISE_OBC_DATA(1).csv",
    "ISE_SC": r"Data_set\ISE_SC_DATA(1).csv"
}

print("📊 Evaluating all models...\n")

for key, path in datasets.items():
    if not os.path.exists(path):
        print(f"⚠️ Dataset not found: {path}")
        continue

    df = pd.read_csv(path)

    # Drop unnecessary columns if present
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # Ensure no NaNs
    df = df.dropna()

    # Features and target
    X = df[['Rank']]  # Only using Rank as feature
    y = df['College']

    # Train RandomForestClassifier
    model = RandomForestClassifier(n_estimators=300, random_state=42)
    model.fit(X, y)

    # Predict on same dataset (for simplicity)
    y_pred = model.predict(X)

    # Map College names to numbers for MAE/RMSE calculation
    college_map = {college: idx for idx, college in enumerate(sorted(df['College'].unique()))}
    y_num = [college_map[val] for val in y]
    y_pred_num = [college_map[val] for val in y_pred]

    mae = mean_absolute_error(y_num, y_pred_num)
    rmse = np.sqrt(mean_squared_error(y_num, y_pred_num))
    r2 = r2_score(y_num, y_pred_num)

    print(f"Model {key}:")
    print(f"  MAE  = {mae:.2f}")
    print(f"  RMSE = {rmse:.2f}")
    print(f"  R²   = {r2:.4f}")
    print("-" * 50)
