# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['webpubsub'] = """
    type: group
    short-summary: Commands to manage Webpubsub.
"""

helps['webpubsub key'] = """
    type: group
    short-summary: Commands to manage Webpubsub keys.
"""

helps['webpubsub event-handler'] = """
    type: group
    short-summary: Commands to manage Webpubsub event handler settings.
"""

helps['webpubsub event-handler hub'] = """
    type: group
    short-summary: Commands to manage Webpubsub hub settings.
"""

helps['webpubsub network-rule'] = """
    type: group
    short-summary: Commands to manage Webpubsub network rules.
"""

helps['webpubsub create'] = """
    type: command
    short-summary: Create a Webpubsub.
    examples:
      - name: Create a WebPubSub Service with Standard SKU and unit 2.
        text: >
          az webpubsub create -n MyWebPubSub -g MyResourceGroup --sku Standard_S1 --unit-count 2
"""

helps['webpubsub list'] = """
    type: command
    short-summary: List Webpubsub.
"""

helps['webpubsub delete'] = """
    type: command
    short-summary: Delete a Webpubsub.
"""

helps['webpubsub show'] = """
    type: command
    short-summary: Show details of a Webpubsub.
"""

helps['webpubsub update'] = """
    type: command
    short-summary: Update a Webpubsub.
    examples:
      - name: Update a WebPubSub Service to unit 10.
        text: >
          az webpubsub update -n MyWebPubSub -g MyResourceGroup --sku Standard_S1 --unit-count 10
"""

helps['webpubsub restart'] = """
    type: command
    short-summary: Restart a Webpubsub.
"""

helps['webpubsub key show'] = """
    type: command
    short-summary: Show connetion strings and keys for a WebPubSub Service
    examples:
      - name: Get the primary key for a WebPubSub Service.
        text: >
          az webpubsub key show -n MyWebPubSub -g MyResourceGroup --query primaryKey -o tsv
"""

helps['webpubsub key regenerate'] = """
    type: command
    short-summary: Regenerate keys for a WebPubSub Service
    examples:
      - name: Regenerate the primary key for a WebPubSub Service.
        text: >
          az webpubsub key regenerate -n MyWebPubSub -g MyResourceGroup --key-type primary --query primaryKey -o tsv
"""

helps['webpubsub network-rule show'] = """
    type: command
    short-summary: Get the Network access control of WebPubSub Service.
"""

helps['webpubsub network-rule update'] = """
    type: command
    short-summary: Update the Network access control of WebPubSub Service.
    examples:
      - name: Set allowing RESTAPI only for public network.
        text: >
            az webpubsub network-rule update --public-network -n MyWebPubSub -g MyResourceGroup --allow RESTAPI
      - name: Set allowing client connection and server connection for a private endpoint connection
        text: >
            az webpubsub network-rule update --connection-name MyPrivateEndpointConnection -n MyWebPubSub -g MyResourceGroup --allow ClientConnection ServerConnection
      - name: Set denying client connection for both public network and private endpoint connections
        text: >
            az webpubsub network-rule update --public-network --connection-name MyPrivateEndpointConnection1 MyPrivateEndpointConnection2 -n MyWebPubSub -g MyResourceGroup --deny ClientConnection
"""

helps['webpubsub event-handler show'] = """
    type: command
    short-summary: Show event handler settings for WebPubSub Service.
"""

helps['webpubsub event-handler clear'] = """
    type: command
    short-summary: Clear event handler settings for WebPubSub Service.
"""

helps['webpubsub event-handler update'] = """
    type: command
    short-summary: Update event handler settings for WebPubSub Service with json. For updating settings per hub, see help in hub subgroup.
    examples:
      - name: Update event handler to handler connect event.
        text: >
            az webpubsub event-handler update -n MyWebPubSub -g MyResourceGroup --items '{\"myHub\": [{\"urlTemplate\": \"http://host.com\", \"systemEventPattern\": \"connect\"}]}'
"""

helps['webpubsub event-handler update'] = """
    type: command
    short-summary: Update event handler settings for WebPubSub Service.
    examples:
      - name: Update event handler to handler connect event.
        text: >
            az webpubsub event-handler update -n MyWebPubSub -g MyResourceGroup --items '{\"myHub\": [{\"urlTemplate\": \"http://host.com\", \"systemEventPattern\": \"connect\"}]}'
"""

helps['webpubsub event-handler hub remove'] = """
    type: command
    short-summary: Remove a hub's event handler settings
    examples:
      - name: Remove all event handler settings in a hub
        text: >
            az webpubsub event-handler hub remove -n MyWebPubSub -g MyResourceGroup --hub-name MyHub
"""

helps['webpubsub event-handler hub update'] = """
    type: command
    short-summary: Update a hub's event handler settings
    examples:
      - name: Update two event handler settings in a hub
        text: >
            az webpubsub event-handler hub update -n MyWebPubSub -g MyResourceGroup --hub-name MyHub --template url-template='http://host.com user-event-pattern="MyEvent" --template url-template="http://host2.com" system-event-pattern="connect"'
"""
