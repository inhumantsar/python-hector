#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as reqs_file:
    requirements = reqs_file.readlines()

with open('requirements_dev.txt') as devreqs_file:
    devreqs = devreqs_file.readlines()
    if '-r requirements.txt' in devreqs:
        devreqs.remove('-r requirements.txt')
        devreqs.append(*requirements)
    test_requirements = setup_requirements = devreqs

setup(
    author="Shaun Martin",
    author_email='shaun@samsite.ca',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Simple bot which watches for stale merge requests and nags people about them",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hector',
    name='hector',
    packages=find_packages(include=['hector']),
    setup_requires=setup_requirements,
    test_suite='test',
    tests_require=test_requirements,
    url='https://github.com/inhumantsar/hector',
    version='0.1.0',
    zip_safe=False,
)
