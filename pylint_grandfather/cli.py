"""
CLI module, for running from the command line
"""
import argparse
import os
import sys
from typing import TextIO

from pylint_grandfather import grandfather_files, build_pylint_map


def _main(pylint_output: TextIO, base_dir: str, dry_run: bool):
    if dry_run:
        pylint_map = build_pylint_map(pylint_output)
        for filename, errors_or_warnings in pylint_map.items():
            path = os.path.join(base_dir, filename)
            print('{}: {} line(s) modified'.format(path, len(errors_or_warnings)))
    else:
        grandfather_files(pylint_output, base_dir)


def _parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-dir', help='Base directory for pylint run', required=True)
    parser.add_argument('--dry-run', help='Output what files will be changed, but do not change them',
                        action='store_true')
    parser.add_argument('infile', type=argparse.FileType('r'),
                        default=sys.stdin, nargs='?', help='Output from a pylint run')
    return parser.parse_args()

def cli():
    """
    Execute to run a CLI. Not intended to be used programmatically.
    """
    options = _parse_options()

    sys.exit(_main(options.infile, os.path.expanduser(options.base_dir), options.dry_run))
