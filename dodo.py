#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
sys.dont_write_bytecode = True

from doit.task import clean_targets
from bz.utils.format import fmt
from bz.utils.shell import call, rglob, globs, which

DOIT_CONFIG = {
    'verbosity': 2,
    'default_tasks': ['test'],
}

DODO = 'dodo.py'
PYTHON = which('python3')
REPOROOT = os.path.dirname(os.path.abspath(__file__))
BZDIR = fmt('{REPOROOT}/bz')
TESTDIR = fmt('{REPOROOT}/tests')
BINDIR = fmt('{REPOROOT}/bin')

try:
    J = call('nproc')[1].strip()
except:
    J = 1

try:
    RMRF = which('rmrf')
except:
    RMRF = 'rm -rf'

def pylint():
    '''
    run pylint
    '''
    return dict(
        name='pylint',
        actions=[
            fmt('pylint -j{J} --rcfile {TESTDIR}/pylint.rc {BZDIR}'),
        ],
    )

def pytest():
    '''
    run pytest
    '''
    return dict(
        name='pytest',
        actions=[
            fmt('{PYTHON} -m pytest -s -vv {TESTDIR}'),
        ],
    )

def pycov():
    '''
    run pycov
    '''
    return dict(
        name='pycov',
        actions=[
            fmt('pytest {PYTHON} -m pytest -s -vv --cov={BZDIR} {TESTDIR}'),
        ],
    )

def task_test():
    '''
    run: pylint, pytest, pycov
    '''
    yield pylint()
    yield pytest()
    yield pycov()

def task_rmcache():
    '''
    remove pycache files
    '''
    cachedirs = rglob('**/__pycache__')
    print('cachedirs =', cachedirs)
    return dict(
        actions=[
            fmt('{RMRF} **/__pycache__'),
        ],
    )
