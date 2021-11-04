# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""The pluginfo action plugin
"""

from __future__ import absolute_import, division, print_function

# pylint: disable=invalid-name
__metaclass__ = type
# pylint: enable=invalid-name

from importlib import import_module

from typing import Dict

import yaml
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display


# pylint: disable=import-error
from ansible_collections.ansible.introspect.plugins.modules.pluginfo import (
    DOCUMENTATION,
)
from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
    AnsibleArgSpecValidator,
)

# pylint: enable=import-error

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader  # type: ignore # noqa: F401

display = Display()


class ActionModule(ActionBase):
    """action module"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._result: Dict
        self._action: str
        self._name: str

    def _check_argspec(self, documentation):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=documentation,
            schema_format="doc",
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            self._result.update({"failed": True, "msg": " ".join(errors)})

    def _get_spec(self):
        ref = dict(zip(["corg", "cname", "plugin"], self._name.split(".")))
        pylib = "ansible_collections.{corg}.{cname}.plugins.modules.{plugin}".format(
            **ref
        )
        try:
            doc = getattr(import_module(pylib), "DOCUMENTATION")
        except AttributeError as _exc:
            self._result["failed"] = True
            self._result[
                "msg"
            ] = f"Documentation string unavailable for '{self._name}'"
            return {}
        except ModuleNotFoundError as exc:
            self._result["failed"] = True
            self._result["msg"] = f"Plugin '{self._name}' could not be found"
            return {}
        try:
            return yaml.load(doc, Loader=SafeLoader)
        except Exception as exc:
            self._result["failed"] = True
            self._result[
                "msg"
            ] = f"Failed to parse doc string for '{self._name}'"
            return {}

    def _set_vars(self):
        self._action = self._task.args.get("action")
        self._name = self._task.args.get("name")

    def run(self, tmp=None, task_vars=None):
        # pylint: disable=W0212
        self._result = super().run(tmp, task_vars)
        self._set_vars()
        self._check_argspec(DOCUMENTATION)
        if self._result.get("failed"):
            return self._result
        doc = self._get_spec()
        if self._result.get("failed"):
            return self._result
        deprecated = doc.get("deprecated")

        self._result.update(
            {
                "changed": False,
                "deprecation": {
                    "details": deprecated,
                    "deprecated": bool(deprecated),
                },
            }
        )

        if deprecated:
            msg = f"{self._name} is deprecated"
            if self._action == "warn":
                display.warning(msg)
            if self._action == "fail":
                self._result.update({"failed": True, "msg": msg})

        return self._result
