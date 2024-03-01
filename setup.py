from setuptools import setup, find_packages

from able import __version__
# https://kiwidamien.github.io/making-a-python-package-vi-including-data-files.html
setup(
    name='able',
    version=__version__,
    url='https://github.com/Wilfongjt/abilities',
    author='James Wilfong',
    author_email='wilfongjt@gmail.com',
    include_package_data=True,
    package_data={'able': ['template/*/*/*/*']},
    packages=['able']
)

'''
setup(
    name='able',
    version=__version__,
    url='https://github.com/Wilfongjt/abilities',
    author='James Wilfong',
    author_email='wilfongjt@gmail.com',
    include_package_data=True,
    package_data={'': ['template/api/model.project.md.C---.tmpl']},
    packages=['able']
)
'''