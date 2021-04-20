#!/usr/bin/env python3

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient


import json
import sys


from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.monitor.version import VERSION as monitor_client_version

if __name__ == '__main__':
    azure_client_id = sys.argv[1]
    azure_secret = sys.argv[2]
    azure_subscription_id = sys.argv[3]
    azure_tenant = sys.argv[4]
    region = sys.argv[5]


    credentials = ServicePrincipalCredentials(
        client_id=azure_client_id,
        secret=azure_secret,
        tenant=azure_tenant
    )

    compute_client = ComputeManagementClient(credentials, azure_subscription_id)
    virtual_machine_sizes = []
    for vm_size in compute_client.virtual_machine_sizes.list(region):
        dict_vm_size = {}
        dict_vm_size['name'] = vm_size.name
        dict_vm_size['max_data_disk_count'] = vm_size.max_data_disk_count
        dict_vm_size['memory_in_mb'] = vm_size.memory_in_mb
        dict_vm_size['number_of_cores'] = vm_size.number_of_cores
        dict_vm_size['os_disk_size_in_mb'] = vm_size.os_disk_size_in_mb
        dict_vm_size['resource_disk_size_in_mb'] = vm_size.resource_disk_size_in_mb
        virtual_machine_sizes.append(dict_vm_size)

    print(json.dumps(virtual_machine_sizes))