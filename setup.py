
from setuptools import setup, find_packages

setup(
    name='specbook',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'specbook = specbook.cli:cli',
        ],
    },
)
