# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
from illustris_elt.version import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='illustris_elt',
    version=__version__,
    description='View the Illustris galaxies with the ELT',
    long_description=readme,
    author='Kieran Leschinski',
    author_email='kieran.leschinski@univie.ac.at',
    url='https://github.com/astronomyk/illustris_elt',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    # packages=find_packages()
)

