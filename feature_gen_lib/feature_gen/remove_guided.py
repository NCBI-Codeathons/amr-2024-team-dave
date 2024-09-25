
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import os

def read_fasta(fasta):
    """
    Function that imports a fasta file into a dictonary
    """
    with open(fasta, "r") as fasta_file:
        fasta_dict = {}
        for record in SeqIO.parse(fasta_file, "fasta"):
            fasta_dict[record.description] = record.seq
    return fasta, fasta_dict

def remove_guided_contigs(fasta_dict):
    filter_contigs = {}
    for seq in fasta_dict.keys():
        if '.guided' not in seq:
            filter_contigs[seq] = fasta_dict[seq]
    return filter_contigs

def write_fasta(fasta_dict, output_file):
    seq_records = []
    for description, sequence in fasta_dict.items():
        seq_record = SeqRecord(Seq(str(sequence)), id=description, description="")
        seq_records.append(seq_record)

    with open(output_file, "w") as output_handle:
        SeqIO.write(seq_records, output_handle, "fasta")

def create_dir(dir_path):
    """Create a directory if it does not exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)  # exist_ok=True avoids raising an error if the directory already exists
        print(f"Directory '{dir_path}' is created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def remove_guided_process(fasta, output_dir):

    fasta_import = read_fasta(fasta)

    basename = os.path.basename(fasta_import[0])
    file_name = '_'.join(basename.split('.')[:-1])

    new_name = file_name + '_denovo.fasta'

    filter_contigs = remove_guided_contigs(fasta_import[1])

    create_dir(output_dir)

    output_path = os.path.join(output_dir, new_name)

    write_fasta(filter_contigs,output_path)