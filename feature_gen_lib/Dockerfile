################# BASE IMAGE ######################
FROM python:3.8.20

################## INSTALLATION ######################

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev && apt-get install -y wget git && apt-get clean && rm -rf /var/lib/apt/lists/*


WORKDIR /home
RUN git clone https://github.com/NCBI-Codeathons/amr-2024-team-dave.git
WORKDIR /home/amr-2024-team-dave/feature_gen_lib
# RUN conda env create -f environment.yml
# RUN echo "conda activate amr-codeathon" >> ~/.bashrc
# SHELL ["/bin/bash", "-c"]
RUN pip install ete3 biopython numpy pandas 
RUN chmod +x *.py
WORKDIR /home/amr-2024-team-dave/feature_gen_lib/feature_gen
RUN chmod +x *.py
