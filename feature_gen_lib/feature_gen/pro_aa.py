import os
import sys
import numpy as np

class SSP:
    def __init__(self):
        # Initialize instance variables
        self.pro = ""  # Protein sequence input
        self.fragment = ""  # Specific fragment of the sequence being analyzed
        self.index_list = []  # List of indices where 'K' appears in the sequence
        self.position = 0  # Position of the found fragment
        self.outfile = "svm_input.txt"  # File to store input for SVM processing

    def extractor(self, seqin):
        """
        Extract 'K' occurrences from the sequence and pass indices
        to fragment_extractor for further processing.
        """
        k_count = 0  # Variable to keep track of 'K' occurrences
        len_seq = len(seqin)  # Length of the protein sequence
        arr_seqin = list(seqin)  # Convert sequence into a list of characters
        
        # Count 'K' occurrences
        for i in range(len_seq):
            if arr_seqin[i] == 'K':  # If the character is 'K', increase count
                k_count += 1
        
        # Store indices where 'K' is located
        self.index_list = [i for i in range(len_seq) if arr_seqin[i] == 'K']
        
        # Call fragment_extractor with the indices of 'K'
        self.fragment_extractor(self.index_list)

    def fragment_extractor(self, idx_list):
        """
        Extract fragments from the sequence based on 'K' positions.
        Write fragments to a file, then process them for SVM input.
        """
        try:
            # Open file to write fragments
            with open("fragments.txt", 'w') as outs:
                # Extract 15 amino acid long fragments around each 'K'
                for idx in idx_list:
                    if (idx - 7) < 0:
                        frag = self.pro[0:idx + 8]  # If index is near start
                    elif (idx + 8) > len(self.pro):
                        frag = self.pro[idx - 7: len(self.pro)]  # If index is near end
                    else:
                        frag = self.pro[idx - 7: idx + 8]  # Extract middle fragment
                    outs.write(frag + "\n")  # Write fragment to file
            
            # Read the fragment file to process features
            with open("fragments.txt", 'r') as f:
                for line in f:
                    str2 = line.strip()  # Remove extra spaces
                    self.features(str2)  # Calculate features for SVM

            # Run SVM calculations and analyze the output
            self.svm_calc()
            self.output_analysis()
        
        except IOError as e:
            # Handle file I/O errors
            print(f"Error: {e}")

    def features(self, s):
        """
        Calculate amino acid frequencies and hydropathy index (GRAVY) for each fragment.
        """
        # Dictionary to count occurrences of each amino acid
        counts = {
            'arg': 0, 'his': 0, 'lys': 0, 'asp': 0, 'glu': 0,
            'asn': 0, 'cys': 0, 'gln': 0, 'gly': 0, 'ser': 0,
            'thr': 0, 'tyr': 0, 'ala': 0, 'ile': 0, 'leu': 0,
            'met': 0, 'phe': 0, 'prol': 0, 'trp': 0, 'val': 0
        }
        
        # Count the occurrences of each amino acid in the fragment
        for ch in s:
            ch = ch.lower()
            if ch in counts:
                counts[ch] += 1
        
        # Total number of amino acids
        total = sum(counts.values())
        
        # Calculate the percentage of each amino acid
        percents = {key: (value * 100) / total for key, value in counts.items()}
        
        # GRAVY (Grand Average of Hydropathy) calculation based on hydropathy index values
        gravy_weights = {
            'ala': 1.80, 'arg': -4.50, 'asn': -3.50, 'asp': -3.50, 'cys': 2.50,
            'gln': -3.50, 'glu': -3.50, 'gly': -0.40, 'his': -3.20, 'ile': 4.50,
            'leu': 3.80, 'lys': -3.90, 'met': 1.90, 'phe': 2.80, 'prol': -1.60,
            'ser': -0.80, 'thr': -0.70, 'trp': -0.90, 'tyr': -1.30, 'val': 4.20
        }
        gravy = sum(counts[aa] * gravy_weights[aa] for aa in counts) / total
        
        # Write feature set to the output file in SVM format
        try:
            with open(self.outfile, 'a') as outs:
                features = "\t".join([f"{i + 1}:{round(percents[aa] * 100) / 100.0}" 
                                      for i, aa in enumerate(counts)])
                outs.write(f"5\t{features}\t21:{round(gravy * 100) / 100.0}\n")
        
        except IOError as e:
            # Handle file I/O errors
            print(f"Error: {e}")
    
    def svm_calc(self):
        """
        Call external SVM prediction tool to classify fragments.
        """
        try:
            # Run the SVM command (this assumes an external tool 'svm-predict')
            os.system("svm-predict svm_input.txt model1 svm_output.txt")
        except Exception as e:
            # Handle system command errors
            print(f"Error: {e}")
    
    def output_analysis(self):
        """
        Analyze the output from the SVM classifier and determine if any valid site was found.
        """
        out = 0  # Variable to track SVM output status
        try:
            # Read the SVM output to check for valid classification
            with open("svm_output.txt", 'r') as f:
                for line in f:
                    if "-1" not in line:
                        out = 1  # Set flag if a site was found

            # Check if any valid site was found
            if out != 1:
                print("No Site found")
            else:
                print("Site found")
            
            # Find the corresponding fragment for the position
            with open("fragments.txt", 'r') as f:
                for line in f:
                    line = line.strip()
                    if line == self.fragment:
                        self.fragment = line
                        break
            
            # Find the position of the identified fragment
            for i, idx in enumerate(self.index_list):
                if i == out:
                    self.position = idx
            
            if not self.position:
                print("No Position found")
            else:
                print(f"Position found :: {self.position}")
        
        except IOError as e:
            # Handle file I/O errors
            print(f"Error: {e}")


# Main function to initiate the SSP class
if __name__ == "__main__":
    ssp = SSP()
    ssp.pro = input("Enter protein sequence: ").replace(" ", "").upper()  # Get protein sequence from user
    
    # Clear the contents of the output file before processing
    try:
        with open(ssp.outfile, 'w') as outs:
            outs.write("")  # Empty the file
    except IOError as e:
        # Handle file I/O errors
        print(f"Error: {e}")
    
    # Begin processing the sequence to extract fragments and analyze
    ssp.extractor(ssp.pro)
