# 2021 - 2023 Jan Provaznik (jan@provaznik.pro)
#
# Partial trace and transpose operations
# for matrices with a structure induced by the Kronecker product.

import setuptools

VERSION = '0.3.1'
DESCRIPTION = 'Partial trace and partial transpose for matrices with Kronecker product structure.'

with open('./README', encoding = 'utf-8') as file:
    README = file.read()

# Yes, yes, yes!

setuptools.setup(
    name = 'departed',
    version = VERSION,
    description = DESCRIPTION,
    long_description = README,
    long_description_content_type = 'text/plain',
    author = 'Jan Provaznik',
    author_email = 'jan@provaznik.pro',
    url = 'https://provaznik.pro/departed',
    license = 'LGPL',

    packages = [ 'departed' ]
)

