# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def storageimportexport_location_list(cmd, client):
    return client.list()


def storageimportexport_location_show(cmd, client,
                                      location_name):
    return client.get(location_name=location_name)


def storageimportexport_job_list(cmd, client,
                                 top=None,
                                 filter=None,
                                 resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(top=top,
                                             filter=filter,
                                             resource_group_name=resource_group_name)
    return client.list_by_subscription(top=top,
                                       filter=filter)


def storageimportexport_job_show(cmd, client,
                                 job_name,
                                 resource_group_name):
    return client.get(job_name=job_name,
                      resource_group_name=resource_group_name)


def storageimportexport_job_create(cmd, client,
                                   job_name,
                                   resource_group_name,
                                   client_tenant_id=None,
                                   location=None,
                                   tags=None,
                                   properties=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    if isinstance(properties, str):
        properties = json.loads(properties)
    return client.create(job_name=job_name,
                         resource_group_name=resource_group_name,
                         client_tenant_id=client_tenant_id,
                         location=location,
                         tags=tags,
                         properties=properties)


def storageimportexport_job_update(cmd, client,
                                   job_name,
                                   resource_group_name,
                                   tags=None,
                                   properties_cancel_requested=None,
                                   properties_state=None,
                                   properties_return_address=None,
                                   properties_return_shipping=None,
                                   properties_delivery_package=None,
                                   properties_log_level=None,
                                   properties_backup_drive_manifest=None,
                                   properties_drive_list=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    return client.update(job_name=job_name,
                         resource_group_name=resource_group_name,
                         tags=tags,
                         cancel_requested=properties_cancel_requested,
                         state=properties_state,
                         return_address=properties_return_address,
                         return_shipping=properties_return_shipping,
                         delivery_package=properties_delivery_package,
                         log_level=properties_log_level,
                         backup_drive_manifest=properties_backup_drive_manifest,
                         drive_list=properties_drive_list)


def storageimportexport_job_delete(cmd, client,
                                   job_name,
                                   resource_group_name):
    return client.delete(job_name=job_name,
                         resource_group_name=resource_group_name)


def storageimportexport_bit_locker_key_list(cmd, client,
                                            job_name,
                                            resource_group_name):
    return client.list(job_name=job_name,
                       resource_group_name=resource_group_name)
