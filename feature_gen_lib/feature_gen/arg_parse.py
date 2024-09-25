import argparse  # Importing argparse to handle command-line arguments

def parse_args():
    # Create a parser object and provide a description of the tool's purpose
    parser = argparse.ArgumentParser(description='Methods for extracting features from genomic data')

    # Required arguments for running the tool
    # Path to the input FASTA file containing genomic sequences
    parser.add_argument('-f', '--fasta', type=str, required=True, help='Path to FASTA file')

    # Expected size of the genome in megabytes (user needs to provide an estimate)
    parser.add_argument('-g', '--genome_size', type=float, required=True, help='Estimated genome size in MB')

    # Percentage skew allowed in the genome size to handle small variations during processing
    parser.add_argument('-s', '--skew', type=float, required=True, help='% skew allowed in genome size')

    # Output directory where the results of feature extraction will be stored
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to output folder')

    # Parse all the provided arguments and return them
    args = parser.parse_args()
    return args  # These parsed arguments will be passed to the main function
