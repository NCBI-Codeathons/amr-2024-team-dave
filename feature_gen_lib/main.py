from feature_gen.genome_importer import genome_import_process
from feature_gen.arg_parse import parse_args
from feature_gen.nucleotide_freq import create_db as create_nucleotide_freq_db


def main():
    # Parse the arguments
    args = parse_args()

    # Use the parsed arguments
    fasta_input = args.fasta
    genome_size = args.genome_size
    genome_skew = args.skew
    output_dir = args.output_dir

    passed_fasta = genome_import_process(fasta_input, genome_size, genome_skew)
    create_nucleotide_freq_db(passed_fasta, output_dir)


if __name__ == "__main__":
    main()