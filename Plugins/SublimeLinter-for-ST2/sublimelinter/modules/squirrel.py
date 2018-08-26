# -*- coding: utf-8 -*-
# squirrel.py - sublimelint package for checking squirrel files

import re

from base_linter import BaseLinter, INPUT_METHOD_TEMP_FILE

CONFIG = {
    'language': 'Squirrel',
    'executable': 'sq',
    'lint_args': ['-c', '-o', '{filename}', '{filename}'],
    'input_method': INPUT_METHOD_TEMP_FILE
}


class Linter(BaseLinter):

    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        print errors
        for line in errors.splitlines():
            match = re.match(r'^.*\sline\s=\s\((?P<line>\d+)\)\scolumn\s=\s\(\d+\)\s:\s(?P<error>.+)', line)

            if match:
                error, line = match.group('error'), match.group('line')
                self.add_message(int(line), lines, error, errorMessages)
