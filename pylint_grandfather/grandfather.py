"""
Main code
"""
import os
import re
from collections import defaultdict
from typing import Iterable, TextIO


def build_pylint_map(lines: Iterable[str]):
    """
    Generates a map of file name to a list of tuples of (line number, error type)
    :param lines: Iterable of lines from the pylint output
    :return: Map of files to (line number, error type)
    """
    line_regex = re.compile(r'^(.*?):(\d+):\s*\[[\w\d]+\(([\w-]+)\),\s+')
    all_matches = [line_regex.match(line) for line in lines]
    matches = [match for match in all_matches if match is not None]

    result = defaultdict(list)
    for match in matches:
        result[match.group(1)].append((int(match.group(2)), match.group(3)))

    return result


def grandfather_files(pylint_output: TextIO, base_dir: str):
    """
    Given the pylint output and the base directory of the run, this will touch all files and write to them
    """
    pylint_map = build_pylint_map(pylint_output)

    for filename, errors_or_warnings in pylint_map.items():
        path = os.path.join(base_dir, filename)
        with open(path, 'r') as f:
            lines = f.readlines()

        # TODO: Handle multiple errors in the same line, instead of ignoring subsequent errors. We can group
        # The pylint map to keep all errors for a particular warning together. This should still map by filename
        # so that we're efficient with our file I/O
        for (line_number, error_or_warning) in errors_or_warnings:
            if 'pylint' in lines[line_number - 1]:  # Don't do anything for lines that already have a pylint directive
                continue

            lines[line_number - 1] = lines[line_number - 1].replace('\n',
                                                                    ' # pylint: disable={}\n'.format(error_or_warning))

        with open(path, 'w') as f:
            f.writelines(lines)
