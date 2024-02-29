from setuptools import setup, find_packages

from able import __version__
setup(
    name='able',
    version=__version__,
    url='https://github.com/Wilfongjt/abilities',
    author='James Wilfong',
    author_email='wilfongjt@gmail.com',
    data_files=[('able',['data/model.project.md.C---.tmpl'])],
    packages=find_packages()
)