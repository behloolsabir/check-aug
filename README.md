# Detecting Compliance Issues 
Unsupervised way to accept or reject a sentence augmentation 

Run this to create the environment. (conda/miniconda is required)
`conda env create -f environment.yml`

Place `augmentations.json` in [raw](data/raw) folder. Run [main.ipynb](src/main.ipynb) to generate the result in [output](data/output). 

# System Design 
Refer [System Design](systemdesign.md) document to improve lexicon-based scenario that detects mentions of compliance issues. 