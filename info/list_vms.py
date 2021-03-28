#!/usr/bin/env python3

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

azure_client_id = '... service principal application id ...'
azure_secret = '... service principal secret/key ...'
azure_subscription_id = '... your subscription id ...'
azure_tenant = '... your tenant id ...'
region = '... substitute your region here ...'

credentials = ServicePrincipalCredentials(
    client_id=azure_client_id,
    secret=azure_secret,
    tenant=azure_tenant
)

compute_client = ComputeManagementClient(credentials, azure_subscription_id)

for _ in compute_client.virtual_machine_sizes.list(region):
    print(_.name)