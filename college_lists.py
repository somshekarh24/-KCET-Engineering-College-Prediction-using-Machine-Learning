import pandas as pd

datasets_to_fix = ["CSE_OBC", "CSE_SC"]
paths = {
    "CSE_OBC": "Data_set/CSE_OBC_dataset(1).csv",
    "CSE_SC": "Data_set/CSE_SC_dataset(1).csv"
}

fix_mapping = {
    "RV": "RVCE",
    "DSAT KANAKAPUR": "DSAT KANAKAPURA"
}

for key in datasets_to_fix:
    df = pd.read_csv(paths[key])
    df['College'] = df['College'].replace(fix_mapping)
    df.to_csv(paths[key], index=False)
    print(f"✅ Fixed dataset {key}")




 
# import pandas as pd

# # Paths to datasets
# datasets = {
#     "CSE_GM": "Data_set/CSE_GM_dataset.csv",
#     "CSE_OBC": "Data_set/CSE_OBC_dataset(1).csv",
#     "CSE_SC": "Data_set/CSE_SC_dataset(1).csv",
#     "ISE_GM": "Data_set/ISE_GM_DATA(1).csv",
#     "ISE_OBC": "Data_set/ISE_OBC_DATA(1).csv",
#     "ISE_SC": "Data_set/ISE_SC_DATA(1).csv"
# }

# # Predefined college lists
# college_lists = {
#     "CSE_GM": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'PES RING ROAD', 'DSCE', 'BIT',
#                'JSSCE', 'PES ELECTRONIC CITY', 'NIE', 'MSRUAS', 'DSAT KANAKAPURA',
#                'RVIT', 'AIT', 'RNSIT', 'REVA', 'OXFORD', 'DSU HOSUR', 'MCE',
#                'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK', 'CAMBRIDGE',
#                'GLOBAL', 'MVJ', 'AMC', 'KSIT', 'DONBOSCO'],
#     "CSE_OBC": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'PES RING ROAD', 'DSCE', 'BIT',
#                 'JSSCE', 'PES ELECTRONIC CITY', 'NIE', 'MSRUAS', 'DSAT KANAKAPURA',
#                 'RVIT', 'AIT', 'RNSIT', 'REVA', 'OXFORD', 'DSU HOSUR', 'MCE',
#                 'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK', 'CAMBRIDGE',
#                 'GLOBAL', 'MVJ', 'AMC', 'KSIT', 'DONBOSCO'],
#     "CSE_SC": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'PES RING ROAD', 'DSCE', 'BIT',
#                'JSSCE', 'PES ELECTRONIC CITY', 'NIE', 'MSRUAS', 'DSAT KANAKAPURA',
#                'RVIT', 'AIT', 'RNSIT', 'REVA', 'OXFORD', 'DSU HOSUR', 'MCE',
#                'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK', 'CAMBRIDGE',
#                'GLOBAL', 'MVJ', 'AMC', 'KSIT', 'DONBOSCO'],
#     "ISE_GM": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'DSCE', 'BIT', 'JSSCE', 'NIE',
#                'MSRUAS', 'DSAT KANAKAPURA', 'RVIT', 'AIT', 'RNSIT', 'REVA',
#                'OXFORD', 'MCE', 'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK',
#                'CAMBRIDGE', 'GLOBAL', 'MVJ', 'AMC', 'DONBOSCO'],
#     "ISE_OBC": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'DSCE', 'BIT', 'JSSCE', 'NIE',
#                 'MSRUAS', 'DSAT KANAKAPURA', 'RVIT', 'AIT', 'RNSIT', 'REVA',
#                 'OXFORD', 'MCE', 'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK',
#                 'CAMBRIDGE', 'GLOBAL', 'MVJ', 'AMC', 'DONBOSCO'],
#     "ISE_SC": ['BMSIT', 'MSRIT', 'BMSCE', 'RVCE', 'DSCE', 'BIT', 'JSSCE', 'NIE',
#                'MSRUAS', 'DSAT KANAKAPURA', 'RVIT', 'AIT', 'RNSIT', 'REVA',
#                'OXFORD', 'MCE', 'NMIT', 'SMVIT', 'CMRIT', 'PRESIDENCY', 'HKBK',
#                'CAMBRIDGE', 'GLOBAL', 'MVJ', 'AMC', 'DONBOSCO']
# }

# for key, path in datasets.items():
#     df = pd.read_csv(path)
#     unknown = set(df['College'].unique()) - set(college_lists[key])
#     if unknown:
#         print(f"⚠️  Dataset {key} has unknown colleges: {unknown}")
#     else:
#         print(f"✅ Dataset {key} has all colleges correctly listed.")

