from Bio import SeqIO

def read_fasta(fasta):
    """
    Function that imports a fasta file into a dictonary
    """
    with open(fasta, "r") as fasta_file:
        fasta_dict = {}
        for record in SeqIO.parse(fasta_file, "fasta"):
            fasta_dict[record.id] = record.seq
    return fasta_dict

def get_longest_record(fasta_dict):
    """
    Function that get the longest sequence from a dict of sequences
    """
    longest_seq_id = max(fasta_dict, key=lambda k: len(fasta_dict[k]))
    longest_seq = fasta_dict[longest_seq_id]
    longest_record = (longest_seq_id, longest_seq)
    return longest_record

def concat_record(fasta_dict):
    return ''.join(str(value) for value in fasta_dict.values())


def check_genome_size(sequence, genome_size, skew):
    """
    This function checks the size of the provided sequences and checks if it is within a ranges provided by skew.
    Genome_size in a float in MB.
    skew is a float representing the precentage skew
    """
    concat_rec = concat_record(fasta_dict)

    bp_genome_size = genome_size * 1000000
    minsize = bp_genome_size - (bp_genome_size * skew)
    maxsize = bp_genome_size + (bp_genome_size * skew)
    print('Checking that genome size is at least ' + str(minsize) + ' and the it is less than ' + str(maxsize))

    if ((len(concat_rec)) >= minsize) & ((len(concat_rec)) <= maxsize):
        return True
    else:
        return False


def genome_import_process(fasta, genome_size, skew):
    """
    Function that imports a fasta file into a dictonary and checks its size
    :param fasta: fasta file
    :param genome_size: estimated genome size for species
    :param skew: the percent skew of the genome size allowed
    :return: tuple of (fasta_file_name, sequence id, sequence)
    """

    fasta_dict = read_fasta(fasta)

    if check_genome_size(fasta_dict, genome_size, skew):
        print('Input sequence ' + fasta + ' passed checks')
        return fasta, fasta_dict
    else:
        print('Input sequence ' + fasta + ' did not pass checks')

