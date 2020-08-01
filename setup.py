#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2018 Telefonica S.A.
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

from setuptools import setup

_name = "osm_ee"

_description = 'OSM Resource Orchestrator'
_author = 'ETSI OSM'
_author_email = 'illoret@indra.es'
_maintainer = 'alfonso.tiernosepulveda'
_maintainer_email = 'alfonso.tiernosepulveda@telefonica.com'
_license = 'Apache 2.0'
_url = 'TOBEDEFINED'
_requirements = [
    # Libraries needed by the code defined by osm
    "PyYAML",
    "grpcio-tools",
    "grpclib",
    "protobuf",

    # Libraries defined by the vnf code, they should be in an external file
    #"asyncssh",
]

setup(
    name=_name,
    #version_command=('0.1'), # TODO - replace for a git command
    version='1.0',
    description=_description,
    long_description=open('README.rst').read(),
    author=_author,
    author_email=_author_email,
    maintainer=_maintainer,
    maintainer_email=_maintainer_email,
    url=_url,
    license=_license,
    packages=[_name],
    package_dir={_name: _name},

    install_requires=_requirements,
    include_package_data=True,
    setup_requires=['setuptools-version-command'],
)