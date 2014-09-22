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


class VolumeController(wsgi.Controller):
    """The Volumes API controller for the OpenStack API."""

    def __init__(self, ext_mgr):
        self.manager = manager.VolumeManager()
        self.ext_mgr = ext_mgr
        super(VolumeController, self).__init__()

    def get_connector(self):
        connector = self.manager.get_connector()
        LOG.info(_("API get_Connector called"))
        return {"connector": connector}


def create_resource(ext_mgr):
    return wsgi.Resource(VolumeController(ext_mgr))
