from os.path import abspath, dirname, join
from setuptools import setup

__version__ = '1.0.4'


def read_file(filename):
    """Get the contents of a file"""
    here = abspath(dirname(__file__))
    with open(join(here, filename), encoding='utf-8') as f:
        return f.read()


setup(name='hatchbuck',
      version=__version__,
      description='Hatchbuck.com CRM API bindings for Python',
      long_description=read_file('README.rst'),
      keywords='hatchbuck CRM API',
      url='https://github.com/vshn/python-hatchbuck',
      author='VSHN AG, Bashar Said',
      author_email='bashar.said@vshn.ch',
      # BSD 3-Clause License:
      # - http://opensource.org/licenses/BSD-3-Clause
      license='BSD',
      py_modules=["hatchbuck"],
      install_requires=[
          'requests>=2',
          'pycountry>=1',
      ])
