# pylint-grandfather

[![Build Status](https://travis-ci.org/jacob-meacham/pylint-grandfather.svg?branch=develop)](https://travis-ci.org/jacob-meacham/pylint-grandfather)

# Introduction
Sometimes, you have an old project that you'd like to introduce pylint to. Usually, this is a huge feat, because the old project might have hundreds or thousands (or more!) lint issues. Fixing all of these issues might actually introduce more bugs than it solves, depending on how long the project has been running. pylint-grandfather allows you to grandfather in old code, while still enforcing that all new or changed code is pylint compliant.

# Quick Start
```
pip install pylint-grandfather
pylint my_base_dir | pylint-grandfather --base_dir my_base_dir
```

Note that this will actually touch all files, so be sure to do this with a clean working directory.

# Usage
```
usage: pylint-grandfather.py [-h] [--base-dir BASE_DIR] [--dry-run DRY_RUN]
                             infile

positional arguments:
  infile               Output from a pylint run

optional arguments:
  -h, --help           show this help message and exit
  --base-dir BASE_DIR  Base directory for pylint run
  --dry-run DRY_RUN    Output what files will be changed, but do not change
                       them
```

# Release Notes
* 1.0.0 - Initial version
