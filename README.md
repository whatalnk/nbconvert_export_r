# nbconvert_exporter_r

Custom exporter of nbconvert for R kernel ([IRKernel](https://github.com/IRkernel/IRkernel))

## Usage: 

### R script (.R)
```
jupyter nbconvert --debug --to=script my_notebook.ipynb
```

Markdown cell and input cell number is exported as comment, like `--to=python`

### R Notebook (.Rmd)
```
jupyter nbconvert --debug --to=RNotebook my_notebook.ipynb
````

## Install

```
# git clone https://github.com/whatalnk/nbconvert_exporter_r
# cd nbconvert_exporter_r
# pip install wheel
python setup.py bdist_wheel
pip install --force-reinstall dist\nbconvert_exporter_r-x.x.x-py3-none-any.whl
```
## Post save hook
- [jupyter_notebook_config.py](https://gist.github.com/whatalnk/c8b3207267d798be713ea4a4664e2ccf) 
    - `~/.jupyter`
    - To save script and HTML whenever the notebook is saved

## See also

- [nbconvert docs: Customizing exporters](https://nbconvert.readthedocs.io/en/latest/external_exporters.html)
- [jupyter notebook docs: File save hooks](https://jupyter-notebook.readthedocs.io/en/latest/extending/savehooks.html)
