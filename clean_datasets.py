# clean_datasets.py

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

print("🧹 Cleaning datasets...\n")

for name, path in datasets.items():
    try:
        df = pd.read_csv(path)

        # Drop useless "Unnamed: 0" if exists
        if "Unnamed: 0" in df.columns:
            df = df.drop(columns=["Unnamed: 0"])
            print(f"✔️ Dropped 'Unnamed: 0' from {name}")

        # Drop rows with missing values
        before = len(df)
        df = df.dropna()
        after = len(df)
        if before != after:
            print(f"✔️ Dropped {before - after} rows with NaN from {name}")

        # Save cleaned file (overwrite original)
        df.to_csv(path, index=False)
        print(f"✅ Cleaned dataset saved: {path}\n")

    except Exception as e:
        print(f"❌ Error cleaning {name}: {e}")
