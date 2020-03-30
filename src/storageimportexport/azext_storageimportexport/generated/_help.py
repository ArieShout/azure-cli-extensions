# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['storageimportexport location'] = """
    type: group
    short-summary: storageimportexport location
"""

helps['storageimportexport location list'] = """
    type: command
    short-summary: Returns a list of locations to which you can ship the disks associated with an import or export job.\
 A location is a Microsoft data center region.
    examples:
      - name: List locations
        text: |-
               az storageimportexport location list
"""

helps['storageimportexport location show'] = """
    type: command
    short-summary: Returns the details about a location to which you can ship the disks associated with an import or ex\
port job. A location is an Azure region.
    examples:
      - name: Get locations
        text: |-
               az storageimportexport location show --location-name "West US"
"""

helps['storageimportexport job'] = """
    type: group
    short-summary: storageimportexport job
"""

helps['storageimportexport job list'] = """
    type: command
    short-summary: Returns all active and completed jobs in a subscription.
    examples:
      - name: List jobs in a resource group
        text: |-
               az storageimportexport job list --resource-group "Default-Storage-WestUS"
"""

helps['storageimportexport job show'] = """
    type: command
    short-summary: Gets information about an existing job.
    examples:
      - name: Get job
        text: |-
               az storageimportexport job show --job-name "test-by1-import" --resource-group "Default-Storage-WestUS"
"""

helps['storageimportexport job create'] = """
    type: command
    short-summary: Creates a new job or updates an existing job in the specified subscription.
    examples:
      - name: Create job
        text: |-
               az storageimportexport job create --location "West US" --properties "{\\"backupDriveManifest\\":true,\\"\
diagnosticsPath\\":\\"waimportexport\\",\\"driveList\\":[{\\"bitLockerKey\\":\\"238810-662376-448998-450120-652806-2033\
90-606320-483076\\",\\"driveHeaderHash\\":\\"\\",\\"driveId\\":\\"9CA995BB\\",\\"manifestFile\\":\\"\\\\\\\\DriveManife\
st.xml\\",\\"manifestHash\\":\\"109B21108597EF36D5785F08303F3638\\"}],\\"jobType\\":\\"Import\\",\\"logLevel\\":\\"Verb\
ose\\",\\"returnAddress\\":{\\"city\\":\\"Redmond\\",\\"countryOrRegion\\":\\"USA\\",\\"email\\":\\"Test@contoso.com\\"\
,\\"phone\\":\\"4250000000\\",\\"postalCode\\":\\"98007\\",\\"recipientName\\":\\"Tets\\",\\"stateOrProvince\\":\\"wa\\\
",\\"streetAddress1\\":\\"Street1\\",\\"streetAddress2\\":\\"street2\\"},\\"storageAccountId\\":\\"/subscriptions/aaaaa\
aaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/Default-Storage-WestUS/providers/Microsoft.ClassicStorage/storageAccount\
s/test\\"}" --job-name "test-by1-import" --resource-group "Default-Storage-WestUS"
"""

helps['storageimportexport job update'] = """
    type: command
    short-summary: Updates specific properties of a job. You can call this operation to notify the Import/Export servic\
e that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also \
be used to cancel an existing job.
    examples:
      - name: Update job
        text: |-
               az storageimportexport job update --properties-backup-drive-manifest true --properties-log-level "Verbos\
e" --properties-state "" --job-name "test-by1-import" --resource-group "Default-Storage-WestUS"
"""

helps['storageimportexport job delete'] = """
    type: command
    short-summary: Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.
    examples:
      - name: Delete job
        text: |-
               az storageimportexport job delete --job-name "test-by1-import" --resource-group "Default-Storage-WestUS"
"""

helps['storageimportexport bit-locker-key'] = """
    type: group
    short-summary: storageimportexport bit-locker-key
"""

helps['storageimportexport bit-locker-key list'] = """
    type: command
    short-summary: Returns the BitLocker Keys for all drives in the specified job.
    examples:
      - name: List BitLocker Keys for drives in a job
        text: |-
               az storageimportexport bit-locker-key list --job-name "test-by1-import" --resource-group "Default-Storag\
e-WestUS"
"""
