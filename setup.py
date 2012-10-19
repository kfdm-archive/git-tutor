#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Git Tutor',
    description='Simple Git Tutorials told through Scenarios',
    author='Paul Traylor',
    url='http://github.com/kfdm/git-tutor/',
    version='0.0.1',
    packages=['tutor'],
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'git-tutor = tutor.cli:main'
        ]
    }
)
