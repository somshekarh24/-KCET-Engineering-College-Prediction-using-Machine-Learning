# check_missing_values.py

import pandas as pd

# Dataset paths
datasets = {
    "CSE_GM": r"Data_set\CSE_GM_dataset.csv",
    "CSE_OBC": r"Data_set\CSE_OBC_dataset(1).csv",
    "CSE_SC": r"Data_set\CSE_SC_dataset(1).csv",
    "ISE_GM": r"Data_set\ISE_GM_DATA(1).csv",
    "ISE_OBC": r"Data_set\ISE_OBC_DATA(1).csv",
    "ISE_SC": r"Data_set\ISE_SC_DATA(1).csv"
}

print("🔍 Checking missing values in datasets...\n")

for name, path in datasets.items():
    try:
        df = pd.read_csv(path)
        print(f"📂 Dataset: {name}")
        print(df.isna().sum())   # count missing values in each column
        print("-" * 50)
    except Exception as e:
        print(f"❌ Error reading {name}: {e}")
