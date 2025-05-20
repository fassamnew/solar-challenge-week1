import pandas as pd

def load_country_data(file_path, country_name):
    """Load and preprocess data for a specific country."""
    df = pd.read_csv(file_path)
    df["Country"] = country_name
    return df