import re

def validate_sql_insert(sql_insert):
    # Extract table name and columns
    table_pattern = re.compile(r"INSERT INTO (\w+) \((.*?)\) VALUES")
    match = table_pattern.search(sql_insert)
    if not match:
        raise ValueError("Invalid SQL INSERT statement format.")
    
    table_name = match.group(1)
    columns = [col.strip() for col in match.group(2).split(",")]
    num_columns = len(columns)
    
    # Extract rows
    row_pattern = re.compile(r"\((.*?)\)")
    rows = row_pattern.findall(sql_insert)
    
    # Collect errors
    errors = []
    
    # Validate each row
    for i, row in enumerate(rows):
        values = [val.strip() for val in row.split(",")]
        if len(values) != num_columns:
            errors.append(f"Row {i + 1}: Expected {num_columns} columns, but found {len(values)} columns.")
    
    # Report errors or success
    if errors:
        print(f"Validation failed for table '{table_name}':")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"Validation successful: {len(rows)} rows in table '{table_name}' have {num_columns} columns each.")

def validate_sql_file(file_path):
    try:
        with open(file_path, "r") as file:
            sql_insert = file.read()
        validate_sql_insert(sql_insert)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to the SQL file: ")
    validate_sql_file(file_path)