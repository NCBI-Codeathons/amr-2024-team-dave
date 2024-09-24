import os
import pandas as pd

def extract_columns_from_tsv(input_dir, output_file):
    """
    Extract columns 4 (gene) and 5 (EC_number) from each TSV file in a directory
    and store the results in a new TSV file using pandas.
    
    :param input_dir: Directory containing input TSV files.
    :param output_file: Path to the output TSV file.
    """
    
    all_data = []
    
    # Iterate over each file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.tsv'):
            input_file = os.path.join(input_dir, file_name)
            
            # Read the TSV file with pandas
            df = pd.read_csv(input_file, delimiter='\t')
            
            # Extract columns 4 (gene) and 5 (EC_number)
            extracted_columns = df[['gene', 'EC_number']]

            # Add a new column with the file name
            extracted_columns['file_name'] = file_name
            
            # Append to the list
            all_data.append(extracted_columns)
    
    # Concatenate all the dataframes and save output as a TSV file
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv(output_file, sep='\t', index=False)
