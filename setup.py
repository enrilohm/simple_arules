from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
name = path.basename(here)

with open(path.join(here, "requirements.txt"),"r") as f:
    requirements=f.read().splitlines()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    version='0.1.0',
    description='apriori-like association rules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/enrilohm/{name}",
    author='Enrico Lohmann',
    author_email='enrilohm@gmail.com',
    python_requires='>=3.7',
    install_requires=requirements,
)
