#!/usr/bin/python
from __future__ import absolute_import, division, print_function

# Copyright: (c) 2022 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

__metaclass__ = type

ANSIBLE_METADATA = {
    "status": ["preview"],
    "supported_by": "community",
    "metadata_version": "1.1",
}

DOCUMENTATION = """
---
module: fortios_system_wccp
short_description: Configure WCCP in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and wccp category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.0.0"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.14
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    member_path:
        type: str
        description:
            - Member attribute path to operate on.
            - Delimited by a slash character if there are more than one attribute.
            - Parameter marked with member_path is legitimate for doing member operation.
    member_state:
        type: str
        description:
            - Add or delete a member under specified attribute path.
            - When member_state is specified, the state option is ignored.
        choices:
            - 'present'
            - 'absent'

    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - 'present'
            - 'absent'
    system_wccp:
        description:
            - Configure WCCP.
        default: null
        type: dict
        suboptions:
            assignment_bucket_format:
                description:
                    - Assignment bucket format for the WCCP cache engine.
                type: str
                choices:
                    - 'wccp-v2'
                    - 'cisco-implementation'
            assignment_dstaddr_mask:
                description:
                    - Assignment destination address mask.
                type: str
            assignment_method:
                description:
                    - Hash key assignment preference.
                type: str
                choices:
                    - 'HASH'
                    - 'MASK'
                    - 'any'
            assignment_srcaddr_mask:
                description:
                    - Assignment source address mask.
                type: str
            assignment_weight:
                description:
                    - Assignment of hash weight/ratio for the WCCP cache engine.
                type: int
            authentication:
                description:
                    - Enable/disable MD5 authentication.
                type: str
                choices:
                    - 'enable'
                    - 'disable'
            cache_engine_method:
                description:
                    - Method used to forward traffic to the routers or to return to the cache engine.
                type: str
                choices:
                    - 'GRE'
                    - 'L2'
            cache_id:
                description:
                    - IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.
                type: str
            forward_method:
                description:
                    - Method used to forward traffic to the cache servers.
                type: str
                choices:
                    - 'GRE'
                    - 'L2'
                    - 'any'
            group_address:
                description:
                    - IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.
                type: str
            password:
                description:
                    - Password for MD5 authentication.
                type: str
            ports:
                description:
                    - Service ports.
                type: list
                elements: str
            ports_defined:
                description:
                    - Match method.
                type: str
                choices:
                    - 'source'
                    - 'destination'
            primary_hash:
                description:
                    - Hash method.
                type: list
                elements: str
                choices:
                    - 'src-ip'
                    - 'dst-ip'
                    - 'src-port'
                    - 'dst-port'
            priority:
                description:
                    - Service priority.
                type: int
            protocol:
                description:
                    - Service protocol.
                type: int
            return_method:
                description:
                    - Method used to decline a redirected packet and return it to the FortiGate unit.
                type: str
                choices:
                    - 'GRE'
                    - 'L2'
                    - 'any'
            router_id:
                description:
                    - IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.
                type: str
            router_list:
                description:
                    - IP addresses of one or more WCCP routers.
                type: list
                elements: str
            server_list:
                description:
                    - IP addresses and netmasks for up to four cache servers.
                type: list
                elements: str
            server_type:
                description:
                    - Cache server type.
                type: str
                choices:
                    - 'forward'
                    - 'proxy'
            service_id:
                description:
                    - Service ID.
                required: true
                type: str
            service_type:
                description:
                    - WCCP service type used by the cache server for logical interception and redirection of traffic.
                type: str
                choices:
                    - 'auto'
                    - 'standard'
                    - 'dynamic'
"""

EXAMPLES = """
- name: Configure WCCP.
  fortinet.fortios.fortios_system_wccp:
      vdom: "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_wccp:
          assignment_bucket_format: "wccp-v2"
          assignment_dstaddr_mask: "<your_own_value>"
          assignment_method: "HASH"
          assignment_srcaddr_mask: "<your_own_value>"
          assignment_weight: "0"
          authentication: "enable"
          cache_engine_method: "GRE"
          cache_id: "<your_own_value>"
          forward_method: "GRE"
          group_address: "<your_own_value>"
          password: "<your_own_value>"
          ports: "<your_own_value>"
          ports_defined: "source"
          primary_hash: "src-ip"
          priority: "0"
          protocol: "0"
          return_method: "GRE"
          router_id: "<your_own_value>"
          router_list: "<your_own_value>"
          server_list: "<your_own_value>"
          server_type: "forward"
          service_id: "<your_own_value>"
          service_type: "auto"
"""

