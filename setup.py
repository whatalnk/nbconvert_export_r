setup(
    name='nbconvert_export_r',
    version='0.0.1',
    description='Custom exporter of nbconvert for R language',
    author='whatalnk',
    url='https://github.com_whatalnk/nbconvert_export_r',
    packages=find_packages(),
    entry_points={
        'nbconvert.exporters': [
            'r = nbconvert_exporter_r:RExporter'
        ],
    }
)
