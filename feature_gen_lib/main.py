from feature_gen.genome_importer import genome_import_process
from feature_gen.arg_parse import parse_args
from feature_gen.nucleotide_freq import create_db as create_nucleotide_freq_db


def main():
    # Parse the arguments
    args = parse_args()

    # Use the parsed arguments
    fasta_input = args.fasta
    output_dir = args.output

    passed_fasta = genome_import_process(fasta_input)
    create_nucleotide_freq_db(passed_fasta, output_dir)


if __name__ == "__main__":
    main()