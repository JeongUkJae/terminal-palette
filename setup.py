from codecs import open
from setuptools import setup, find_packages

with open('terminal_palette/__init__.py', encoding='utf-8') as f:
    for line in f.readlines():
        if '__version__' in line:
            version = line.split("'")[1]

setup(
    name='terminal-palette',
    version=version,
    description="A library to color text in terminal",
    url='https://github.com/JeongUkJae/terminal-palette',
    author='Jeong Ukjae',
    author_email='jeongukjae@gmail.com',
    license='MIT',
    packages=['terminal_palette'],
    classifiers=[
        "Development Status :: 3 - Alpha", "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7", "Topic :: Utilities"
    ])
