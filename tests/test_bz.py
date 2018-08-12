#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bz import Bugzilla

def test_bz():
    bz = Bugzilla()
    assert bz
