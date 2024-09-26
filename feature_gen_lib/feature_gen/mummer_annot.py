import os
import pandas as pd

def parse_mummer_output(sample_id, input_file, output_file):
    """
    Parses a MUMMER output file to extract relevant fields and write them to a new TSV file.
  
    :param input_file: Path to the MUMMER output file.
    :param output_file: Path/name of the output TSV file.
    """

    # Extract the base name of the file to use in the first column. Ensure file name is distinct
    file_name_without_extension = os.path.splitext(os.path.basename(input_file))[0]

    # Initialize the fields to store the extracted data from the QRY column
    total_snps = ''
    total_gsnps = ''
    total_indels = ''
    total_gindels = ''

    # Read the file line by line to extract the relevant fields from the QRY column
    with open(input_file, 'r') as f:
        for line in f:
            if line.startswith('TotalSNPs'):
                # Extract the QRY value (second column, after the REF column)
                total_snps = line.split()[2]
            if line.startswith('TotalGSNPs'):
                total_gsnps = line.split()[2]
            if line.startswith('TotalIndels'):
                total_indels = line.split()[2]
            if line.startswith('TotalGIndels'):
                total_gindels = line.split()[2]

    # Create a DataFrame for the extracted data
    extracted_data = pd.DataFrame({
        'sample_id': [sample_id],
        'file_name': [file_name_without_extension],
        'TotalSNPs': [total_snps],
        'TotalGSNPs': [total_gsnps],
        'TotalIndels': [total_indels],
        'TotalGIndels': [total_gindels]
    })

    # Write the DataFrame to a TSV file
    extracted_data.to_csv(output_file, index=False)

