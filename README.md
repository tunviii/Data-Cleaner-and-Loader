# CSV/TSV Data Cleaner & Loader

A Python-based data cleaning and loading pipeline that processes messy CSV and TSV files, validates the data, tracks rejected records, and loads clean data into a PostgreSQL database.

The project simulates a real-world ETL workflow where raw data from external sources may contain missing values, inconsistent formats, duplicate records, and invalid entries.

## Features

* Supports CSV and TSV files
* Removes extra whitespace from text fields
* Handles missing values
* Normalizes inconsistent date formats
* Detects and removes duplicate records
* Validates required fields
* Validates email addresses
* Identifies invalid or corrupted records
* Separates valid and rejected rows
* Stores rejected records for review
* Loads cleaned data into PostgreSQL
* Logs processing activity and data quality metrics
* Generates a summary of processed, fixed, rejected, and loaded rows

## Project Workflow

```text
Raw CSV / TSV File
        │
        ▼
    File Reader
        │
        ▼
   Data Cleaning
   ├── Trim whitespace
   ├── Handle missing values
   ├── Normalize dates
   └── Remove duplicates
        │
        ▼
   Data Validation
   ├── Required fields
   ├── Email validation
   └── Date validation
        │
        ▼
 ┌───────────────┐
 ▼               ▼
Valid Rows    Rejected Rows
 │               │
 ▼               ▼
PostgreSQL    Rejected CSV
 │
 ▼
Processing Logs
```

## Tech Stack

* **Python**
* **Pandas**
* **PostgreSQL**
* **SQLAlchemy**
* **psycopg2**
* **python-dotenv**
* **Python logging**

## Project Structure

```text
data-cleaner-loader/
│
├── data/
│   ├── raw/
│   │   └── messy_data.csv
│   │
│   └── rejected/
│       └── rejected_rows.csv
│
├── src/
│   ├── cleaner.py
│   ├── validator.py
│   ├── database.py
│   └── main.py
│
├── logs/
│   └── app.log
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd data-cleaner-loader
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

Replace the values with your PostgreSQL credentials.

> Do not commit the `.env` file to version control.

## Input Data

The application accepts CSV and TSV files containing structured records.

Example input:

```csv
id,name,email,join_date,salary
1,  Tanvi  ,tanvi@email.com,2024-01-15,50000
2,Rahul,rahul@email.com,15/02/2024,60000
3,Priya,,2024/03/10,55000
4,Aman,aman@email.com,,45000
5,Tanvi,tanvi@email.com,2024-01-15,50000
6,John,john@email,invalid-date,70000
```

The input data may contain:

* Extra whitespace
* Missing values
* Inconsistent date formats
* Duplicate rows
* Invalid email addresses
* Invalid dates

## Data Cleaning

The cleaning pipeline performs the following operations:

### Whitespace Removal

Extra whitespace is removed from string fields.

```text
"  Tanvi  " → "Tanvi"
```

### Date Normalization

Multiple date formats are converted into a consistent datetime format.

Examples:

```text
2024-01-15
15/02/2024
2024/03/10
```

Invalid dates are identified during validation.

### Duplicate Removal

Duplicate records are detected and removed before loading the data into the database.

### Missing Value Handling

Missing values are identified and handled based on validation rules and required fields.

## Data Validation

Each record is validated before being loaded into the database.

Validation checks include:

* Required fields must not be empty
* Email addresses must follow a valid format
* Date fields must contain valid dates
* Invalid records are rejected

Rejected records are stored separately for review.

Example:

```text
id,name,email,rejection_reason

3,Priya,,Missing email

6,John,john@email,Invalid email and date
```

## Database Loading

Validated records are loaded into a PostgreSQL table using SQLAlchemy.

The application separates invalid records from valid records to ensure that only clean and validated data is inserted into the database.

## Logging

The application logs processing activity and data quality metrics.

Example log output:

```text
2026-09-14 12:30:00 - INFO - File processing started
2026-09-14 12:30:01 - INFO - Original rows: 100
2026-09-14 12:30:01 - INFO - Duplicates removed: 5
2026-09-14 12:30:01 - INFO - Rows rejected: 3
2026-09-14 12:30:02 - INFO - Rows loaded: 92
2026-09-14 12:30:02 - INFO - File processing completed
```

Logs are stored in:

```text
logs/app.log
```

## Running the Project

Place your raw data file inside:

```text
data/raw/
```

Run the application:

```bash
python src/main.py
```

## Output

After processing, the application provides a summary similar to:

```text
Processing Complete

Original Rows: 100
Duplicates Removed: 5
Missing Values Detected: 4
Valid Rows: 92
Rejected Rows: 3
Rows Loaded to Database: 92
```

Rejected records are saved to:

```text
data/rejected/rejected_rows.csv
```

Clean and validated records are loaded into PostgreSQL.

## Example Use Case

Organizations often receive data from spreadsheets, exports, or external systems where data quality cannot be guaranteed.

This tool can be used to process files containing:

* Employee records
* Customer data
* Sales data
* Student records
* Inventory data

Before inserting the data into a database, the application cleans and validates the records to improve data quality and prevent invalid database entries.

## Future Improvements

* Add MySQL support
* Add automatic file type detection
* Support custom validation rules
* Add schema validation
* Add command-line arguments using `argparse`
* Generate detailed data quality reports
* Add unit tests using `pytest`
* Support batch processing for large datasets
* Add Docker support
* Add a simple web interface
* Add configurable database tables and column mappings

## Key Concepts Demonstrated

* Data cleaning with Pandas
* Data validation
* ETL pipelines
* Data quality management
* Error handling
* Logging
* PostgreSQL integration
* SQLAlchemy
* Environment variable management
* Rejected record tracking

