import pandas as pd

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Clean and preprocess the data."""
    # Fill missing values
    df['Where Did the Incident Happen?'] = df['Where Did the Incident Happen?'].fillna("None")
    df['Describe the incident'] = df['Describe the incident'].fillna("None")
    df['At which date the incident happen?'] = df['At which date the incident happen?'].fillna("None")
    df['At what time the incident happen?'] = df['At what time the incident happen?'].fillna("None")
    df['Latitude (Incident)'] = df['Latitude (Incident)'].fillna(0.0)
    df['Longitude (Incident)'] = df['Longitude (Incident)'].fillna(0.0)

    # Convert Pincode to string
    df['Pincode'] = df['Pincode'].astype(str)

    # Create derived column for 'Has Incident'
    df['Has Incident'] = df['Have You Experienced Any Safety Incidents?'].apply(lambda x: 1 if x != 'None' else 0)

    return df

if __name__ == "__main__":
    # File paths
    raw_data_path = "../data/epics_data.csv"
    processed_data_path = "../data/processed_epics_data.csv"

    # Load and process data
    df = load_data(raw_data_path)
    processed_df = preprocess_data(df)

    # Save processed data
    processed_df.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")
