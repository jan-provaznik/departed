#!/usr/bin/env python3
#
# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)

import setuptools

VERSION = '0.3.0'
DESCRIPTION = 'Partial trace and partial transposition for Kronecker representation of multi-partite discrete variable quantum systems.'

with open('./README', encoding = 'utf-8') as file:
    README = file.read()

# Yes, yes, yes!

setuptools.setup(
    name = 'impartial',
    version = VERSION,
    description = DESCRIPTION,
    long_description = README,
    long_description_content_type = 'text/plain',
    author = 'Jan Provaznik',
    author_email = 'jan@provaznik.pro',
    url = 'https://provaznik.pro/impartial',
    license = 'LGPL',

    packages = [ 'impartial' ]
)

