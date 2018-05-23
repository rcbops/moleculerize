=============
Moleculerize
=============

Build molecule config files from an Ansible dynamic inventory file

Quick Start Guide
-----------------

1. Install ``moleculerize`` from PyPI with pip::

    $ pip install moleculerize

2. For more information on using the moleculerize launch help by::

    $ moleculerize --help

3. Here is an example of building a molecule config from an Ansible dynamic inventory file::

    $ moleculerize --output molecule/default/molecule.yml /path/to_my/dynamic_inventory.json


Release Process
---------------

See `release_process.rst`_ for information on the release process for 'moleculerize'

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _release_process.rst: docs/release_process.rst
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _qTest Manager API: https://support.qasymphony.com/hc/en-us/articles/115002958146-qTest-API-Specification