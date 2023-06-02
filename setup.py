#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requires = [
    'SQLAlchemy==2.0.9'
]

# List of dependencies installed via `pip install -e ".[test]"`
test_requires = ['pytest>=3', ]

# List of dependencies installed via `pip install -e ".[dev]"`
dev_requires = [
    'pyramid_debugtoolbar',
    'bump2version==0.5.11',
    'wheel==0.33.6',
    'watchdog==0.9.0',
    'flake8==3.7.8',
    'tox==3.14.0',
    'coverage==5.2.1',
    'Sphinx==1.8.5',
    'twine==1.14.0',
    'pytest==6.2.4',
    'black==21.7b0',
    'waitress==2.1.2',
    'pyramid==2.0.1',
    'psycopg2-binary==2.8.6',
    'pyramid-tm==2.5',
]

setup(
    author="animalizate.org",
    author_email='animalizate.org@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE v3 (AGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Proyecto animalista",
    entry_points={
        'paste.app_factory': [
            'main = app:main'
        ],
    },
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
        'test': test_requires,
    },
    license="GNU AFFERO GENERAL PUBLIC LICENSE v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='app',
    name='app',
    packages=find_packages(include=['app', 'app.*']),
    test_suite='tests',
    tests_require=test_requires,
    url='https://github.com/mricharleon/app',
    version='0.1.0',
    zip_safe=False,
)
