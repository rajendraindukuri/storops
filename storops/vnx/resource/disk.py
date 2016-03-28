# coding=utf-8
# Copyright (c) 2015 EMC Corporation.
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
from __future__ import unicode_literals

import re

from storops.lib.common import check_text
from storops.vnx.resource import VNXCliResource, VNXCliResourceList

__author__ = 'Cedric Zhuang'


class VNXDisk(VNXCliResource):
    _index_pattern = re.compile('(\w+)_(\w+)_(\w+)')

    def __init__(self, index=None, cli=None):
        super(VNXDisk, self).__init__()
        self._cli = cli
        self._index = index
        if index is not None:
            self.parse_index(self.index)

    @property
    def bus(self):
        return self.parse_index(self._index)[0]

    @property
    def enclosure(self):
        return self.parse_index(self._index)[1]

    @property
    def disk(self):
        return self.parse_index(self._index)[2]

    @property
    def index(self):
        if self._index is None:
            if self.disk_index is not None:
                self._index = '{}_{}_{}'.format(*self.disk_index)
            else:
                raise ValueError('disk index is not initialized.')
        return self._index

    @property
    def index_string(self):
        bus, enc, disk = self.parse_index(self.index)
        return 'bus {} enclosure {} disk {}'.format(bus, enc, disk)

    def _get_raw_resource(self):
        return self._cli.get_disk(poll=self.poll,
                                  *self.parse_index(self._index))

    @classmethod
    def parse_index(cls, index):
        match = re.search(cls._index_pattern, index)
        if match is None:
            raise ValueError('invalid disk index.  disk index must '
                             'be something like '
                             '"1_2_A0", in which "1" is the bus id, "2"'
                             'is the enclosure id and "A0" is the disk id.')
        return match.groups()

    @classmethod
    def get(cls, cli, index=None):
        if index is None:
            ret = VNXDiskList(cli)
        else:
            index = check_text(index).upper()
            ret = VNXDisk(index, cli)
        return ret

    def remove(self):
        return self._cli.remove_disk(self._index, poll=self.poll)

    def install(self):
        return self._cli.install_disk(self._index, poll=self.poll)


class VNXDiskList(VNXCliResourceList):
    def __init__(self, cli=None, disk_indices=None):
        super(VNXDiskList, self).__init__(cli)
        if disk_indices is not None:
            self._disk_indices = [index.lower() for index in disk_indices
                                  if index is not None]
        else:
            self._disk_indices = None

    def _filter(self, disk):
        if self._disk_indices:
            index = disk.index
            ret = index and index.lower() in self._disk_indices
        else:
            ret = True
        return ret

    @classmethod
    def get_resource_class(cls):
        return VNXDisk

    def _get_raw_resource(self):
        return self._cli.get_disk(poll=self.poll)
