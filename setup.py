from setuptools import setup, find_packages

setup(
    name='nbconvert_exporter_r',
    version='0.0.5',
    description='Custom exporter of nbconvert for R language',
    author='whatalnk',
    url='https://github.com_whatalnk/nbconvert_exporter_r',
    packages=find_packages(),
    package_data={
        '': ['templates/*.tpl'],
    },
    # Because there is no 'language_info' in metadata of IRKernel
    # not 'nbconvert.exporters' but 'nbconvert.exporters.script'
    # and the key is case sensitive
    entry_points={
        'nbconvert.exporters.script': [
            'R = nbconvert_exporter_r:RExporter'
        ],
        'nbconvert.exporters': [
            'RNotebook = nbconvert_exporter_r:RNotebookExporter'
        ],
    }
)
