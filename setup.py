import os
from setuptools import setup, find_packages


def read(fname):
    """
    Utility function to read the README file.

    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="spfileops",
    version="0.1",
    author="Sam Perry",
    author_email="u1265119@unimail.hud.ac.uk",
    description=("A collection of useful file operation tools, written by Sam "
                 "Perry"),
    license="GPL",
    keywords="pathops fileops file operations",
    url="https://github.com/Pezz89/fileops",
    packages=find_packages(),
    install_requires=read('requirements.txt'),
)
