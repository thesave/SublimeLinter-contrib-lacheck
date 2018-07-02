#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Saverio Giallorenzo
# Copyright (c) 2018 Saverio Giallorenzo
#
# License: MIT
#

from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class Lacheck(Linter):

    syntax = ('latex', 'latexing', 
        'latex (knitr)', 'knitr-rnw', 
        'latex beamer', 'latexing beamer')
    cmd = 'lacheck @'
    error_stream = util.STREAM_BOTH
    regex = r'.+, line (?P<line>\d+): (?:(possible unwanted space at "{")|(?P<message>.+))'
    # multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
