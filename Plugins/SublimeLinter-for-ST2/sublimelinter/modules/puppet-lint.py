# -*- coding: utf-8 -*-
# puppet-lint.py - sublimelint package for checking puppet files
# Requires:
# gem install puppet-lint

import re

from base_linter import BaseLinter, INPUT_METHOD_FILE

CONFIG = {
    'language': 'puppet-lint',
    'executable': 'puppet-lint',
    'lint_args': ['--no-80chars-check', '{filename}'],
    'test_existence_args': '--version',
    'input_method': INPUT_METHOD_FILE
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match(r'[Ee]rr(or)?: (?P<error>.+?(Syntax error at \'(?P<near>.+?)\'; expected \'.+\')) at /.+?:(?P<line>\d+)?', line)
            if not match:
                match = re.match(r'[Ee]rr(or)?: (?P<error>.+?(Could not match (?P<near>.+?))?) at /.+?:(?P<line>\d+)?', line)
                if not match:
                    match = re.match(r'(ERROR|WARNING): (?P<error>.+?) on line (?P<line>\d+)?$', line)

            if match:
                error, line = match.group('error'), match.group('line')
                lineno = int(line)
                try:
                    near = match.group('near')
                except IndexError:
                    near = ''

                if near:
                    error = '{0}, near "{1}"'.format(error, near)
                    self.underline_regex(view, lineno, '(?P<underline>{0})'.format(re.escape(near)), lines, errorUnderlines)

                self.add_message(lineno, lines, error, errorMessages)
