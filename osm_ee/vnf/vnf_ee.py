##
# Copyright 2019 Telefonica Investigacion y Desarrollo, S.A.U.
# This file is part of OSM
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For those usages not covered by the Apache License, Version 2.0 please
# contact with: nfvlabs@tid.es
##

import asyncio
import logging

from osm_ee.exceptions import VnfException


class VnfEE:

    def __init__(self, config_params):
        self.logger = logging.getLogger('osm_ee.vnf')
        self.config_params = config_params

    async def config(self, id, params):
        self.logger.debug("Execute action config params: {}".format(params))
        # Config action is special, params are merged with previous config calls
        self.config_params.update(params)
        yield "OK", "Configured"

    async def sleep(self, id, params):
        self.logger.debug("Execute action sleep, params: {}".format(params))

        for i in range(3):
            await asyncio.sleep(5)
            self.logger.debug("Temporal result return, params: {}".format(params))
            yield "PROCESSING", f"Processing {i} action id {id}"
        yield "OK", f"Processed action id {id}"

    @staticmethod
    def _check_required_params(params, required_params):
        for required_param in required_params:
            if required_param not in params:
                raise VnfException("Missing required param: {}".format(required_param))
