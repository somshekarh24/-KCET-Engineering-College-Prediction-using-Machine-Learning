import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import os

# Ensure models folder exists
os.makedirs('models', exist_ok=True)

# Dataset paths
datasets = {
    "CSE_GM": r"Data_set\CSE_GM_dataset.csv",
    "CSE_OBC": r"Data_set\CSE_OBC_dataset(1).csv",
    "CSE_SC": r"Data_set\CSE_SC_dataset(1).csv",
    "ISE_GM": r"Data_set\ISE_GM_DATA(1).csv",
    "ISE_OBC": r"Data_set\ISE_OBC_DATA(1).csv",
    "ISE_SC": r"Data_set\ISE_SC_DATA(1).csv"
}

for key, path in datasets.items():
    df = pd.read_csv(path)
    
    # Fill missing Rank values
    df['Rank'] = df['Rank'].fillna(df['Rank'].median())

    # Features: Rank + Year
    X = df[['Rank', 'Year']]
    y = df['College']

    # Train RandomForest model
    model = RandomForestClassifier(n_estimators=300, random_state=42)
    model.fit(X, y)

    # Save model
    filename = f"models/model_{key.lower()}.pkl"
    pickle.dump(model, open(filename, 'wb'))
    print(f"✅ Saved model: {filename}")
