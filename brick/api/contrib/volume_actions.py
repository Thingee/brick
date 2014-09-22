#   Copyright 2012 OpenStack Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.


from brick.api import extensions
from brick.api.openstack import wsgi
from brick.openstack.common import log as logging
from brick.volume import manager


LOG = logging.getLogger(__name__)


class VolumeActionsController(wsgi.Controller):
    def __init__(self, *args, **kwargs):
        super(VolumeActionsController, self).__init__(*args, **kwargs)
        self.manager = manager.VolumeManager()

    @wsgi.action('os-connector')
    def _connector(self):
        LOG.debug("os-connector called")

        connector = self.manager.get_connector()
        LOG.debug("Connector = %s" % connector)
        return {"connector": connector}


class Volume_actions(extensions.ExtensionDescriptor):
    """Enable volume actions
    """

    name = "VolumeActions"
    alias = "os-volume-actions"
    namespace = "http://docs.openstack.org/volume/ext/volume-actions/api/v1.1"
    updated = "2012-05-31T00:00:00+00:00"

    def get_controller_extensions(self):
        controller = VolumeActionsController()
        extension = extensions.ControllerExtension(self, 'volumes', controller)
        return [extension]
