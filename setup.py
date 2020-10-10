from setuptools import setup, find_packages
import pyeasylog

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name=pyeasylog.__appname__,
    version=pyeasylog.__version__,
    packages=find_packages(),
    author="john imperial",
    description="a preconfigured logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnnyEmpires/pyeasylog",
    python_requires='>=3.6'
    )
