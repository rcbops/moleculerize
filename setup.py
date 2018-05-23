#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='moleculerize',
    version='0.0.0',
    description="Build molecule config files from an Ansible dynamic inventory file",
    long_description=readme + '\n\n' + history,
    author="rcbops",
    author_email='rpc-automation@rackspace.com',
    url='https://github.com/rcbops/molecularize',
    entry_points={
        'console_scripts': [
            'moleculerize=moleculerize.__init__:main',
        ],
    },
    packages=['moleculerize'],
    install_requires=['Click>=6.0', 'jinja2'],
    include_package_data=True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='moleculerize',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
