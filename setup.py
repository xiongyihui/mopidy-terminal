from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-Terminal',
    version=get_version('mopidy_terminal/__init__.py'),
    url='https://github.com/xiongyihui/mopidy-terminal',
    license='Apache License, Version 2.0',
    author='Yihui Xiong',
    author_email='yihui.xiong@seeed.cc',
    description='Mopdiy extension for web terminal',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'terminado',
    ],
    entry_points={
        'mopidy.ext': [
            'terminal = mopidy_terminal:Extension',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
