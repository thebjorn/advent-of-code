"""minimal setup.py for the project"""

from setuptools import setup, find_packages

setup(
    name='adventofcode',
    version='0.0.1',
    description='Advent of Code',
    author='Bjorn Pettersen',
    author_email='bp@datakortet.no',
    url='https://github.com/thebjorn/advent-of-code',
    insttall_requires=[
        'rich',
        'devtools',
        'regex',
    ],
    packages=find_packages(),
    zip_safe=False,
)
