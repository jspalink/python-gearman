#!/usr/bin/env python3

from setuptools import setup

from gearman import __version__ as version

setup(
    name = 'gearman',
    version = version,
    author = 'Jonathan Spalink',
    author_email = 'jspalink@info.com',
    description = 'Gearman API - Client, worker, and admin client interfaces',
    long_description=open('README.txt').read(),
    packages = ['gearman'],
    license='Apache',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
