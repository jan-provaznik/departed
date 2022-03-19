#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)
#
# Let's see how poorly this goes.

import setuptools

VERSION = '0.1'
DESCRIPTION = 'Partial trace and partial transposition for Kronecker representation of multi-partite discrete variable quantum systems.'

# Yes, yes, yes!

setuptools.setup(
    name = 'impartial',
    version = VERSION,
    description = DESCRIPTION,
    author = 'Jan Provaznik',
    author_email = 'jan@provaznik.pro',
    url = 'https://provaznik.pro/impartial',
    license = 'LGPL',
    packages = [ 'impartial' ]
)

