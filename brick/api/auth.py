# Copyright (c) 2013 OpenStack Foundation
#
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

from brick.api.middleware import auth
from brick.i18n import _
from brick.openstack.common import log as logging


LOG = logging.getLogger(__name__)


class BrickKeystoneContext(auth.BrickKeystoneContext):
    def __init__(self, application):
        LOG.warn(_('brick.api.auth:BrickKeystoneContext is deprecated. '
                   'Please use '
                   'brick.api.middleware.auth:BrickKeystoneContext '
                   'instead.'))
        super(BrickKeystoneContext, self).__init__(application)


def pipeline_factory(loader, global_conf, **local_conf):
    LOG.warn(_('brick.api.auth:pipeline_factory is deprecated. Please use '
             'brick.api.middleware.auth:pipeline_factory instead.'))
    auth.pipeline_factory(loader, global_conf, **local_conf)
