#  tests for cython-0.29.24-py38hd77b12b_0 (this is a generated file);
print('===== testing package: cython-0.29.24-py38hd77b12b_0 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import platform
is_cpython = platform.python_implementation() == 'CPython'

import Cython
import Cython.Compiler.Code
import Cython.Compiler.FlowControl
import Cython.Compiler.Lexicon
import Cython.Compiler.Parsing
import Cython.Compiler.Scanning
import Cython.Compiler.Visitor
import Cython.Plex.Actions
import Cython.Plex.Scanners

if is_cpython:
    import Cython.Runtime.refnanny

import Cython.Runtime.refnanny
import sys
import os
import subprocess
from pprint import pprint
from os.path import isfile

print('sys.executable: %r' % sys.executable)
print('sys.prefix: %r' % sys.prefix)
print('sys.version: %r' % sys.version)
print('PATH: %r' % os.environ['PATH'])
print('CWD: %r' % os.getcwd())
print('ENVIRON: %s' % os.environ)

from distutils.spawn import find_executable
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

compiler = os.environ.get('CC', 'gcc')

print('compiler determined as {}'.format(compiler))
if find_executable(compiler):
    print('found exectuable {}'.format(find_executable(compiler)))
    sys.argv[1:] = ['build_ext', '--inplace']
    setup(name='fib',
          cmdclass={'build_ext': build_ext},
          ext_modules=[Extension("fib", ["fib.pyx"])])

    try:
        import fib
        assert fib.fib(10) == 55
    except ImportError:
        cmd = [sys.executable, '-c', 'import fib; print(fib.fib(10))']
        out = subprocess.check_output(cmd)
        assert out.decode('utf-8').strip() == '55'
#  --- run_test.py (end) ---

print('===== cython-0.29.24-py38hd77b12b_0 OK =====');
print("import: 'Cython'")
import Cython

print("import: 'Cython.Build'")
import Cython.Build

print("import: 'Cython.Compiler'")
import Cython.Compiler

print("import: 'Cython.Runtime'")
import Cython.Runtime

print("import: 'Cython.Distutils'")
import Cython.Distutils

print("import: 'Cython.Debugger'")
import Cython.Debugger

print("import: 'Cython.Debugger.Tests'")
import Cython.Debugger.Tests

print("import: 'Cython.Plex'")
import Cython.Plex

print("import: 'Cython.Tests'")
import Cython.Tests

print("import: 'Cython.Build.Tests'")
import Cython.Build.Tests

print("import: 'Cython.Compiler.Tests'")
import Cython.Compiler.Tests

print("import: 'Cython.Utility'")
import Cython.Utility

print("import: 'Cython.Tempita'")
import Cython.Tempita

print("import: 'pyximport'")
import pyximport

