import pandas as pd
# STEP 0: Settings - change these to match the file
INPUT_FILE = "messy_data.xlsx"
OUTPUT_FILE = "cleaned_data.xlsx"

def load_excel(file_path):
    # Read the Excel file into a pandas DataFrame (a table).
    print(f"Reading file: {file_path}")
    data = pd.read_excel(file_path)
    print(f"Loaded {len(data)} rows and {len(data.columns)} columns.\n")
    return data

def clean_column_names(data):
    # Make column names lowercase, trimmed and use underscores instead of spaces.
    print("Cleaning column names...")
    new_columns = []
    for col in data.columns:
        col = str(col).strip()          # remove leading/trailing spaces
        col = col.lower()                # make lowercase
        col = col.replace(" ", "_")      # replace spaces with underscores
        new_columns.append(col)
    data.columns = new_columns
    print("New column names:", list(data.columns), "\n")
    return data

def trim_text_cells(data):
    # Remove extra spaces from text values, like '  Ali  ' -> 'Ali'.
    print("Trimming extra spaces from text cells...")
    for col in data.columns:
        if data[col].dtype == "object":  
            data[col] = data[col].apply(
                lambda value: value.strip() if isinstance(value, str) else value
            )
    return data

def standardize_text_case(data, columns_to_fix=None):
    print("Standardizing text case (Title Case)...")
    target_columns = columns_to_fix if columns_to_fix else data.columns
    for col in target_columns:
        if col in data.columns and data[col].dtype == "object":
            data[col] = data[col].apply(
                lambda value: value.title() if isinstance(value, str) else value
            )
    return data

def remove_duplicate_rows(data):
    # Remove rows that are exact duplicates of another row.
    print("Removing duplicate rows...")
    before = len(data)
    data = data.drop_duplicates()
    after = len(data)
    print(f"Removed {before - after} duplicate row(s).\n")
    return data

def fill_missing_values(data):
    # Fill empty cells with something reasonable instead of leaving them blank.
    print("Filling missing values...")
    for col in data.columns:
        if data[col].dtype == "object":
            # Empty text cells -> "Unknown"
            data[col] = data[col].fillna("Unknown")
        else:
            # Empty number cells -> 0
            data[col] = data[col].fillna(0)
    return data

def save_excel(data, file_path):
    # Save the cleaned table to a new Excel file.
    data.to_excel(file_path, index=False)
    print(f"Cleaned file saved as: {file_path}")

def main():
    data = load_excel(INPUT_FILE)
    data = clean_column_names(data)
    data = trim_text_cells(data)
    data = standardize_text_case(data)
    data = remove_duplicate_rows(data)
    data = fill_missing_values(data)
    save_excel(data, OUTPUT_FILE)
    print("\nAll done! Your file has been cleaned.")
if __name__ == "__main__":
    main()