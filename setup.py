from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='basiclog',
    version='0.1.3',
    packages=find_packages(),
    author="john imperial",
    description="a preconfigured logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnnyEmpires/pyeasylog",
    python_requires='>=3.6'
    )
