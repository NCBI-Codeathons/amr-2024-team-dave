from feature_gen.genome_importer import genome_import_process
from feature_gen.arg_parse import parse_args


def main():
    # Parse the arguments
    args = parse_args()

    # Use the parsed arguments
    fasta_input = args.fasta
    genome_size = args.genome_size
    genome_skew = args.skew

    genome_import_process(fasta_input, genome_size, genome_skew)


if __name__ == "__main__":
    main()