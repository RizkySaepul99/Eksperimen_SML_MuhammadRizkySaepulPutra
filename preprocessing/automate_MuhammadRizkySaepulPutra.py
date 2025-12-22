import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df = df.loc[~df['Position'].str.contains('GK', na=False)].copy()

    df = df.drop(columns=[
        'Alternative positions', 'GK Handling', 'GK Kicking',
        'GK Positioning', 'GK Reflexes', 'GK Diving',
        'url', 'card', 'play style', 'Height', 'Weight',
        'ID', 'Rank', 'Name', 'GENDER', 'Position',
        'Preferred foot', 'Nation', 'League', 'Team', 'Age'
    ])

    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

def run_all_steps():
    df = load_data("EAFC26_raw.csv")
    df_clean = preprocess_data(df)
    save_data(df_clean, "preprocessing/EAFC26_preprocessing.csv")
    return df_clean

if __name__ == "__main__":

    run_all_steps()

