# Copyright 2011 Justin Santa Barbara
# All Rights Reserved.
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

"""The volumes api."""

from brick.api.openstack import wsgi
from brick.i18n import _
from brick.openstack.common import log as logging
from brick.volume import manager


LOG = logging.getLogger(__name__)


class ConnectorController(wsgi.Controller):
    """The local Connector API controller for the OpenStack API."""

    def __init__(self):
        super(ConnectorController, self).__init__()
        self.manager = manager.VolumeManager()

    def index(self, req):
        LOG.info(_("API get_Connector called"))
        connector = self.manager.get_connector()
        LOG.debug("Connector: %s" % connector)
        return {"connector": connector}


def create_resource():
    return wsgi.Resource(ConnectorController())
