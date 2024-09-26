import argparse  # Importing argparse to handle command-line arguments

def parse_args():
    # Create a parser object and provide a description of the tool's purpose
    parser = argparse.ArgumentParser(description='Methods for extracting features from genomic data')

    # Required arguments
    parser.add_argument('-m', '--mode', required=True, type=str, help='mode to run: choices = [ nuc_feat, pro_feat, fetch, remove_guided, mummer_parse, prokka_parse]')

    # Optional basd on mode
    parser.add_argument('-f', '--fasta', type=str, help='Path to nuclotide FASTA file')
    parser.add_argument('-p', '--protein', type=str, help='Path to amino acid FASTA file from prokka')
    parser.add_argument('-o', '--output', type=str, help='path to ouput folder or file')
    parser.add_argument('-e', '--email', type=str, help='email for entrez')
    parser.add_argument('-a', '--accession_name', type=str, help='NCBi Assembly Name')
    parser.add_argument('-i', '--input', type=str, help='Input File')
    parser.add_argument('-s', '--sample', type=str, help='Sample ID')


    # Optional args

    return parser.parse_args()
