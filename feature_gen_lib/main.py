from feature_gen.genome_importer import genome_import_process
from feature_gen.arg_parse import parse_args
from feature_gen.nucleotide_freq import create_db as create_nucleotide_freq_db
from feature_gen.fetch_assembly import download_assembly
from feature_gen.protein_importer import read_protein_fasta
from feature_gen.aminoacid_freq import create_db as create_aminoacid_freq_db
from feature_gen.remove_guided import remove_guided_process as remove_guided


def main():
    # Parse the arguments
    args = parse_args()

    # parse the mode to run in
    mode = args.mode

    if mode == 'nuc_feat':
        fasta_input = args.fasta
        output_dir = args.output

        passed_fasta = genome_import_process(fasta_input)
        create_nucleotide_freq_db(passed_fasta, output_dir)

    elif mode == 'pro_feat':
        protein_input = args.protein
        output_dir = args.output

        imported_proteins = read_protein_fasta(protein_input)
        create_aminoacid_freq_db(imported_proteins, output_dir)

    elif mode == 'fetch':
        accession = args.accession_name
        email = args.email
        output_dir = args.output

        download_assembly(accession,email, output_dir)

    elif mode == 'remove_guided':
        fasta_input = args.fasta
        output_dir = args.output

        remove_guided(fasta_input, output_dir)

    else:
        print("Mode is invalid. Current supported modes are: nuc_feat, pro_feat, fetch")


if __name__ == "__main__":
    main()