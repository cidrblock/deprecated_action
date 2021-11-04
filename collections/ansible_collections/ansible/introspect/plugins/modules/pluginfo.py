#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# pylint: disable=missing-module-docstring

from __future__ import absolute_import, division, print_function

# pylint: disable=invalid-name
__metaclass__ = type
# pylint: enable=invalid-name

DOCUMENTATION = """
---
module: pluginfo
author: Bradley Thornton (@cidrblock)
short_description: Determine if a module is dead
version_added: "1.0.0"
description:
  - Determine if a module is dead
options:
  action:
    description: the action to take when a plugin is found to be deprecated
    type: str
    choices:
    - ignore
    - warn
    - fail
    default: warn
  name:
    description:
    - The fully qualified module name
    type: str
"""

EXAMPLES = r"""
---
"""

RETURN = """
---
"""
