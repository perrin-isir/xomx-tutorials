# xomx-tutorials
Tutorials for xomx ([https://github.com/perrin-isir/xomx](https://github.com/perrin-isir/xomx))

### List of colab notebooks:
- *xomx_kidney_classif*: a tutorial in two phases:  
  [xomx_kidney_classif_1.ipynb](https://colab.research.google.com/github/perrin-isir/xomx-tutorials/blob/main/tutorials/xomx_kidney_classif_1.ipynb)
(phase 1) and  
  [xomx_kidney_classif_2.ipynb](https://colab.research.google.com/github/perrin-isir/xomx-tutorials/blob/main/tutorials/xomx_kidney_classif_2.ipynb) 
(phase 2).  
Remark: the phase 1, about importation and basic preprocessing of the data, can be skipped.  
*Goal of the tutorial:*  use a 
recursive feature elimination method on RNA-seq data to identify gene 
biomarkers for the differential diagnosis of three types of kidney cancer.


- [xomx_pbmc.ipynb](https://colab.research.google.com/github/perrin-isir/xomx-tutorials/blob/main/tutorials/xomx_pbmc.ipynb)  
*Goal of the tutorial:* follow the single cell RNA-seq [Scanpy tutorial on 3k PBMCs](
https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html), except
for the computation of biomarkers for which recursive feature elimination is used.


- [xomx_tcr.ipynb](https://colab.research.google.com/github/perrin-isir/xomx-tutorials/blob/main/tutorials/xomx_tcr.ipynb)  
*Goal of the tutorial:* train an extra-trees classifier to predict whether a TCR beta-chain CDR3 sequence is associated with a given epitope.


- [xomx_hla.ipynb](https://colab.research.google.com/github/perrin-isir/xomx-tutorials/blob/main/tutorials/xomx_hla.ipynb)  
*Goal of the tutorial:* try to predict the tissue type based on HLA-presented peptides that have been found in it.

### To run tutorials as python scripts instead of notebooks:
You can run locally the `convert_notebooks_to_scripts.sh` shell script. It will convert the tutorials to python scripts and put them in the `tuto_scripts` folder:
```
bash convert_notebooks_to_scripts.sh
cd tuto_scripts
```
You can now run the tutorials with python, for instance:
```
python xomx_pbmc.py
```
You can also pass "bokeh" or "matplotlib" as an argument to the scripts to force the plots to be generated by either bokeh or matplotlib. 
For example:
```
python xomx_pbmc.py matplotlib
```
For large plots, it may be interesting to use matplotlib as it can improve responsiveness compared to the JavaScript-powered stand-alone bokeh plots. 
