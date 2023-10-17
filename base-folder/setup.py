from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Number guessing game in Python 3'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="Ashishneo (Florian Dedov)",
    author_email="<ashishneo66@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['random', 'math'],
    keywords=['game', 'Number', 'guessing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)