import pandas as pd


def clean_data(df):
    stats = {
        "original_rows": len(df),
        "duplicates_removed": 0,
        "missing_values_fixed": 0
    }

    # Remove whitespace from strings
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Count missing values
    stats["missing_values_fixed"] = df.isnull().sum().sum()

    # Remove duplicates
    before = len(df)

    df = df.drop_duplicates()

    stats["duplicates_removed"] = before - len(df)
    return df, stats

def clean_dates(df, column):
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce",
        format="mixed"
    )


    return df