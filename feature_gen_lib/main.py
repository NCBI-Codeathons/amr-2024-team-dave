from feature_gen.genome_importer import genome_import_process
from feature_gen.arg_parse import parse_args
from feature_gen.nucleotide_freq import create_db as create_nucleotide_freq_db


def main():
    # Step 1: Parse the command-line arguments
    args = parse_args()

    # Step 2: Extract the parsed arguments
    # 'fasta_input' is the path to the input FASTA file
    fasta_input = args.fasta
    # 'genome_size' refers to the size of the genome being processed
    genome_size = args.genome_size
    # 'genome_skew' captures the GC/AT skew information of the genome
    genome_skew = args.skew
    # 'output_dir' is the directory where the results will be saved
    output_dir = args.output_dir

    # Step 3: Process the genome input
    # This function takes the FASTA file, genome size, and skew to process the genome
    passed_fasta = genome_import_process(fasta_input, genome_size, genome_skew)

    # Step 4: Create the nucleotide frequency database
    # This function uses the processed FASTA file and saves the nucleotide frequency data to the output directory
    create_nucleotide_freq_db(passed_fasta, output_dir)


# Step 5: Call the 'main' function when the script is executed
if __name__ == "__main__":
    main()
