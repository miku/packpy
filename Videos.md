# Dave Forgac Share Your Code

Below are notes on each slide. 68 slides, 29 minutes.

## Beautiful Python Code

Code snippet.

## I want to share code, what do I do?

## Package

* Upload to PyPI, pip install

## Documentation

* Write docs

## Source Hosting

* Collaboration

## Tests

* Nothing breaks

## CI

* Automatic checks

## Licence

* Required.

## Contribution

* Guidelines.

## A long list of items to share code

## TL;DR (13/68)

* cookiecutter helps with setup
* new projects from templates

## Terminology

## Module

* Saved python code, stored in a file, importable.

## Import Package

* Namespace/Directory
* `__init__.py`

## Distribution Package

* bundle code
* shareable, installable
* complexity: various distribution packages

## Source Distribution

* sdist
* source code, extensions (C)
* when installed, all the extensions are compiled at install time

## Built Distribution

* wheel
* compiled beforehand, only need to be extracted at install timl
* many-linux platform tag (XXX: lookup), which is a lowest common denominator
  for Linux (will work on most modern Linux systems)

## Wheel

* Multiple types of wheels
* Universal wheel (only Python, supports 2 and 3)
* Pure Python (either 2 or 3)
* Platform (contain all compiled code for platform)

## History (21/68)

* ecosystem grew organically for a long time
* 2011 PyPA working group created, took over 4 packaging tools
* PyPUG, big improvement - python packaging user guide
* rest of the talk is about how to build a package according to that guide

## Let's make a package (22/68)

* using cookiecutter
* A few overlapping templates: https://github.com/audreyr/cookiecutter-pypackage#similar-cookiecutter-templates

```
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
You've downloaded /Users/tir/.cookiecutters/cookiecutter-pypackage before. Is it okay to delete and re-download it? [yes]:
```

Stores templates at `$HOME/.cookiecutters`.

Questions:

```
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
You've downloaded /Users/tir/.cookiecutters/cookiecutter-pypackage before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
full_name [Martin Czygan]:
email [martin.czygan@gmail.com]:
github_username [miku]:
project_name [Python Boilerplate]: ElectricSheep
project_slug [electricsheep]:
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: Example for Pycon Balkan.
pypi_username [miku]:
version [0.1.0]:
use_pytest [n]:
use_pypi_deployment_with_travis [y]:
add_pyup_badge [n]:
Select command_line_interface:
1 - Click
2 - No command-line interface
Choose from 1, 2 [1]:
create_author_file [y]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

26 files and three directories that you do not need to maintain.

```
$ tree -sh electricsheep
electricsheep
├── [ 162]  AUTHORS.rst
├── [3.5K]  CONTRIBUTING.rst
├── [  89]  HISTORY.rst
├── [1.0K]  LICENSE
├── [ 262]  MANIFEST.in
├── [2.2K]  Makefile
├── [ 893]  README.rst
├── [ 408]  docs
│   ├── [ 614]  Makefile
│   ├── [  28]  authors.rst
│   ├── [4.8K]  conf.py
│   ├── [  33]  contributing.rst
│   ├── [  28]  history.rst
│   ├── [ 310]  index.rst
│   ├── [1.1K]  installation.rst
│   ├── [ 775]  make.bat
│   ├── [  27]  readme.rst
│   └── [  81]  usage.rst
├── [ 170]  electricsheep
│   ├── [ 162]  __init__.py
│   ├── [ 431]  cli.py
│   └── [  44]  electricsheep.py
├── [ 130]  requirements_dev.txt
├── [ 397]  setup.cfg
├── [1.5K]  setup.py
├── [ 136]  tests
│   ├── [  68]  __init__.py
│   └── [ 918]  test_electricsheep.py
└── [ 289]  tox.ini

3 directories, 26 files
```

All setup.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Martin Czygan",
    author_email='martin.czygan@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Example for Pycon Balkan.",
    entry_points={
        'console_scripts': [
            'electricsheep=electricsheep.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='electricsheep',
    name='electricsheep',
    packages=find_packages(include=['electricsheep']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/miku/electricsheep',
    version='0.1.0',
    zip_safe=False,
)
```

* most important file: setup.py
* used during installation and the package index

## setup.py

* just a python file
* keep it simple

## setup.cfg

* goes along setup.py
* usually for dist options (test frameworks, extensions, etc.)

## MANIFEST.IN

* data files
* configuration
* docs

## README.rst

* long description on the PyPI

## setup.py (1/2)

```
from setuptools import setup, find_packages
```

* rest is just arguments for the setup function.
* manually, or find_packages
* `packages=find_packages(exclude=['docs', 'tests'])`
* install_requires, different from requirements.txt (vs)
* package_data (calculating the path)

## setup.py (2/2)

* entry_points define interfaces, also for plugins, console_scripts, right thing for the installation platform
* license
* classifier, not used, mostly docs

## setup.cfg (38/68)

* Example

```
[bdist_wheel]
universal = 1

[flake8]
exclude = docs
```

## MANIFEST.in

* include, exclude files

## README.rst

* Link to docs

## LICENSE

* separate license file

## Tests (42/68)

* ./test directory with stubs
* tool like tox

## Docs

* People like to expand, not create

## CI

* .travis.yml

## REQUIREMENTS.TXT

* more for the developers of a project
* tool: piptools

## ALSO COMMON (48/68)

* changelog
* history

## SERVICES 

* for supporting the project
* create repository
* continous integration
* `travis enable`

## GIT PUSH

* nice

## Read the docs

* or GH

## PYPI

* create package
* testpypi.python.org for experimentation (no junk to real index)

## Settings for pypi

* in ~/.pypirc
* password maybe

## Virtualenv

* pew
* virtualenvwrapper

## Packaging tools

* pip install wheel
* pip install twine

## Build distribution files

* ./setup.py sdist
* ./setup.py bdist_wheel
* or make dist

## Upload (62/68)

* twine

## INSTALL

* pip install example-package

## Development mode

* ./setup.py develop
* pip install -e .
* if entrypoints are changed, need to reinstall

## RINSE, REPEAT

* change code
* update version
* run tests
* CI
* build dists
* upload

## VERSIONS (66/68)

* bumpversion
* versioneer

## RECAP

* there are templates available
* use the tools
* share the code

## THANKS
