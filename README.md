# ables
Useful Python Mixins

### 1.1 Create a python project

```python
# main.py 
# This is github sample Python script.

__version__ = '1.15.1'
from able.mergeable import Mergeable

def main():
    template = 'Hi from <<A>>, looking at <<B>>.'
    nv_list = [{'name': '<<A>>', 'value': 'github'}, {'name': '<<B>>', 'value': 'docker'}]
    example = Mergeable().merge(template, nv_list)
    print('example',example)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

```

### 1. Add setup.py to your project 
```python
# setup.py goes in root of your application

from setuptools import setup, find_packages

# from able.__init__ import __version__
__version__='1.15.1'
setup(
    name='able',
    version=__version__,
    url='https://github.com/Wilfongjt/abilities',
    author='James Wilfong',
    author_email='wilfongjt@gmail.com',
    packages=find_packages()
)

```

### 1.3 Install package
Syntax: pip install "Package" @ git+"URL of the repository"

```bash
pip install able@git+https://github.com/Wilfongjt/abilities#egg=able-0.1.0
```

see the /scripts folder

## Templates
Setup template and template subfolders
the template folder
```
template
    + <lib-name>
        + <target-subfolder-name>
            + latest
                + "<target-file-name>.tmpl"
```

example: template/github/script/latest/git.rebase.sh.C--D.tmpl

```python

```

DataString(string, settings)
    .insert(new_line)
    .update(existing_line, new_line)
    .upsert(new_or_existing_line, upsert_line)
    .delete(existing_line)
    .replace(existing_value, new_value)

settings {'duplicates': True} 
Insert means append new-line to the end
Update means find and replace all found lines
Upsert means find and replace all found lines otherwise append new-line
Delete means find and remove all line found lines

settings {'duplicates': False}
Insert means append new-line to the end when new-line not found
Update means find and replace first found line
Upsert means find and replace first found line otherwise append new-line
Delete means find and remove single found 
