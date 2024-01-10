# ables
Useful Python Mixins
## Import package from GitHub

### 1. Create a python project
Add setup.py 
```python


```
### 2. Enable project 
```bash
python3 -m venv ./.venv
```
```bash
pip install -U pip setuptools
```
```bash
pip install -e .
```

### 2. Confirm package import

```bash

python3 -c "from able.appendable import Appendable"
python3 -c "from able.classnameable import ClassNameable"
python3 -c "from able.datable import Datable"
python3 -c "from able.failable import Failable"
python3 -c "from able.file_env import FileEnv"
python3 -c "from able.folderfileable import FolderFileable"
python3 -c "from able.inputable import Inputable"
python3 -c "from able.lb_util import Lb_Util"
python3 -c "from able.mergeable import Mergeable"
python3 -c "from able.projectable import Projectable"
python3 -c "from able.recordable import Recordable"
python3 -c "from able.resultable import Resultable"
python3 -c "from able.string_creator import CreatorString"
python3 -c "from able.string_deleter import DeleterString"
python3 -c "from able.string_updater import UpdaterString"
python3 -c "from able.taskable import Taskable"

```
## Install package
Syntax: pip install "Package" @ git+"URL of the repository"

```bash
pip install able@git+https://github.com/Wilfongjt/abilities#egg=able-0.1.0
```

see the /scripts folder