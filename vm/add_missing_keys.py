#!/usr/bin/env python3
import json
import sys

if __name__ == '__main__':
    instances_file_path = sys.argv[1]

    f = open(instances_file_path, )
    instances = json.load(f)
    for inst_name in instances:
        inst = instances[inst_name]
        if 'assign_public_ip' not in inst:
            inst['assign_public_ip'] = 'Static'
        if 'assign_public_ip' in inst:
            if inst['assign_public_ip'] == 'yes':
                inst['assign_public_ip'] = 'Static'
            if inst['assign_public_ip'] == 'no':
                inst['assign_public_ip'] = 'Disabled'
    print(json.dumps(instances))
