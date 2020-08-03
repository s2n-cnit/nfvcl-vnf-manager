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
import asyncio
from shlex import split

logger = logging.getLogger("osm_ee.util")


async def local_async_exec(command: str
                           ) -> (int, str, str):
    """
        Executed a local command using asyncio.
        TODO - do not know yet if return error code, and stdout and strerr or just one of them
    """
    scommand = split(command)

    logger.debug("Execute local command: {}".format(command))
    process = await asyncio.create_subprocess_exec(
        *scommand,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # wait for command terminate
    stdout, stderr = await process.communicate()

    return_code = process.returncode
    logger.debug("Return code: {}".format(return_code))

    output = ""
    if stdout:
        output = stdout.decode()
        logger.debug("Output: {}".format(output))

    if stderr:
        out_err = stderr.decode()
        logger.debug("Stderr: {}".format(out_err))

    return return_code, stdout, stderr
