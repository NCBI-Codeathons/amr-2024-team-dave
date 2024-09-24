import os
import sys
import numpy as np

class SSP:
    def __init__(self):
        self.pro = ""
        self.fragment = ""
        self.index_list = []
        self.position = 0
        self.outfile = "svm_input.txt"

    def extractor(self, seqin):
        k_count = 0
        len_seq = len(seqin)
        arr_seqin = list(seqin)
        
        # Count 'K' occurrences
        for i in range(len_seq):
            if arr_seqin[i] == 'K':
                k_count += 1
        
        # Store indices of 'K'
        self.index_list = [i for i in range(len_seq) if arr_seqin[i] == 'K']
        
        self.fragment_extractor(self.index_list)

    def fragment_extractor(self, idx_list):
        try:
            with open("fragments.txt", 'w') as outs:
                for idx in idx_list:
                    if (idx - 7) < 0:
                        frag = self.pro[0:idx + 8]
                    elif (idx + 8) > len(self.pro):
                        frag = self.pro[idx - 7: len(self.pro)]
                    else:
                        frag = self.pro[idx - 7: idx + 8]
                    outs.write(frag + "\n")
            
            with open("fragments.txt", 'r') as f:
                for line in f:
                    str2 = line.strip()
                    self.features(str2)
            
            self.svm_calc()
            self.output_analysis()
        
        except IOError as e:
            print(f"Error: {e}")

    def features(self, s):
        # Amino acid counts
        counts = {
            'arg': 0, 'his': 0, 'lys': 0, 'asp': 0, 'glu': 0,
            'asn': 0, 'cys': 0, 'gln': 0, 'gly': 0, 'ser': 0,
            'thr': 0, 'tyr': 0, 'ala': 0, 'ile': 0, 'leu': 0,
            'met': 0, 'phe': 0, 'prol': 0, 'trp': 0, 'val': 0
        }
        for ch in s:
            ch = ch.lower()
            if ch in counts:
                counts[ch] += 1
        
        # Total amino acids
        total = sum(counts.values())
        
        # Percent calculations
        percents = {key: (value * 100) / total for key, value in counts.items()}
        
        # Gravy calculation
        gravy_weights = {
            'ala': 1.80, 'arg': -4.50, 'asn': -3.50, 'asp': -3.50, 'cys': 2.50,
            'gln': -3.50, 'glu': -3.50, 'gly': -0.40, 'his': -3.20, 'ile': 4.50,
            'leu': 3.80, 'lys': -3.90, 'met': 1.90, 'phe': 2.80, 'prol': -1.60,
            'ser': -0.80, 'thr': -0.70, 'trp': -0.90, 'tyr': -1.30, 'val': 4.20
        }
        gravy = sum(counts[aa] * gravy_weights[aa] for aa in counts) / total
        
        try:
            with open(self.outfile, 'a') as outs:
                features = "\t".join([f"{i + 1}:{round(percents[aa] * 100) / 100.0}" 
                                      for i, aa in enumerate(counts)])
                outs.write(f"5\t{features}\t21:{round(gravy * 100) / 100.0}\n")
        
        except IOError as e:
            print(f"Error: {e}")
    
    def svm_calc(self):
        
        try:
            os.system("svm-predict svm_input.txt model1 svm_output.txt")
        except Exception as e:
            print(f"Error: {e}")
    
    def output_analysis(self):
        out = 0
        try:
            with open("svm_output.txt", 'r') as f:
                for line in f:
                    if "-1" not in line:
                        out = 1

            if out != 1:
                print("No Site found")
            else:
                print("Site found")
            
            with open("fragments.txt", 'r') as f:
                for line in f:
                    line = line.strip()
                    if line == self.fragment:
                        self.fragment = line
                        break
            
            for i, idx in enumerate(self.index_list):
                if i == out:
                    self.position = idx
            
            if not self.position:
                print("No Position found")
            else:
                print(f"Position found :: {self.position}")
        
        except IOError as e:
            print(f"Error: {e}")


# Main function
if __name__ == "__main__":
    ssp = SSP()
    ssp.pro = input("Enter protein sequence: ").replace(" ", "").upper()
    
    try:
        with open(ssp.outfile, 'w') as outs:
            outs.write("")  # Clear the file contents
    except IOError as e:
        print(f"Error: {e}")
    
    ssp.extractor(ssp.pro)

