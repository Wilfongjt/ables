from setuptools import setup, find_packages

from able.__init__ import __version__
setup(
    name='able',
    version=__version__,
    url='https://github.com/Wilfongjt/abilities',
    author='James Wilfong',
    author_email='wilfongjt@gmail.com',
    packages=find_packages()
)