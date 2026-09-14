import pandas as pd

from cleaner import clean_data
from validator import validate_data
from database import get_engine


def main():

    # Read file
    df = pd.read_csv("data/raw/messy_data.csv")

    # Clean
    df, stats = clean_data(df)

    # Validate
    valid_rows, rejected_rows = validate_data(df)

    valid_df = pd.DataFrame(valid_rows)

    rejected_df = pd.DataFrame(rejected_rows)

    # Save rejected rows
    rejected_df.to_csv(
        "data/rejected/rejected_rows.csv",
        index=False
    )

    # Database
    engine = get_engine()

    # Load valid data
    valid_df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )

    print("Processing complete")

    print(stats)

    print(
        f"Valid rows: {len(valid_df)}"
    )

    print(
        f"Rejected rows: {len(rejected_df)}"
    )


if __name__ == "__main__":
    main()