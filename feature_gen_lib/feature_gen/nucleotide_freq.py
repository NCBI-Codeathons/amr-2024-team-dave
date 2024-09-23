from itertools import product
import pandas as pd
import os

def space_seperated_record(fasta_dict):
    return ' '.join(str(value) for value in fasta_dict.values())


def count_nucleotides(input_seq):
    sequence = input_seq.upper()

    nucleotides = ['A', 'C', 'G', 'T']

    nucleotide_counts = {}

    for nucleotide in nucleotides:
        nucleotide_counts[nucleotide] = sequence.count(nucleotide)

    return nucleotide_counts

def generate_combinations(nucleotides, X):
    return [''.join(seq) for seq in product(nucleotides, repeat=X)]


def count_dinucleotides(input_seq):
    di_nuc = generate_combinations(['A', 'C', 'G', 'T'], 2)

    sequence = input_seq.upper()

    dinucleotide_counts = {}

    for pair in di_nuc:
        dinucleotide_counts[pair] = sequence.count(pair)

    return dinucleotide_counts


def count_trinucleotides(input_seq):
    tri_nuc = generate_combinations(['A', 'C', 'G', 'T'], 3)

    sequence = input_seq.upper()

    trinucleotide_counts = {}

    for pair in tri_nuc:
        trinucleotide_counts[pair] = sequence.count(pair)

    return trinucleotide_counts

def merge_dicts(dict1, dict2, dict3, dict4):
    merged_dict = {**dict1, **dict2, **dict3, **dict4}
    return merged_dict

def create_directory(dir_path):
    """Create a directory if it does not exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)  # exist_ok=True avoids raising an error if the directory already exists
        print(f"Directory '{dir_path}' is created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def create_db(import_sequnce, output_folder):
    input_file = import_sequnce[0]
    seq_dict = import_sequnce[1]
    space_seq = space_seperated_record(seq_dict)

    input_data = {}
    input_data['file'] = import_sequnce[0]

    nuc_counts = count_nucleotides(space_seq)
    dinuc_counts = count_dinucleotides(space_seq)
    trinuc_counts = count_trinucleotides(space_seq)

    data = merge_dicts(input_data, nuc_counts, dinuc_counts, trinuc_counts)

    nuc_freq_df = pd.DataFrame(data, index=[0])

    file_prefix = os.path.splitext(os.path.basename(input_file))[0]

    filename = file_prefix + '.nuc_freq.csv'

    output_path = os.path.join(output_folder, filename)

    create_dir(output_folder)

    nuc_freq_df.to_csv(output_path, index=False)

    return nuc_freq_df