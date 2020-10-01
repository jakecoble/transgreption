# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['word_sandwich']
install_requires = \
['beautifulsoup4>=4.9.1,<5.0.0',
 'flask>=1.1.2,<2.0.0',
 'livereload>=2.6.3,<3.0.0',
 'python-slugify>=4.0.1,<5.0.0',
 'requests>=2.24.0,<3.0.0',
 'url-normalize>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'word-sandwich',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jake Coble',
    'author_email': 'jakecoble@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
