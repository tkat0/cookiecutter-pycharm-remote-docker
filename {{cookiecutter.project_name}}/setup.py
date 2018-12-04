from setuptools import setup

requirements = open('requirements.txt').read().splitlines()

setup(install_requires=requirements)