import os
import pandas as pd

def parse_prokka_txt_output(sample_id, input_file, output_file):
    """
    Parses a prokka txt output file to extract relevant fields and write them to a new TSV file.
    
    :param input_file: Path to the input file.
    :param output_file: Path/name of the output TSV file.
    """
    
    columns_of_interest = ['CDS', 'gene', 'rRNA', 'tRNA', 'tmRNA']
    
    # Read the input file
    with open(input_file, 'r') as file:
        # Parse the file content as key-value pairs
        data = {}
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
    
    # Extract values for the columns of interest
    extracted_data = {col: data.get(col, '') for col in columns_of_interest}

    # Add the sample id to the extracted data
    extracted_data['sample_id'] = sample_id
    
    # Extract the file name
    file_name_without_extension = os.path.splitext(os.path.basename(input_file))[0]
    
    # Add the file name to the extracted data
    extracted_data['file_name'] = file_name_without_extension
    
    # Convert to a DataFrame
    df = pd.DataFrame([extracted_data])
    
    # Reorder the columns to put 'file_name' first
    df = df[['sample_id'] + ['file_name'] + columns_of_interest]
    
    # Write to output TSV file
    df.to_csv(output_file, index=False)

