#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import json
import yaml
import moleculerize
import pytest
from os import getenv
from click.testing import CliRunner


# ======================================================================================================================
# Globals
# ======================================================================================================================
SKIP_EVERYTHING = False if getenv('SKIP_EVERYTHING') is None else True


# ======================================================================================================================
# Test Suites
# ======================================================================================================================
class TestMoleculerize(object):
    """Tests for moleculerize"""

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_load_parse_json_inventory(self, groups, json_inventory):
        """Verify that moleculerize can successfully load a JSON Ansible inventory file."""

        # Setup
        hosts_inventory = moleculerize.generate_hosts_inventory(json_inventory)

        # Test
        for host in groups.keys():
            assert hosts_inventory[host] == set(groups[host])

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_render_template(self, groups, json_inventory):
        """Verify that moleculerize can create a YAML template with correct syntax."""

        # Setup
        hosts_inventory = moleculerize.generate_hosts_inventory(json_inventory)
        render_yaml = yaml.load(moleculerize.render_molecule_template(hosts_inventory, moleculerize.TEMPLATE))

        # Expectations
        platforms_exp = [{'name': host, 'groups': groups[host]} for host in groups.keys() if host != 'host6']
        platforms_exp.append({'name': 'host6'})

        observed = render_yaml['platforms']

        # Test
        for platform in platforms_exp:
            assert platform in observed

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_missing_required_keys(self):
        """Verify that moleculerize will reject JSON Ansible inventory files missing required keys."""

        # Setup
        json_inventory_missing_meta = json.loads('{ "invalid": {} }')
        json_inventory_missing_hostvars = json.loads('{ "_meta": { "invalid": {} } }')

        # Test
        with pytest.raises(RuntimeError):
            moleculerize.generate_hosts_inventory(json_inventory_missing_meta)

        with pytest.raises(RuntimeError):
            moleculerize.generate_hosts_inventory(json_inventory_missing_hostvars)

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_invalid_template_path(self, json_inventory):
        """Verify that moleculerize will fail gracefully if the template file cannot be found."""

        # Setup
        hosts_inventory = moleculerize.generate_hosts_inventory(json_inventory)

        # Test
        with pytest.raises(RuntimeError):
            moleculerize.render_molecule_template(hosts_inventory, 'MISSING_TEMPLATE')

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_invalid_inventory_path(self):
        """Verify that moleculerize will fail gracefully if the inventory file cannot be found."""

        # Test
        with pytest.raises(RuntimeError):
            moleculerize._load_input_file('invalid_path')

    @pytest.mark.skipif(SKIP_EVERYTHING, reason='Skip if we are creating/modifying tests!')
    def test_invalid_config_path(self, mocker):
        """Verify that moleculerize will fail gracefully if the Molecule config file cannot be written."""

        runner = CliRunner()
        cli_arguments = ['/path/does/not/exist']

        mocker.patch('moleculerize._load_input_file', return_value=None)
        mocker.patch('moleculerize._load_input_file', return_value={})
        mocker.patch('moleculerize.generate_hosts_inventory', return_value={})

        # Expectations
        exit_code_exp = 2

        # Test
        result = runner.invoke(moleculerize.main, args=cli_arguments)

        assert exit_code_exp == result.exit_code
