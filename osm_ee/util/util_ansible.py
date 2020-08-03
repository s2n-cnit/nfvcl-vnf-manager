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

import logging
import json
from shlex import quote

import osm_ee.util.util_ee as util_ee

logger = logging.getLogger("osm_ee.util_ansible")


async def execute_playbook(playbook_name: str, inventory: str, extra_vars: dict,
                           ) -> (int, str):

    command = 'ansible-playbook --inventory={} --extra-vars {} {}'.format(quote(inventory),
                                                                          quote(json.dumps(extra_vars)),
                                                                          quote(playbook_name))

    logger.debug("Command to be executed: {}".format(command))

    return_code, stdout, stderr = await util_ee.local_async_exec(command)
    logger.debug("Return code: {}".format(return_code))
    logger.debug("stdout: {}".format(stdout))
    logger.debug("stderr: {}".format(stderr))

    return return_code, stdout, stderr
