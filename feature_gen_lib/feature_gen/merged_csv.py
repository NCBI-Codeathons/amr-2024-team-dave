import pandas as pd
import os

# Define the folder containing your CSV files
folder_path = 'Your/Folder/path/to/csv/folder'  # Replace with your folder path
output_file = 'your_filenames.csv'  # Output file

# Initialize an empty list to store the dataframes
dataframes = []
all_columns = set()  # To store all unique columns

# Optionally define a custom fill value for missing data (None or NaN by default)
fill_value = None  # Set this to a specific value like 0 or 'Missing' if desired

# Optional: Predefine a column order to follow (leave as None if you don't want this)
custom_column_order = None  # E.g., ['col1', 'col2', 'col3', 'file_name']

# Loop through all CSV files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Full path to the CSV file
        file_path = os.path.join(folder_path, file_name)
        
        try:
            # Progress log
            print(f"Reading file: {file_name}")
            
            # Read the CSV file (optionally in chunks for large files)
            df = pd.read_csv(file_path)
            
            # Add the file name column to keep track of the file source
            df['file_name'] = file_name
            
            # Append the dataframe to the list
            dataframes.append(df)
            
            # Update the set of all unique columns
            all_columns.update(df.columns)
        
        except Exception as e:
            # Handle exceptions (e.g., read errors)
            print(f"Error reading {file_name}: {e}")
            continue

# Convert the set of all unique columns to a sorted list
all_columns = sorted(list(all_columns))

# If a custom column order is provided, use it
if custom_column_order:
    all_columns = custom_column_order

# Reindex each dataframe to have the same columns, filling missing values with the specified fill_value
for i in range(len(dataframes)):
    dataframes[i] = dataframes[i].reindex(columns=all_columns, fill_value=fill_value)

# Concatenate all dataframes, ignoring the index
merged_df = pd.concat(dataframes, ignore_index=True)

# Remove duplicate rows if necessary (optional)
merged_df.drop_duplicates(inplace=True)

# Save the merged dataframe to a single CSV file
try:
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved to {output_file}")
except Exception as e:
    print(f"Error saving merged CSV: {e}")
