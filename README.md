```yaml
- hosts: localhost
  gather_facts: false
  tasks:
  - ansible.introspect.pluginfo:
      name: ansible.netcommon.cli_config
  - ansible.introspect.pluginfo:
      action: warn
      name: ansible.netcommon.net_vlan
  - ansible.introspect.pluginfo:
      name: community.general.cloud.linode.linode
  - ansible.introspect.pluginfo:
      action: fail
      name: ansible.netcommon.net_user
```

```

PLAYBOOK: site.yaml *************************************************************************************************************************************************
1 plays in site.yaml

PLAY [localhost] ****************************************************************************************************************************************************
META: ran handlers

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
task path: /home/bthornto/github/get_doc/site.yaml:4
ok: [localhost] => {
    "changed": false,
    "deprecation": {
        "deprecated": false,
        "details": null
    }
}

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
task path: /home/bthornto/github/get_doc/site.yaml:6
[WARNING]: ansible.netcommon.net_vlan is deprecated
ok: [localhost] => {
    "changed": false,
    "deprecation": {
        "deprecated": true,
        "details": {
            "alternative": "Use platform-specific \"[netos]_vlans\" module",
            "removed_at_date": "2022-06-01",
            "why": "Updated modules released with more functionality"
        }
    }
}

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
task path: /home/bthornto/github/get_doc/site.yaml:9
ok: [localhost] => {
    "changed": false,
    "deprecation": {
        "deprecated": false,
        "details": null
    }
}

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
task path: /home/bthornto/github/get_doc/site.yaml:11
fatal: [localhost]: FAILED! => {
    "changed": false,
    "deprecation": {
        "deprecated": true,
        "details": {
            "alternative": "Use platform-specific \"[netos]_user\" module",
            "removed_at_date": "2022-06-01",
            "why": "Updated modules released with more functionality"
        }
    },
    "msg": "ansible.netcommon.net_user is deprecated"
}

PLAY RECAP **********************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

```