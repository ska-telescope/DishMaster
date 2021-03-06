#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the DishMaster project
#
#
#
# Distributed under the terms of the BSD-3-Clause license.
# See LICENSE.txt for more info.

import os
import sys
from setuptools import setup

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

readme_filename = os.path.join(setup_dir, 'README.rst')
with open(readme_filename) as file:
    long_description = file.read()

release_filename = os.path.join(setup_dir, 'DishMaster', 'release.py')
exec(open(release_filename).read())

pack = ['DishMaster']

setup(
      name=name,
      version=version,
      description='SKA Dish Master TANGO device server',
      packages=pack,
      include_package_data=True,
      test_suite="test",
      entry_points={'console_scripts':['DishMaster = DishMaster:main']},
      author='apurva.ska',
      author_email='apurva.ska at gmail.com',
      license='BSD-3-Clause',
      long_description=long_description,
      url='www.tango-controls.org',
      platforms="All Platforms", install_requires=['pytango', 'mock'],
      #test_suite='test',
      #install_requires=['pytango'],  # FIXME: add your package's dependencies to this list
      setup_requires=[
          # dependency for `python setup.py test`
          'pytest-runner',
          # dependencies for `python setup.py build_sphinx`
          'sphinx',
          'recommonmark'
      ],
      tests_require=[
          'pytest',
          'pytest-cov',
          'pytest-json-report',
          'pycodestyle',
      ],
      extras_require={
          'dev':  ['prospector[with_pyroma]', 'yapf', 'isort']
      }
)
