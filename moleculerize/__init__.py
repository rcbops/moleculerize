#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import sys
import json
from jinja2 import Environment, FileSystemLoader, TemplateError
import pkg_resources
import click


# ======================================================================================================================
# Globals
# ======================================================================================================================
TEMPLATES_DIR = 'data'
TEMPLATE = 'molecule.yml.j2'
OUTPUT_FILE = 'molecule.yml'
__version__ = '1.0.0'


# ======================================================================================================================
# Functions
# ======================================================================================================================
def _load_input_file(file_path):
    """Read and validate the input file contents.

    Args:
        file_path (str): A string representing a valid file path.
    Returns:
        dict: The exit code to return to the shell.
    Raises:
        RuntimeError: invalid path.
    """

    try:
        with open(file_path, 'r') as f:
            json_inventory = json.loads(f.read())
    except IOError:
        raise RuntimeError('Invalid path "{}" for inventory file!'.format(file_path))

    return json_inventory


def generate_hosts_inventory(json_inventory):
    """Build a dictionary of hosts and associated groups from a Ansible JSON inventory file as keys.

    Args:
        json_inventory (dict): A dictionary object representing a Ansible JSON inventory file.
    Returns:
        dict(list): A dictionary of hosts with each host having a list of associated groups.
            { 'host_name': ['group1', 'group2'] }
    """

    inventory_child_groups = {}

    try:
        inventory_hosts = {k: set() for k in json_inventory['_meta']['hostvars'].keys()}
        inventory_groups = {k: v for (k, v) in json_inventory.items() if k != '_meta'}
    except KeyError:
        raise RuntimeError('Expected key(s) missing from inventory file! ("_meta", hostvars")')

    for group_name, group_info in inventory_groups.items():
        if 'children' in group_info and len(group_info['children']) > 0:
            for child in group_info['children']:
                if child in inventory_child_groups.keys():
                    inventory_child_groups[child].add(group_name)
                else:
                    inventory_child_groups[child] = {group_name}

    for group_name, group_info in inventory_groups.items():
        if 'hosts' in group_info.keys():
            for host in group_info['hosts']:
                inventory_hosts[host].add(group_name)

                if group_name in inventory_child_groups.keys():
                    inventory_hosts[host].update(inventory_child_groups[group_name])

    return inventory_hosts


def render_molecule_template(inventory_hosts, template_file):
    """Create a molecule config file from a template.

    Args:
        inventory_hosts (dict(list(str)): A dictionary of inventory hosts with each host having a list of associated
            groups.
        template_file (str): The template file to use for rendering.
    Returns:
        str: A molecule config file populated with hosts and groups.
    """

    template_path = pkg_resources.resource_filename('moleculerize', TEMPLATES_DIR)
    j2_env = Environment(loader=FileSystemLoader(template_path),
                         trim_blocks=True,
                         lstrip_blocks=True,
                         keep_trailing_newline=True
                         )

    try:
        return j2_env.get_template(template_file).render(hosts=inventory_hosts)
    except TemplateError as e:
        print(e)
        raise RuntimeError('Template "{}" not found!'.format(template_file))


# ======================================================================================================================
# Main
# ======================================================================================================================
@click.command()
@click.argument('inv_file', type=click.Path(exists=True))
@click.option('--template', '-t',
              type=click.STRING,
              default=TEMPLATE,
              help='Molecule config template file')
@click.option('--output', '-o',
              type=click.STRING,
              default=OUTPUT_FILE,
              help='Output file path for molecule config.')
def main(inv_file, template, output):
    """Build molecule config files from an Ansible dynamic inventory file

    \b
    Required Arguments:
        INV_FILE        A valid Ansible dynamic inventory file
    """

    exit_code = 0

    try:
        inventory_hosts = generate_hosts_inventory(_load_input_file(inv_file))

        try:
            with open(output, 'wb') as f:
                f.write(render_molecule_template(inventory_hosts, template))
        except IOError:
            raise RuntimeError('Cannot write "{}" Molecule configuration file!'.format(output))

        print("Inventory file: {}".format(inv_file))
        print("Template file: {0}/{1}".format(TEMPLATES_DIR, template))
        print("Output file: {}".format(output))

        print("\nSuccess!")
    except RuntimeError as e:
        exit_code = 1
        print(e)

        print("\nFailed!")

    return exit_code


if __name__ == '__main__':
    sys.exit()
