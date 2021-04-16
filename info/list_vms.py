#!/usr/bin/env python3

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

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

for _ in compute_client.virtual_machine_sizes.list(region):
    print(_.name)
