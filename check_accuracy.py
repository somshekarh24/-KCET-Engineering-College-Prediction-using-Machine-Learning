import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
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

# Collect all colleges for LabelEncoder
all_colleges = set()
for path in datasets.values():
    if os.path.exists(path):
        df = pd.read_csv(path)
        all_colleges.update(df['College'].unique())

le_college = LabelEncoder().fit(list(all_colleges))

print("📊 Model Accuracies:\n")

for key, path in datasets.items():
    if not os.path.exists(path):
        print(f"{key}: Dataset not found, skipping.")
        continue

    df = pd.read_csv(path)
    df = df.dropna(subset=['Rank', 'College'])  # Remove missing values

    X = df[['Rank']]
    y = le_college.transform(df['College'])

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(X_test, y_test) * 100
    print(f"Model {key}: Accuracy = {accuracy:.2f}%")
