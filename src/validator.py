import re


def validate_data(df):

    rejected_rows = []
    valid_rows = []

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    for _, row in df.iterrows():

        is_valid = True

        # Required fields
        if not row["name"] or not row["email"]:
            is_valid = False

        # Email validation
        elif not re.match(email_pattern, row["email"]):
            is_valid = False

        # Date validation
        elif str(row["join_date"]) == "NaT":
            is_valid = False

        if is_valid:
            valid_rows.append(row)
        else:
            rejected_rows.append(row)

    return valid_rows, rejected_rows