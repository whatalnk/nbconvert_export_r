from setuptools import setup, find_packages

setup(
    name='nbconvert_export_r',
    version='0.0.1',
    description='Custom exporter of nbconvert for R language',
    author='whatalnk',
    url='https://github.com_whatalnk/nbconvert_export_r',
    packages=find_packages(),
    package_data={
        '': ['templates/*.tpl'],
    },
    entry_points={
        'nbconvert.exporters': [
            'r = nbconvert_exporter_r:RExporter'
        ],
    }
)
