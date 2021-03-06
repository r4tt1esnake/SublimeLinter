# flake8: noqa
"""This module exports the linter classes and the highlight, linter, persist and util submodules."""

from . import (
    linter,
    persist,
    util,
)

from .const import WARNING, ERROR

from .linter import Linter
from .base_linter.python_linter import PythonLinter
from .base_linter.ruby_linter import RubyLinter
from .base_linter.node_linter import NodeLinter
from .base_linter.composer_linter import ComposerLinter


# For compatibility with SL3, export a pseudo highlight class
class highlight:
    WARNING=WARNING
    ERROR=ERROR
