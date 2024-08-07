# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isyflask_core']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.20.0,<0.21.0',
 'alembic==1.7.7',
 'SQLAlchemy==1.4.36',
 'Flask==2.1.2',
 'Flask-Cors==3.0.10',
 'Flask-Migrate==3.1.0',
 'Flask-SQLAlchemy==2.5.1']

setup_kwargs = {
    'name': 'isyflask-core',
    'version': '0.1.1',
    'description': 'Librerías core de manejo de la DB del framework isy.',
    'author': 'David Cuy',
    'author_email': 'david.cuy.sanchez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DavidCuy/isyflask-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
