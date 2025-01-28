import re
import uuid
import csv
import os
from typing import Dict, List, Set, Optional

def parse_sql_file(sql_file: str) -> List[Dict[str, str]]:
    """
    Parses an SQL file to extract rows of data.
    
    Args:
        sql_file: Path to the input SQL file.
    
    Returns:
        A list of dictionaries representing the rows and their columns.
    """
    rows = []
    with open(sql_file, "r") as file:
        sql_content = file.read()

    # Use regex to extract rows of data
    row_pattern = re.compile(
        r"\((\d+),\s*(\d+),\s*'([^']*)',\s*'([^']*)',\s*(\d+)\)", 
        re.MULTILINE
    )
    matches = row_pattern.findall(sql_content)

    # Define column names (since they are not in the data)
    columns = ["id", "thumb_id", "name", "alias", "released"]

    for match in matches:
        # Create a dictionary for the row
        row = dict(zip(columns, match))
        rows.append(row)

    return rows

def generate_uuid_mapping(rows: List[Dict[str, str]], columns_to_update: Set[str]) -> Dict[str, Dict[str, str]]:
    """
    Generates a mapping of old IDs to new UUIDs for specified columns.
    
    Args:
        rows: List of dictionaries representing the rows.
        columns_to_update: Set of column names to generate mappings for.
    
    Returns:
        A dictionary where keys are column names and values are mappings of old IDs to new UUIDs.
    """
    mappings = {col: {} for col in columns_to_update}
    for row in rows:
        for col in columns_to_update:
            old_id = row.get(col)  # Use .get() to avoid KeyError
            if old_id and old_id not in mappings[col]:
                mappings[col][old_id] = str(uuid.uuid4())  # Generate a new UUID
    return mappings

def rewrite_sql_file(rows: List[Dict[str, str]], mappings: Dict[str, Dict[str, str]], output_file: str):
    """
    Rewrites the SQL file with new UUIDs and saves it to the output file.
    
    Args:
        rows: List of dictionaries representing the rows.
        mappings: Dictionary of mappings for each column.
        output_file: Path to the output SQL file.
    """
    with open(output_file, "w") as file:
        # Write the INSERT INTO statement with column names
        columns = ", ".join(rows[0].keys())  # Get column names from the first row
        file.write(f"INSERT INTO demo_artists ({columns}) VALUES\n")

        # Write each row's values
        for i, row in enumerate(rows):
            # Replace old IDs with new UUIDs for specified columns
            for col, mapping in mappings.items():
                if row.get(col) in mapping:  # Use .get() to avoid KeyError
                    row[col] = mapping[row[col]]

            # Prepare the row values
            values = ", ".join([f"'{val}'" if val is not None else "NULL" for val in row.values()])
            file.write(f"({values})")

            # Add a comma after each row except the last one
            if i < len(rows) - 1:
                file.write(",\n")
            else:
                file.write(";\n")  # End with a semicolon

def save_mappings(mappings: Dict[str, Dict[str, str]], output_dir: Optional[str] = None):
    """
    Saves the ID mappings to separate CSV files or returns them as dictionaries.
    
    Args:
        mappings: Dictionary of mappings for each column.
        output_dir: Directory to save the mapping files. If None, mappings are returned as dictionaries.
    
    Returns:
        If output_dir is None, returns the mappings as dictionaries. Otherwise, saves them to disk.
    """
    if output_dir:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Save mappings to CSV files
        for col, mapping in mappings.items():
            output_file = os.path.join(output_dir, f"{col}_mapping.csv")
            with open(output_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["old_id", "new_uuid"])  # Write header
                for old_id, new_uuid in mapping.items():
                    writer.writerow([old_id, new_uuid])
            print(f"Mapping for {col} saved to {output_file}")
    else:
        # Return mappings as dictionaries
        return mappings

def main(
    sql_file: str,
    columns_to_update: Set[str],
    output_sql_file: str,
    output_mapping_dir: Optional[str] = None,
):
    """
    Main function to process the SQL file, generate UUIDs, and rewrite the SQL file.
    
    Args:
        sql_file: Path to the input SQL file.
        columns_to_update: Set of column names to update with UUIDs.
        output_sql_file: Path to the output SQL file.
        output_mapping_dir: Directory to save the mapping files. If None, mappings are kept in memory.
    """
    # Check if output_sql_file is provided
    if not output_sql_file:
        raise ValueError("Output SQL file path must be provided.")

    # Create the directory for the output SQL file if it doesn't exist
    os.makedirs(os.path.dirname(output_sql_file), exist_ok=True)

    # Parse the SQL file
    rows = parse_sql_file(sql_file)
    print(f"Parsed {len(rows)} rows from the SQL file.")

    # Generate UUID mappings for specified columns
    mappings = generate_uuid_mapping(rows, columns_to_update)
    print(f"Generated UUID mappings for columns: {columns_to_update}")

    # Rewrite the SQL file with new UUIDs
    rewrite_sql_file(rows, mappings, output_sql_file)
    print(f"Rewritten SQL file saved to {output_sql_file}")

    # Save or return the mappings
    if output_mapping_dir:
        save_mappings(mappings, output_mapping_dir)
    else:
        # Keep mappings in memory
        print("Mappings are kept in memory.")
        return mappings

# Example usage
if __name__ == "__main__":
    sql_file = "/Users/home/Downloads/ljb_artists_20250127.sql"  # Path to your input SQL file
    columns_to_update = {"id"}  # Columns to update with UUIDs
    output_sql_file = "./ljb_artists_cleaned_20250127.sql"  # Path to save the new SQL file
    output_mapping_dir = "./mappings"  # Directory to save the mapping files (set to None to keep in memory)

    # Choose whether to save mappings to disk or keep them in memory
    use_memory = False  # Set to True to keep mappings in memory
    if use_memory:
        mappings = main(sql_file, columns_to_update, output_sql_file, None)
        print("Mappings in memory:", mappings)
    else:
        main(sql_file, columns_to_update, output_sql_file, output_mapping_dir)