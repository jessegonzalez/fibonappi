#!/usr/bin/env python

from setuptools import setup, find_packages
from fibonappi import VERSION

setup(name='fibonappi',
      version=VERSION,
      author='Jesse Gonzalez',
      author_email='jesse.gonzalez.jr@gmail.com',
      url='https://github.com/jessegonzalez/fibonappi',
      package=find_packages(),
      test_suite="fibonappi_test",
      )
