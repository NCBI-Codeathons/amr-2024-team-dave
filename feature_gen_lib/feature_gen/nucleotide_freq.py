from itertools import product  # Import product function to generate all possible combinations of nucleotides
import pandas as pd  # Import pandas for data manipulation
import os  # Import os for interacting with the operating system (e.g., file paths and directories)

def space_seperated_record(fasta_dict):
    """
    Concatenates sequences from the dictionary into a single string, 
    where sequences are separated by spaces.
    
    :param fasta_dict: A dictionary of sequences.
    :return: A single space-separated string of all sequences.
    """
    return ' '.join(str(value) for value in fasta_dict.values())  # Join sequences with space separation

def concat_record(fasta_dict):
    """
    Concatenates all sequences from the dictionary into a continuous string.
    
    :param fasta_dict: A dictionary of sequences.
    :return: A single concatenated string of all sequences.
    """
    return ''.join(str(value) for value in fasta_dict.values())  # Join sequences with no separation

def count_nucleotides(input_seq):
    """
    Counts the occurrences of each nucleotide (A, C, G, T) in a given sequence.
    
    :param input_seq: Input DNA sequence (as a string).
    :return: A dictionary with nucleotide counts.
    """
    sequence = input_seq.upper()  # Convert sequence to uppercase to ensure uniformity
    nucleotides = ['A', 'C', 'G', 'T']  # List of possible nucleotides
    nucleotide_counts = {}

    # Count each nucleotide in the sequence
    for nucleotide in nucleotides:
        nucleotide_counts[nucleotide] = sequence.count(nucleotide)

    return nucleotide_counts  # Return the dictionary of nucleotide counts

def get_gc_content(fasta_dict):
    """
    Calculates the GC content (percentage of G and C nucleotides) in the combined sequences.
    
    :param fasta_dict: A dictionary of sequences.
    :return: A dictionary containing the GC content.
    """
    single_record = concat_record(fasta_dict)  # Concatenate all sequences into one
    total_len = len(single_record)  # Get the total length of the sequence
    g_content = single_record.upper().count('G') / total_len  # Calculate the proportion of G nucleotides
    c_content = single_record.upper().count('C') / total_len  # Calculate the proportion of C nucleotides

    gc_content = {}
    gc_content['GC_Content'] = (g_content + c_content) / total_len  # Combine G and C content

    return gc_content  # Return the GC content as a dictionary

def generate_combinations(nucleotides, X):
    """
    Generates all possible combinations of nucleotides of length X.
    
    :param nucleotides: List of nucleotide bases ['A', 'C', 'G', 'T'].
    :param X: Length of the combinations (e.g., 2 for dinucleotides).
    :return: A list of nucleotide combinations.
    """
    return [''.join(seq) for seq in product(nucleotides, repeat=X)]  # Generate and return combinations

def count_dinucleotides(input_seq):
    """
    Counts the occurrences of all possible dinucleotide combinations (e.g., AA, AC, etc.).
    
    :param input_seq: Input DNA sequence (as a string).
    :return: A dictionary with dinucleotide counts.
    """
    di_nuc = generate_combinations(['A', 'C', 'G', 'T'], 2)  # Generate all dinucleotide combinations
    sequence = input_seq.upper()  # Convert the sequence to uppercase
    dinucleotide_counts = {}

    # Count each dinucleotide in the sequence
    for pair in di_nuc:
        dinucleotide_counts[pair] = sequence.count(pair)

    return dinucleotide_counts  # Return the dictionary of dinucleotide counts

def count_trinucleotides(input_seq):
    """
    Counts the occurrences of all possible trinucleotide combinations (e.g., AAA, AAC, etc.).
    
    :param input_seq: Input DNA sequence (as a string).
    :return: A dictionary with trinucleotide counts.
    """
    tri_nuc = generate_combinations(['A', 'C', 'G', 'T'], 3)  # Generate all trinucleotide combinations
    sequence = input_seq.upper()  # Convert the sequence to uppercase
    trinucleotide_counts = {}

    # Count each trinucleotide in the sequence
    for pair in tri_nuc:
        trinucleotide_counts[pair] = sequence.count(pair)

    return trinucleotide_counts  # Return the dictionary of trinucleotide counts

def merge_dicts(dict1, dict2, dict3, dict4, dict5):
    merged_dict = {**dict1, **dict2, **dict3, **dict4, **dict5}
    return merged_dict

def create_dir(dir_path):
    """
    Creates a directory if it does not already exist.
    
    :param dir_path: Path to the directory.
    """
    try:
        os.makedirs(dir_path, exist_ok=True)  # Create the directory if it doesn't exist
        print(f"Directory '{dir_path}' is created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")  # Print error message if directory creation fails

def create_db(sample_id, import_sequnce, output_folder):
    input_file = import_sequnce[0]
    seq_dict = import_sequnce[1]
    space_seq = space_seperated_record(seq_dict)

    input_data = {}
    input_data['sample_id'] = sample_id

    # Calculate GC content and nucleotide frequencies
    gc_content = get_gc_content(input_data)
    nuc_counts = count_nucleotides(space_seq)
    dinuc_counts = count_dinucleotides(space_seq)
    trinuc_counts = count_trinucleotides(space_seq)

    data = merge_dicts(input_data, gc_content, nuc_counts, dinuc_counts, trinuc_counts)

    # Create a DataFrame with the merged data
    nuc_freq_df = pd.DataFrame(data, index=[0])

    # Define the output file name based on the input file name
    file_prefix = os.path.splitext(os.path.basename(input_file))[0]
    filename = file_prefix + '.nuc_freq.csv'

    # Define the full output path
    output_path = os.path.join(output_folder, filename)

    # Create the output directory if it doesn't exist
    create_dir(output_folder)

    # Save the DataFrame as a CSV file
    nuc_freq_df.to_csv(output_path, index=False)

    return nuc_freq_df  # Return the DataFrame
