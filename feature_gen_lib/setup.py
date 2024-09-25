from setuptools import setup, find_packages

setup(
    name='feature_Generation_lib',               # Name of your tool
    version='0.1',                # Version of your tool
    description='A tool for extraction features from genomic seuqences',  # Brief description
    authors='Edward Bird',                 # Replace with your name
    author_email='edwardbirdlab@gmail.com',  # Your email
    url='https://github.com/NCBI-Codeathons/amr-2024-team-dave',  # Project URL
    packages=find_packages(),     # Automatically find and include your packages
    entry_points={                # Create a CLI command
        'console_scripts': [
            'feature-gen = feature_gen_lib.main:main',  # 'my-tool' is the command; main function in main.py
        ],
    },
    install_requires={  # Optional: List of dependencies eg:Panda,sklit,Biopython
    },
)