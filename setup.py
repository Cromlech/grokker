# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


install_requires = [
    'setuptools',
    'venusian'
]

tests_require = [
    'pytest >= 2.0',
]


setup(
    name='grokker',
    version = '0.2.dev0',
    description="A reformulation of Martian based on Venusian.",
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    license="BSD",
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    extras_require = dict(
        test=tests_require,
    ),
)
