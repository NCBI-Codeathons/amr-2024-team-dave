import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Methods for extracting features from genomic data')

    # Required arguments
    parser.add_argument('-f', '--fasta', type=str, required=True, help='Path to FASTA file')
    parser.add_argument('-g','--genome_size', type=float, required=True, help='Estimated genome size in MB')
    parser.add_argument('-s', '--skew', type=float, required=True, help='% skew allowed in genome size')

    return args
