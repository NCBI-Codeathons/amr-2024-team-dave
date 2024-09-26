from Bio import SeqIO  # Importing Biopython's SeqIO module for handling sequence file formats

def read_fasta(fasta):
    """
    Reads a FASTA file and stores the sequences in a dictionary.
    
    :param fasta: Path to the input FASTA file.
    :return: A dictionary where the keys are sequence IDs and values are the sequences.
    """
    with open(fasta, "r") as fasta_file:
        fasta_dict = {}
        for record in SeqIO.parse(fasta_file, "fasta"):
            fasta_dict[record.description] = record.seq
    return fasta_dict

def remove_guided_contigs(fasta_dict):
    filter_contigs = {}
    for seq in fasta_dict.keys():
        if '.guided' not in seq:
            filter_contigs[seq.split(' ')[0]] = fasta_dict[seq]
    return filter_contigs

def get_longest_record(fasta_dict):
    """
    Finds the longest sequence in a dictionary of sequences.
    
    :param fasta_dict: A dictionary with sequence IDs as keys and sequences as values.
    :return: A tuple containing the ID of the longest sequence and the sequence itself.
    """
    # Find the sequence with the maximum length using the dictionary's values
    longest_seq_id = max(fasta_dict, key=lambda k: len(fasta_dict[k]))  # Find the key (ID) of the longest sequence
    longest_seq = fasta_dict[longest_seq_id]  # Retrieve the longest sequence
    longest_record = (longest_seq_id, longest_seq)  # Store ID and sequence in a tuple
    return longest_record  # Return the tuple with the longest sequence and its ID

def concat_record(fasta_dict):
    """
    Concatenates all sequences in the dictionary into a single string.
    
    :param fasta_dict: A dictionary where the keys are sequence IDs and values are sequences.
    :return: A concatenated string of all sequences.
    """
    # Convert each sequence to string and concatenate them
    return ''.join(str(value) for value in fasta_dict.values())  # Join all sequences into a single string

def check_genome_size(fasta_dict, genome_size, skew):
    """
    Checks whether the total size of the concatenated sequences falls within the allowed range
    defined by the genome size and skew percentage.
    
    :param fasta_dict: A dictionary of sequences.
    :param genome_size: The estimated genome size (in megabases).
    :param skew: The allowed percentage deviation (skew) from the genome size.
    :return: Boolean indicating whether the genome size check passed.
    """
    concat_rec = concat_record(fasta_dict)  # Concatenate all sequences into one

    # Convert genome size from megabases (MB) to base pairs (bp)
    bp_genome_size = genome_size * 1_000_000  # Multiply MB by 1 million to get base pairs
    minsize = bp_genome_size - (bp_genome_size * skew)  # Minimum allowed genome size based on skew
    maxsize = bp_genome_size + (bp_genome_size * skew)  # Maximum allowed genome size based on skew
    print('Checking that genome size is at least ' + str(minsize) + ' and it is less than ' + str(maxsize))

    # Check if the length of the concatenated sequence is within the allowed range
    if (minsize <= len(concat_rec) <= maxsize):
        return True  # Return True if genome size is within the range
    else:
        return False  # Return False if genome size is outside the allowed range

def genome_import_process(fasta):
    """
    Imports a FASTA file and checks whether the total genome size is within the allowable range.
    
    :param fasta: Path to the input FASTA file.
    :param genome_size: The estimated genome size (in megabases) for the species.
    :param skew: The allowed percentage deviation (skew) from the genome size.
    :return: A tuple containing the FASTA file name and the sequence dictionary if the check passes.
    """
    
    fasta_dict = read_fasta(fasta)  # Read the FASTA file and store sequences in a dictionary

<<<<<<< HEAD
    fasta_dict = read_fasta(fasta)

    filtered_contigs = remove_guided_contigs(fasta_dict)

    return fasta, filtered_contigs

=======
    # Perform genome size check
    if check_genome_size(fasta_dict, genome_size, skew):
        print('Input sequence ' + fasta + ' passed checks')  # Inform the user if the sequence passes
        return fasta, fasta_dict  # Return the FASTA file name and the sequence dictionary
    else:
        print('Input sequence ' + fasta + ' did not pass checks')  # Inform the user if the sequence fails
>>>>>>> main
