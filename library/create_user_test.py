#!/usr/bin/env python3


from ansible.module_utils.basic import *

def main():
	module = AnsibleModule(argument_spec={})
	response = {"hello": "world"}
	print("TEST LECTURE SCRIPT")
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
	main()
