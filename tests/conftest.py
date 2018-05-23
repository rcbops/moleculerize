#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
import json


@pytest.fixture()
def groups():
    return {'host1': ['group1_with_hosts', 'group4_with_children'],
            'host2': ['group2_with_hosts', 'group4_with_children'],
            'host3': ['group2_with_hosts', 'group4_with_children'],
            'host4': ['group3_with_hosts', 'group4_with_children'],
            'host5': ['group3_with_hosts', 'group4_with_children'],
            'host6': []}


@pytest.fixture()
def json_inventory():
    inventory = """
    {
        "_meta": {
            "hostvars": {
                "host1": {},
                "host2": {},
                "host3": {},
                "host4": {},
                "host5": {},
                "host6": {}
            }
        },
        "group1_with_hosts": {
            "children": [],
            "hosts": [
                "host1"
            ]
        },
        "group2_with_hosts": {
            "children": [],
            "hosts": [
                "host2",
                "host3"
            ]
        },
        "group3_with_hosts": {
            "children": [],
            "hosts": [
                "host4",
                "host5"
            ]
        },
        "group4_with_children": {
            "children": [
                "group1_with_hosts",
                "group2_with_hosts",
                "group3_with_hosts"
            ],
            "hosts": []
        },
        "group5_with_no_hosts_no_children": {
            "children": [],
            "hosts": []
        }
    }
    """
    return json.loads(inventory)
