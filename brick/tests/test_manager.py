# (c) Copyright 2013 Hewlett-Packard Development Company, L.P.
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

import string

from brick.openstack.common import log as logging
from brick import test
from brick.volume import manager

import mock

LOG = logging.getLogger(__name__)


class VolumeManagerTestCase(test.TestCase):

    def setUp(self):
        super(VolumeManagerTestCase, self).setUp()
        self.cmds = []

    def fake_execute(self, *cmd, **kwargs):
        self.cmds.append(string.join(cmd))
        return "", None

    @mock.patch('socket.gethostname')
    @mock.patch('brick.initiator.linuxfc.LinuxFibreChannel.get_fc_wwnns')
    @mock.patch('brick.initiator.linuxfc.LinuxFibreChannel.get_fc_wwpns')
    @mock.patch('brick.initiator.connector.ISCSIConnector.get_initiator')
    def test_connect_volume(self, mock_iscsi, mock_fc_wwpns,
                            mock_fc_wwnns, mock_socket):

        fake_connector = {"host": "fakehost",
                          "initiator": "fake_iqn",
                          "ip": "10.0.0.1",
                          "wwnns": ["100010604b01045d"],
                          "wwpns": ["200010604b01045d"]
                          }

        mock_iscsi.return_value = fake_connector["initiator"]
        mock_fc_wwpns.return_value = fake_connector["wwpns"]
        mock_fc_wwnns.return_value = fake_connector["wwnns"]
        mock_socket.return_value = fake_connector["host"]
        mgr = manager.VolumeManager()

        mgr.configuration = mock.Mock()
        mgr.configuration.my_ip = fake_connector["ip"]
        connector = mgr.get_connector()
        self.assertEqual(fake_connector, connector)
