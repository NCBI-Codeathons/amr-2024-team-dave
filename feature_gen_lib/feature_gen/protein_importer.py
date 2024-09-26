from Bio import SeqIO

def read_protein_fasta(fasta):
    """
    Function that imports a protein FASTA file into a dictionary.
    
    Parameters:
    fasta (str): Path to the FASTA file containing protein sequences.

    Returns:
    dict: A dictionary where keys are sequence IDs (headers) and values are 
          the corresponding protein sequences as strings.
    """
    with open(fasta, "r") as fasta_file:
        fasta_dict = {}  # Initialize an empty dictionary to store the sequences
        # Parse the FASTA file and populate the dictionary with ID and sequence pairs
        for record in SeqIO.parse(fasta_file, "fasta"):
            fasta_dict[record.id] = str(record.seq)  # Convert sequence to a string if needed
    return fasta, fasta_dict
