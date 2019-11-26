from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

with open(path.join(here, 'pylfs/.version'), encoding='utf-8') as f:
	version = f.read()

setup(
	name = 'pylfs',
	version = version,
	description = "Linux from Scratch Automation in Python",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/Innovaters/lfs_automation.git',
	author = 'Kiran Kumar Kotari',
	author_email = 'kirankotari@live.com',
    entry_points={
        'console_scripts': [
            'pylfs = pylfs.pylfs:run'
        ],
    },
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Operating System :: Microsoft :: Windows',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
		],
	keywords = 'LFS automation in Python',
	packages = find_packages(exclude=['tests', 'pylfs/res/tar_files']),
	package_dir = {'pylfs': 'pylfs'},
	package_data = {'pylfs': ['res/*', '../.version']},
)