#!/bin/bash
jupyter nbconvert --no-prompt --to script --output-dir='./tuto_scripts/' tutorials/*.ipynb
sed -i 's/get_ipython().system(/os.system(f/g' tuto_scripts/*.py
