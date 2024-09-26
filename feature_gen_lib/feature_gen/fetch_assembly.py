from Bio import Entrez, SeqIO
import os
import urllib.request

def create_dir(dir_path):
    """Create a directory if it does not exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)  # exist_ok=True avoids raising an error if the directory already exists
        print(f"Directory '{dir_path}' is created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def download_assembly(accession, email, output_dir="assemblies"):

    Entrez.email = email

    try:

        create_dir(output_dir)

        # Search for the assembly using the accession number
        handle = Entrez.esearch(db="assembly", term=accession)
        record = Entrez.read(handle)
        handle.close()

        # Check if any results found
        if not record['IdList']:
            print(f"No assembly found for {accession}")
            return

        # Fetch the assembly details using the ID
        assembly_id = record['IdList'][0]
        handle = Entrez.esummary(db="assembly", id=assembly_id, report="full")
        summary = Entrez.read(handle)
        handle.close()

        # Get FTP link for downloading the assembly (fna file, genomic data)
        ftp_path = summary['DocumentSummarySet']['DocumentSummary'][0]['FtpPath_GenBank']
        if ftp_path == "":
            print(f"No FTP link found for {accession}")
            return

        # Assemble the full URL for the genomic fasta file (fna)
        file_name = os.path.basename(ftp_path) + "_genomic.fna.gz"
        ftp_link = ftp_path + "/" + file_name

        # Download the file
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, file_name)
        print(f"Downloading {file_name} ...")
        ftp_link = 'https' + ftp_link[3:]
        print(ftp_link)
        urllib.request.urlretrieve(ftp_link, output_file)
        print(f"Downloaded to {output_file}")

    except Exception as e:
        print(f"Error downloading {accession}: {e}")