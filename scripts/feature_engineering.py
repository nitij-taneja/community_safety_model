import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_data(file_path):
    """Load processed data."""
    return pd.read_csv(file_path)

def normalize_geo_features(df):
    """Normalize latitude and longitude using MinMaxScaler."""
    scaler = MinMaxScaler()
    df[['Latitude (Accommodation)', 'Longitude (Accommodation)']] = scaler.fit_transform(
        df[['Latitude (Accommodation)', 'Longitude (Accommodation)']]
    )
    df[['Latitude (Incident)', 'Longitude (Incident)']] = scaler.fit_transform(
        df[['Latitude (Incident)', 'Longitude (Incident)']]
    )
    return df

def engineer_features(df):
    """Engineer new features."""
    # Encode categorical features
    label_enc = LabelEncoder()
    df['Encoded_Commute_Mode'] = label_enc.fit_transform(df['Commute Mode(s)'])
    df['Encoded_Accommodation'] = label_enc.fit_transform(df['Type of Accommodation'])

    # Extract time-based features
    df['Leave_Hour'] = pd.to_datetime(df['When Do You Leave for College?'], format='%H:%M', errors='coerce').dt.hour
    df['Leave_Day'] = pd.to_datetime(df['When Do You Leave for College?'], format='%H:%M', errors='coerce').dt.dayofweek
    # Generate a simple risk score
    df['Risk_Score'] = df['Has Incident'] + df['How many incidents have you experienced?']

    # Normalize geographical features
    df = normalize_geo_features(df)

    return df

if __name__ == "__main__":
    # File paths
    processed_data_path = "./data/processed_epics_data.csv"
    feature_engineered_data_path = "./data/feature_engineered_data.csv"

    # Load and process data
    df = load_data(processed_data_path)
    engineered_df = engineer_features(df)

    # Save feature-engineered dataset
    engineered_df.to_csv(feature_engineered_data_path, index=False)
    print(f"Feature-engineered data saved to {feature_engineered_data_path}")

