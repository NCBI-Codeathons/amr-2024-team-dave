from itertools import product
from Bio import SeqUtils
import pandas as pd
import os

def space_seperated_record(fasta_dict):
    return ' '.join(str(value) for value in fasta_dict.values())

def generate_combinations(nucleotides, X):
    return [''.join(seq) for seq in product(nucleotides, repeat=X)]

def get_aminoacids():
    aa_list = []
    for aa in SeqUtils.IUPACData.protein_letters:
        aa_list.append(aa)
    return aa_list


def count_aminoacids(fasta_dict):
    seq = space_seperated_record(fasta_dict)

    sequence = seq.upper()

    aa_list = get_aminoacids()

    aa_counts = {}

    for aa in aa_list:
        aa_counts[aa] = sequence.count(aa)

    return aa_counts


def count_diaminoacids(fasta_dict):
    seq = space_seperated_record(fasta_dict)

    sequence = seq.upper()

    aa_list = get_aminoacids()

    di_aas = generate_combinations(aa_list, 2)

    di_aa_counts = {}

    for di_aa in di_aas:
        di_aa_counts[di_aa] = sequence.count(di_aa)

    return di_aa_counts


def count_triaminoacids(fasta_dict):
    seq = space_seperated_record(fasta_dict)

    sequence = seq.upper()

    aa_list = get_aminoacids()

    tri_aas = generate_combinations(aa_list, 3)

    tri_aa_counts = {}

    for tri_aa in tri_aas:
        tri_aa_counts[tri_aa] = sequence.count(tri_aa)

    return tri_aa_counts

def create_dir(dir_path):
    """Create a directory if it does not exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)  # exist_ok=True avoids raising an error if the directory already exists
        print(f"Directory '{dir_path}' is created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def merge_dicts(dict1, dict2, dict3, dict4):
    merged_dict = {**dict1, **dict2, **dict3, **dict4}
    return merged_dict

def create_db(sample_id, protein_import, output_folder):
    input_file = protein_import[0]
    seq_dict = protein_import[1]

    input_data = {}
    input_data['sample_id'] = sample_id
    aa_counts = count_aminoacids(seq_dict)
    di_aa_counts = count_diaminoacids(seq_dict)
    tri_aa_counts = count_triaminoacids(seq_dict)

    data = merge_dicts(input_data, aa_counts, di_aa_counts, tri_aa_counts)

    aa_freq_df = pd.DataFrame(data, index=[0])

    file_prefix = os.path.splitext(os.path.basename(input_file))[0]

    filename = file_prefix + '.aa_freq.csv'

    output_path = os.path.join(output_folder, filename)

    create_dir(output_folder)

    aa_freq_df.to_csv(output_path, index=False)

    return aa_freq_df