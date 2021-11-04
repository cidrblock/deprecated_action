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
      action: fail
      name: ansible.netcommon.net_user
```

```

PLAY [localhost] ****************************************************************************************************************************************************

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
ok: [localhost]

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
[WARNING]: ansible.netcommon.net_vlan is deprecated
ok: [localhost]

TASK [ansible.introspect.pluginfo] **********************************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "deprecation": {"deprecated": true, "details": {"alternative": "Use platform-specific \"[netos]_user\" module", "removed_at_date": "2022-06-01", "why": "Updated modules released with more functionality"}}, "msg": "ansible.netcommon.net_user is deprecated"}

PLAY RECAP **********************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

```