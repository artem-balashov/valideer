#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="valideer",
    version="0.4.2",
    description="Lightweight data validation and adaptation library for Python",
    long_description=open("README.rst").read(),
    url="https://github.com/artem-balashov/valideer",
    author="Artem Balashov",
    author_email="artem.balashov@inivtae.com",
    packages=find_packages(),
    install_requires=["decorator>=5.0.5"],
    test_suite="valideer.tests",
    platforms=["any"],
    keywords="validation adaptation typechecking jsonschema",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
