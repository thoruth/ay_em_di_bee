#!/usr/bin/env python

from distutils.core import setup

setup(name='magic_module',
      version='1.0',
      description='Just another interview',
      author='The one and only Viet',
      author_email='viet@letrungvietanh.com',
      packages=['magic_package'],
      tests_require=['pytest'],
      install_requires=[
         'pandas',
         'tqdm',
         'lxml',
         'cchardet'
     ]
    )