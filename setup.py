#!/usr/bin/env python
"""Imaging library"""
from setuptools import find_packages, setup
 
setup(name = 'imaginglib',
    version = '0.1',
    description = "Imaging Library",
    long_description = "For resizing, cropping, rotating and converting images",
    scripts = ['imaginglib/imaginglib.py'],
    platforms = ["Linux"],
    author="Kumari Shalini",
    author_email="shaliniroy012@gmail.com",
    url="https://shaliniroy012.wordpress.com/",
    license = "MIT",
    packages=find_packages()
)
