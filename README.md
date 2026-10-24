# Excel Data Cleaner

A small Python script I made to clean up messy Excel files. If you've ever gotten a spreadsheet with duplicate rows, inconsistent names, extra spaces or missing values, this will sort most of that out for you automatically.

## What it fixes

- Removes duplicate rows
- Trims extra spaces from text
- Cleans up column names (lowercase, underscores instead of spaces)
- Makes text formatting consistent (Title Case)
- Fills in missing/blank cells instead of leaving them empty

## Requirements

- Python 3.7 or newer
- pandas
- openpyxl

Install them with:

```bash
pip install pandas openpyxl
```

## How to use it

1. Put your Excel file in the same folder as `excel_cleaner.py`
2. Open `excel_cleaner.py` and update these two lines at the top with your file names:

```python
INPUT_FILE = "messy_data.xlsx"
OUTPUT_FILE = "cleaned_data.xlsx"
```

3. Run it:

```bash
python excel_cleaner.py
```

4. Check the folder - you'll have a new file (`cleaned_data.xlsx` by default) with everything cleaned up.

## Don't have messy data to test with?

There's also a `create_messy_data.py` script included that generates a sample messy spreadsheet so you can try the cleaner out without needing your own file. Just run:

```bash
python create_messy_data.py
```

This creates `messy_data.xlsx` with some duplicate rows, inconsistent capitalization, and missing values baked in, so you can see the cleaner actually do its job.

## Notes

- Missing text cells get filled with `"Unknown"`, missing numbers get filled with `0`. You can change this in the `fill_missing_values` function if you want different defaults.
- By default it title-cases every text column. If you only want specific columns changed, pass a list into `standardize_text_case()`, e.g. `standardize_text_case(data, columns_to_fix=["city", "name"])`.

## License

Feel free to use or modify this however you like.
