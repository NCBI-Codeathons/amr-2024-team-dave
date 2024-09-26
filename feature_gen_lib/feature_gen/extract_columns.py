import os  # Importing the os module to interact with the file system
import pandas as pd  # Importing pandas for data manipulation and file reading

def extract_columns_from_tsv(input_dir, output_file):
    """
    Extract columns 4 (gene) and 5 (EC_number) from each TSV file in a directory
    and store the results in a new TSV file using pandas.
    
    :param input_dir: Directory containing input TSV files.
    :param output_file: Path to the output TSV file.
    """
    
    all_data = []  # Initialize an empty list to store data from all files
    
    # Iterate over each file in the input directory
    for file_name in os.listdir(input_dir):
        # Check if the file has a .tsv extension
        if file_name.endswith('.tsv'):
            # Construct the full path to the input TSV file
            input_file = os.path.join(input_dir, file_name)
            
            # Read the TSV file into a pandas DataFrame, with tab as the delimiter
            df = pd.read_csv(input_file, delimiter='\t')
            
            # Extract columns 'gene' and 'EC_number' from the DataFrame
            extracted_columns = df[['gene', 'EC_number']]

            # Add a new column that contains the file name for identification
            extracted_columns['file_name'] = file_name
            
            # Append the DataFrame (with extracted columns) to the list
            all_data.append(extracted_columns)
    
    # Concatenate all DataFrames in the list into one final DataFrame
    final_df = pd.concat(all_data, ignore_index=True)
    
    # Write the concatenated DataFrame to the output file in TSV format
    final_df.to_csv(output_file, sep='\t', index=False)
