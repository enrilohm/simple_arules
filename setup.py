from setuptools import setup, find_packages
from os import path

description="hello world pip package"

here = path.abspath(path.dirname(__file__))
name = path.basename(here)

with open(path.join(here, "requirements.txt"),"r") as f:
    requirements=f.read().splitlines()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    version='0.1.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/enrilohm/{name}",
    author='Enrico Lohmann',
    scripts=["src/scripts/pip_hello_world"],
    author_email='enrilohm@gmail.com',
    python_requires='>=3.7',
    install_requires=requirements,
)
