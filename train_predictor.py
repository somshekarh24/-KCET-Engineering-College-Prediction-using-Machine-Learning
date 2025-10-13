# train_predictor.py
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset paths
datasets = {
    "CSE_GM": r"Data_set\CSE_GM_dataset.csv",
    "CSE_OBC": r"Data_set\CSE_OBC_dataset(1).csv",
    "CSE_SC": r"Data_set\CSE_SC_dataset(1).csv",
    "ISE_GM": r"Data_set\ISE_GM_DATA(1).csv",
    "ISE_OBC": r"Data_set\ISE_OBC_DATA(1).csv",
    "ISE_SC": r"Data_set\ISE_SC_DATA(1).csv"
}

# Colleges mapping for each branch-category
college_lists = {
    "CSE_GM": ['BMSIT','MSRIT','BMSCE','RVCE','PES RING ROAD','DSCE','BIT',
               'JSSCE','PES ELECTRONIC CITY','NIE','MSRUAS','DSAT KANAKAPURA',
               'RVIT','AIT','RNSIT','REVA','OXFORD','DSU HOSUR','MCE',
               'NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK','CAMBRIDGE',
               'GLOBAL','MVJ','AMC','KSIT','DONBOSCO'],
    "CSE_OBC": ['BMSIT','MSRIT','BMSCE','RVCE','PES RING ROAD','DSCE','BIT',
                'JSSCE','PES ELECTRONIC CITY','NIE','MSRUAS','DSAT KANAKAPURA',
                'RVIT','AIT','RNSIT','REVA','OXFORD','DSU HOSUR','MCE',
                'NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK','CAMBRIDGE',
                'GLOBAL','MVJ','AMC','KSIT','DONBOSCO'],
    "CSE_SC": ['BMSIT','MSRIT','BMSCE','RVCE','PES RING ROAD','DSCE','BIT',
               'JSSCE','PES ELECTRONIC CITY','NIE','MSRUAS','DSAT KANAKAPURA',
               'RVIT','AIT','RNSIT','REVA','OXFORD','DSU HOSUR','MCE',
               'NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK','CAMBRIDGE',
               'GLOBAL','MVJ','AMC','KSIT','DONBOSCO'],
    "ISE_GM": ['BMSIT','MSRIT','BMSCE','RVCE','DSCE','BIT','JSSCE','NIE',
               'MSRUAS','DSAT KANAKAPURA','RVIT','AIT','RNSIT','REVA',
               'OXFORD','MCE','NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK',
               'CAMBRIDGE','GLOBAL','MVJ','AMC','DONBOSCO'],
    "ISE_OBC": ['BMSIT','MSRIT','BMSCE','RVCE','DSCE','BIT','JSSCE','NIE',
                'MSRUAS','DSAT KANAKAPURA','RVIT','AIT','RNSIT','REVA',
                'OXFORD','MCE','NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK',
                'CAMBRIDGE','GLOBAL','MVJ','AMC','DONBOSCO'],
    "ISE_SC": ['BMSIT','MSRIT','BMSCE','RVCE','DSCE','BIT','JSSCE','NIE',
               'MSRUAS','DSAT KANAKAPURA','RVIT','AIT','RNSIT','REVA',
               'OXFORD','MCE','NMIT','SMVIT','CMRIT','PRESIDENCY','HKBK',
               'CAMBRIDGE','GLOBAL','MVJ','AMC','DONBOSCO']
}

# Train and save models
for key, path in datasets.items():
    print(f"Training model for {key}...")
    
    df = pd.read_csv(path)
    
    # Map colleges to numeric index
    df['College_idx'] = df['College'].apply(lambda x: college_lists[key].index(x))
    
    X = df[['Rank']]  # Features
    y = df['College_idx']  # Target
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=500, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    
    print(f"MAE={mae:.2f}, RMSE={rmse:.2f}, R²={r2:.4f}")
    
    # Save model
    with open(f"models/model_{key}.pkl", "wb") as f:
        pickle.dump(model, f)
        
print("All models trained and saved successfully!")
