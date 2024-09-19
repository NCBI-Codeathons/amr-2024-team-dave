import glob

# Find all files starting with 'GCA_'
gca_files = glob.glob("GCA_*.tsv")

# Create output file names based on input file names
output_files = [
    (f.replace(".tsv", "_gene.txt"), f.replace(".tsv", "_ec_number.txt")) 
    for f in gca_files
]

rule all:
    input:
        [out for pair in output_files for out in pair]

rule extract_columns:
    input:
        csv_file="{filename}.tsv"
    output:
        gene_file="{filename}_gene.txt",
        ec_number_file="{filename}_ec_number.txt"
    shell:
        """
        awk -F'\t' 'NR > 1 {{print $4}}' {input.tsv_file} > {output.gene_file}
        awk -F'\t' 'NR > 1 {{print $5}}' {input.tsv_file} > {output.ec_number_file}
        """