RETURN = """
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    FortiOSHandler,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_legacy_fortiosapi,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    schema_to_module_spec,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_schema_versioning,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import (
    FAIL_SOCKET_MSG,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.data_post_processor import (
    remove_invalid_fields,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    is_same_comparison,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    serialize,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import (
    find_current_values,
)


def filter_system_wccp_data(json):
    option_list = [
        "assignment_bucket_format",
        "assignment_dstaddr_mask",
        "assignment_method",
        "assignment_srcaddr_mask",
        "assignment_weight",
        "authentication",
        "cache_engine_method",
        "cache_id",
        "forward_method",
        "group_address",
        "password",
        "ports",
        "ports_defined",
        "primary_hash",
        "priority",
        "protocol",
        "return_method",
        "router_id",
        "router_list",
        "server_list",
        "server_type",
        "service_id",
        "service_type",
    ]

    json = remove_invalid_fields(json)
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_single_path(data, path, index):
    if (
        not data
        or index == len(path)
        or path[index] not in data
        or not data[path[index]]
    ):
        return

    if index == len(path) - 1:
        data[path[index]] = " ".join(str(elem) for elem in data[path[index]])
    elif isinstance(data[path[index]], list):
        for value in data[path[index]]:
            flatten_single_path(value, path, index + 1)
    else:
        flatten_single_path(data[path[index]], path, index + 1)


def flatten_multilists_attributes(data):
    multilist_attrs = [
        ["server_list"],
        ["router_list"],
        ["ports"],
        ["primary_hash"],
    ]

    for attr in multilist_attrs:
        flatten_single_path(data, attr, 0)

    return data


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace("_", "-")] = underscore_to_hyphen(v)
        data = new_data

    return data


def system_wccp(data, fos, check_mode=False):
    vdom = data["vdom"]

    state = data["state"]

    system_wccp_data = data["system_wccp"]
    system_wccp_data = flatten_multilists_attributes(system_wccp_data)
    filtered_data = underscore_to_hyphen(filter_system_wccp_data(system_wccp_data))

    # check_mode starts from here
    if check_mode:
        diff = {
            "before": "",
            "after": filtered_data,
        }
        mkey = fos.get_mkey("system", "wccp", filtered_data, vdom=vdom)
        current_data = fos.get("system", "wccp", vdom=vdom, mkey=mkey)
        is_existed = (
            current_data
            and current_data.get("http_status") == 200
            and isinstance(current_data.get("results"), list)
            and len(current_data["results"]) > 0
        )

        # 2. if it exists and the state is 'present' then compare current settings with desired
        if state == "present" or state is True:
            if mkey is None:
                return False, True, filtered_data, diff

            # if mkey exists then compare each other
            # record exits and they're matched or not
            if is_existed:
                is_same = is_same_comparison(
                    serialize(current_data["results"][0]), serialize(filtered_data)
                )

                current_values = find_current_values(
                    current_data["results"][0], filtered_data
                )

                return (
                    False,
                    not is_same,
                    filtered_data,
                    {"before": current_values, "after": filtered_data},
                )

            # record does not exist
            return False, True, filtered_data, diff

        if state == "absent":
            if mkey is None:
                return (
                    False,
                    False,
                    filtered_data,
                    {"before": current_data["results"][0], "after": ""},
                )

            if is_existed:
                return (
                    False,
                    True,
                    filtered_data,
                    {"before": current_data["results"][0], "after": ""},
                )
            return False, False, filtered_data, {}

        return True, False, {"reason: ": "Must provide state parameter"}, {}

    if state == "present" or state is True:
        return fos.set("system", "wccp", data=filtered_data, vdom=vdom)

    elif state == "absent":
        return fos.delete("system", "wccp", mkey=filtered_data["service-id"], vdom=vdom)
    else:
        fos._module.fail_json(msg="state must be present or absent!")


def is_successful_status(resp):
    return (
        "status" in resp
        and resp["status"] == "success"
        or "http_status" in resp
        and resp["http_status"] == 200
        or "http_method" in resp
        and resp["http_method"] == "DELETE"
        and resp["http_status"] == 404
    )


def fortios_system(data, fos, check_mode):
    fos.do_member_operation("system", "wccp")
    if data["system_wccp"]:
        resp = system_wccp(data, fos, check_mode)
    else:
        fos._module.fail_json(msg="missing task body: %s" % ("system_wccp"))
    if isinstance(resp, tuple) and len(resp) == 4:
        return resp
    return (
        not is_successful_status(resp),
        is_successful_status(resp)
        and (resp["revision_changed"] if "revision_changed" in resp else True),
        resp,
        {},
    )


versioned_schema = {
    "type": "list",
    "elements": "dict",
    "children": {
        "service_id": {"v_range": [["v6.0.0", ""]], "type": "string", "required": True},
        "router_id": {"v_range": [["v6.0.0", ""]], "type": "string"},
        "cache_id": {"v_range": [["v6.0.0", ""]], "type": "string"},
        "group_address": {"v_range": [["v6.0.0", ""]], "type": "string"},
        "server_list": {
            "v_range": [["v6.0.0", ""]],
            "type": "list",
            "multiple_values": True,
            "elements": "str",
        },
        "router_list": {
            "v_range": [["v6.0.0", ""]],
            "type": "list",
            "multiple_values": True,
            "elements": "str",
        },
        "ports_defined": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "source"}, {"value": "destination"}],
        },
        "server_type": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "forward"}, {"value": "proxy"}],
        },
        "ports": {
            "v_range": [["v6.0.0", ""]],
            "type": "list",
            "multiple_values": True,
            "elements": "str",
        },
        "authentication": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "enable"}, {"value": "disable"}],
        },
        "password": {"v_range": [["v6.0.0", ""]], "type": "string"},
        "forward_method": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "GRE"}, {"value": "L2"}, {"value": "any"}],
        },
        "cache_engine_method": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "GRE"}, {"value": "L2"}],
        },
        "service_type": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "auto"}, {"value": "standard"}, {"value": "dynamic"}],
        },
        "primary_hash": {
            "v_range": [["v6.0.0", ""]],
            "type": "list",
            "options": [
                {"value": "src-ip"},
                {"value": "dst-ip"},
                {"value": "src-port"},
                {"value": "dst-port"},
            ],
            "multiple_values": True,
            "elements": "str",
        },
        "priority": {"v_range": [["v6.0.0", ""]], "type": "integer"},
        "protocol": {"v_range": [["v6.0.0", ""]], "type": "integer"},
        "assignment_weight": {"v_range": [["v6.0.0", ""]], "type": "integer"},
        "assignment_bucket_format": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "wccp-v2"}, {"value": "cisco-implementation"}],
        },
        "return_method": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "GRE"}, {"value": "L2"}, {"value": "any"}],
        },
        "assignment_method": {
            "v_range": [["v6.0.0", ""]],
            "type": "string",
            "options": [{"value": "HASH"}, {"value": "MASK"}, {"value": "any"}],
        },
        "assignment_srcaddr_mask": {"v_range": [["v6.0.0", ""]], "type": "string"},
        "assignment_dstaddr_mask": {"v_range": [["v6.0.0", ""]], "type": "string"},
    },
    "v_range": [["v6.0.0", ""]],
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = "service-id"
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": "bool", "default": False},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "member_path": {"required": False, "type": "str"},
        "member_state": {
            "type": "str",
            "required": False,
            "choices": ["present", "absent"],
        },
        "state": {"required": True, "type": "str", "choices": ["present", "absent"]},
        "system_wccp": {
            "required": False,
            "type": "dict",
            "default": None,
            "options": {},
        },
    }
    for attribute_name in module_spec["options"]:
        fields["system_wccp"]["options"][attribute_name] = module_spec["options"][
            attribute_name
        ]
        if mkeyname and mkeyname == attribute_name:
            fields["system_wccp"]["options"][attribute_name]["required"] = True

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    check_legacy_fortiosapi(module)

    is_error = False
    has_changed = False
    result = None
    diff = None

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if "access_token" in module.params:
            connection.set_option("access_token", module.params["access_token"])

        if "enable_log" in module.params:
            connection.set_option("enable_log", module.params["enable_log"])
        else:
            connection.set_option("enable_log", False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(
            fos, versioned_schema, "system_wccp"
        )

        is_error, has_changed, result, diff = fortios_system(
            module.params, fos, module.check_mode
        )

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result["matched"] is False:
        module.warn(
            "Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv"
        )

    if not is_error:
        if versions_check_result and versions_check_result["matched"] is False:
            module.exit_json(
                changed=has_changed,
                version_check_warning=versions_check_result,
                meta=result,
                diff=diff,
            )
        else:
            module.exit_json(changed=has_changed, meta=result, diff=diff)
    else:
        if versions_check_result and versions_check_result["matched"] is False:
            module.fail_json(
                msg="Error in repo",
                version_check_warning=versions_check_result,
                meta=result,
            )
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == "__main__":
    main()
