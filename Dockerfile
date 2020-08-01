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

FROM ubuntu:18.04

# Set the working directory to /app
WORKDIR /app/EE

# Libraries used by the base osm defined ee
RUN apt-get update && apt-get install -y git python3 python3-pip \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -U grpcio-tools \
    && python3 -m pip install -U grpclib \
    && python3 -m pip install -U PyYAML

# Copy the current directory contents into the container at /app/LCM
ADD . /app/EE

# Install as module
RUN python3 -m pip install -e /app/EE

# Install SNMP Generator and its dependencies
#RUN apt-get install -y python3-pip unzip build-essential libsnmp-dev wget curl
#RUN curl -s https://storage.googleapis.com/golang/go1.11.8.linux-amd64.tar.gz| tar -v -C /usr/local -xz
#ENV PATH $PATH:/usr/local/go/bin
#ENV GOPATH /go
#RUN go get github.com/go-logfmt/logfmt \
#    && go get github.com/go-kit/kit/log
#RUN wget -q https://github.com/prometheus/snmp_exporter/archive/v0.17.0.tar.gz -P /tmp/ \
#    && tar -C /tmp -xf /tmp/v0.17.0.tar.gz \
#    && (cd /tmp/snmp_exporter-0.17.0/generator && go build) \
#    && cp /tmp/snmp_exporter-0.17.0/generator/generator /usr/local/bin/snmp_generator

EXPOSE 50051

#CMD python3 -m osm_ee.frontend_server
# For development
CMD [ "bash", "-c", "while true; do /app/EE/osm_ee/scripts/ee_start.sh ; sleep 5; done" ]
