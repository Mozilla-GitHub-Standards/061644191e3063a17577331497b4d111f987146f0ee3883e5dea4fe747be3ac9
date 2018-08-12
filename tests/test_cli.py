#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from bz.cli import main
from bz.utils.shell import call

def test_help(capfd):
    with pytest.raises(SystemExit) as pytest_wrapped_ex:
        r = main(['--help'])
    assert pytest_wrapped_ex.type == SystemExit
    assert pytest_wrapped_ex.value.code == 0
    out, err = capfd.readouterr()
    assert '-h, --help' in out
