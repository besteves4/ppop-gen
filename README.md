# PPOP policies generator

## Requirements
(recommended to use `pyenv`)

1. Python3
2. dash (python-lib)
3. rdflib (python-lib)

## Usage

1. From base folder of this repo, execute `python main.py`.
2. Fill in the details regarding the data controller and the respective processing activities to be described in the PPOP privacy policy
3. A file containing the generated `odrl:Privacy` policy will be stored at `./policy.ttl`
4. Simultaneously the generated machine-readable (and also a human-readable) policy will be displayed in the UI
