from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Remove comments and empty lines
        return [line.strip() for line in lines if line and not line.startswith("#")]
setup(
    # The name of the package (or tool) that you're distributing
    name='feature_Generation_lib', 

    # The version number of your package
    version='0.1',

    # A brief description of what your package does
    description='A tool for extraction features from genomic sequences',

    # The name of the author(s) responsible for the package
    authors='Edward Bird,Kirtan Dave',  # Replace with your name or team

    # The email of the author(s) for contact purposes
    author_email='edwardbirdlab@gmail.com,kirtandave7@gmail.com',

    # The URL of the project (e.g., GitHub repository)
    url='https://github.com/NCBI-Codeathons/amr-2024-team-dave',

    # Automatically discover all Python packages in your project
    packages=find_packages(),

    # Define command-line entry points for your package
    entry_points={                
        'console_scripts': [
            # 'feature-gen' is the command to be used in the terminal;
            # 'feature_gen_lib.main:main' specifies the location of the main function
            'feature-gen = feature_gen_lib.main:main',
        ],
    },
<<<<<<< HEAD
    install_requires=parse_requirements('requirements.txt')
)
=======

    # Dependencies required to run your package (optional)
    install_requires={  # List external libraries here, such as pandas, scikit-learn, or Biopython
    },
)
>>>>>>> main
