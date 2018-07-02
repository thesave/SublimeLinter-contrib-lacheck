#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Saverio Giallorenzo
# Copyright (c) 2018 Saverio Giallorenzo
#
# License: MIT
#

from SublimeLinter.lint import Linter, util  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class Lacheck(Linter):
    cmd = 'lacheck ${file}'
    error_stream = util.STREAM_BOTH
    regex = ( 
        r'.+, line (?P<line>\d+): (?:(possible unwanted space at "{")|(?P<message>.+))' 
    )
    defaults = {
         'selector': 'text.tex.latex - meta.block.parameters.knitr - source.r.embedded.knitr',
    }
    multiline = True
    line_col_base = (1, 1)