from Bio import SeqIO

def read_protein_fasta(fasta):
    """
    Function that imports a protein fasta file into a dictionary
    """
    with open(fasta, "r") as fasta_file:
        fasta_dict = {}
        for record in SeqIO.parse(fasta_file, "fasta"):
            fasta_dict[record.id] = str(record.seq)  # Convert sequence to a string if needed
    return fasta, fasta_dict