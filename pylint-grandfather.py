import re
import sys
import argparse
from collections import defaultdict
from pylint_grandfather import grandfather_files, build_pylint_map
from typing import Iterable, TextIO

import os

def main(pylint_output: TextIO, base_dir: str, dry_run: bool):
    if dry_run:
        pylint_map = build_pylint_map(pylint_output)
        for filename, errors_or_warnings in pylint_map.items():
            path = os.path.join(base_dir, filename)
            print('{}: {} lines'.format(path, len(errors_or_warnings)))
    else:
        grandfather_files(pylint_output, base_dir)


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-dir', help='Base directory for pylint run')
    parser.add_argument('--dry-run', help='Output what files will be changed, but do not change them')
    parser.add_argument('infile', type=argparse.FileType('r'),
                        default=sys.stdin)
    return parser.parse_args()


if __name__ == '__main__':
    options = parse_options()

    sys.exit(main(options.infile, os.path.expanduser(options.base_dir)))
