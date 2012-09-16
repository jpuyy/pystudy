#!/usr/bin/env python
# -- coding: utf-8 --
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My project',
	'author': 'jpuyy',
	'url': 'http://localhost/project',
	'download_url': 'http://localhost/project',
	'author_email': 'jpuyy.com@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
