# E-GUARD

<p> 
<img align="left" src="https://github.com/NCBI-Codeathons/amr-2024-team-dave/blob/main/genome/E-guard_logo.png" width="150" height="150" alt="Project Logo"> ESKAPE pathogens represent a significant cause of drug-resistant infections in healthcare settings. They exhibit high mutation rates and demonstrate significant resistance to multiple drugs. Early prediction of resistance patterns helps clinicians choose effective antibiotics, improving treatment and reducing resistance development.
</p>



## Project Goals

This project aimed to develop a machine learning model for rapid identification of ESKAPE pathogens, enhancing diagnostic capabilities and informing treatment strategies. The model will be trained on genomic and protein sequences, phenotypic and clinical data to predict phenotypic features and clinical outcomes from sample's genomic sequence. 

Keywords: ESKAPE pathogens, Machine learning, Genomic data, Phenotypic data, Clinical data, Model development, Diagnostic tool, public health



## Approach
![Workflow Image](https://github.com/NCBI-Codeathons/amr-2024-team-dave/blob/main/genome/workflow_team_dave.JPG)


## Methods
We collected isolates' accession ids and erd_groups from NCBI Isolate Browser. Based on erd_group that represents SNP cluster of each isolate, we chose isolates from all SNP clusters for each ESKAPE pathogen. Then processed our data by using PROKKA, gene annotation and Mummer, SNP-calling. We extracted some scoring features using Random Forest and Support Vector Machine (SVM) and calculated important sequence features and annotation features.
From more than 340,000 isolates of ESKAP pathogens, we totally took 23,000 covering all of the SNP clusters for our training and tst datasets.

![alt text](https://github.com/NCBI-Codeathons/amr-2024-team-dave/blob/main/Capture.PNG)

![alt text](https://github.com/NCBI-Codeathons/amr-2024-team-dave/blob/main/3.PNG)

## Results
Our pipeline extracted some features like sequence features for genomic and protein sequences, transcription fautres including coding sequences and mRNA, tRNA and rRNA contents.we will work more to connect these featres to phenotypic ones.


## Future Work
- Integrate AMR (Antimicrobial Resistance) pattern recognition using a CARD-like database.
- Enrich analysis with AMR gene data to develop comprehensive genetic resistance profiles.
- Enhance model capabilities for predicting resistance patterns.
- Expand research to include a broader range of pathogens for greater impact.
- Foster collaborations with other research teams and institutions to improve methodologies against AMR.
- Conduct more model validation using clinical samples to ensure robustness and accuracy.


## Our Team

- Kirtan Dave (Team Leader), Assistant Professor in Bioinformatics Research and development cell  Parul University 
- Narges SangaraniPour, Shahid Beheshti University of medical sciences 
- Edward Bird , Kansas State University, Interdepartmental Genetics
- Abolhassan Bahari , High Institute for Research and Education in Transfusion Medicine
- Priyal Visavadiya, Gujarat Biotechnology University, Gandhinagar
- Precious Osadebamwen, Dalhousie University, Halifax, NS

  <img width="1440" alt="Screenshot 1403-07-06 at 18 58 28" src="https://github.com/user-attachments/assets/8d7ab937-cbcd-4afe-bea7-1fa8b5c03418">


## NCBI Codeathon Disclaimer
This software was created as part of an NCBI codeathon, a hackathon-style event focused on rapid innovation. While we encourage you to explore and adapt this code, please be aware that NCBI does not provide ongoing support for it.

For general questions about NCBI software and tools, please visit: [NCBI Contact Page](https://www.ncbi.nlm.nih.gov/home/about/contact/)

