from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylint-grandfather',
    version='1.0.0',
    description='Grandfather in specific pylint failures',
    long_description=long_description,
    url='https://github.com/jacob-meacham/pylint-grandfather',
    author='Jacob Meacham',
    author_email='jacob.e.meacham@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='lint pylint',
    packages=['pylint_grandfather'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pylint-grandfather=pylint_grandfather.cli:cli',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/jacob-meacham/pylint-grandfather/issues',
        'Source': 'https://github.com/jacob-meacham/pylint-grandfather/',
    },
)
