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

Options
-------

Options start with one or two dashes.  Many of the options an additional value
next to them.

-h, --help
    Usage help. This lists all current command line options with a short
    description.

-o, --output <file>
    Write the molecule config to <file>.  If this option is omitted, the
    config will be written to `molecule.yml`.

-s, --scenario <name>
    The molecule config scenario to be created and defined in the config file.

-t, --template <file>
    Use the jinja2 template <file> for creating the molecule config file.  If
    this option is omitted, the template is assumed to be
    `data/molecule.yml.j2`.


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
