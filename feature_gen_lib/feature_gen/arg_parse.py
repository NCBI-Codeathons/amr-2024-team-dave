import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Methods for extracting features from genomic data')

    # Required arguments
    parser.add_argument('-f', '--fasta', type=str, required=True, help='Path to FASTA file')
    parser.add_argument('-o', '--output', type=str, required=True, help='path to ouput folder')

    # Optional args

    return parser.parse_args()
