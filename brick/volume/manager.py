#    (c) Copyright 2012-2014 Hewlett-Packard Development Company, L.P.
#    All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
"""The Brick volume manager, which services all requests.

The manager is responsible for local target creation and target discovery.

"""
from oslo.config import cfg

from brick.configuration import Configuration
from brick.initiator import connector
from brick.openstack.common import log as logging
from brick import utils


LOG = logging.getLogger(__name__)
volume_manager_opts = [

]
CONF = cfg.CONF
CONF.register_opts(volume_manager_opts)


class VolumeManager(object):
    """Manages target creation and discovery."""

    def __init__(self, service_name=None, *args, **kwargs):
        super(VolumeManager, self).__init__(*args, **kwargs)

        self.configuration = Configuration(volume_manager_opts,
                                           config_group=service_name)

    def get_connector(self):
        """Fetch the initiator side connection information."""
        root_helper = utils.get_root_helper()
        return connector.get_connector_properties(root_helper,
                                                  self.configuration.my_ip)
