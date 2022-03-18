#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Let's see how poorly this goes.

import setuptools
import sys
import os, os.path

VERSION = '0.4.5'

# Yes, yes, yes!

setuptools.setup(
    name = 'impartial',
    version = VERSION,
    description = 'Partial trace and transposition',
    author = 'Jan Provaznik',
    author_email = 'jan@provaznik.pro',
    url = 'https://provaznik.pro/impartial',
    license = 'LGPL',
    packages = [ 'impartial' ]
)

