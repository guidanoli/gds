#!/usr/bin/env python
from setuptools import setup, find_packages

exec(open("pydslib/__version__.py").read())

setup(
    name='pydslib',
    version=__version__,
    author='Guilherme Dantas',
    author_email='guidanoli@hotmail.com',
    
	description='A collection of well known data structures'
				'implemented in Python.',
	long_description=open('README.rst').read(),
	url='https://github.com/guidanoli/pydslib',
    license='MIT',
	
    packages=["pydslib"],
	
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: Implementation :: CPython',
	]
)

