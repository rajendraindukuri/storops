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

import logging

import storops
from storops.unity.resource import UnityResource, UnityResourceList
from storops.unity.client import UnityClient

__author__ = 'Rajendra Indukuri'

log = logging.getLogger(__name__)


class UnityUserQuota(UnityResource):
    """
    Support CRUD operations for user_quota

    Operations supported:
    create: Create user_quota on a file_system/tree_quota
    modify: Modify user_quota on a file_system/tree_quota
    """
    @classmethod
    def create(cls, cli, file_system_id=None, tree_quota_id=None,
               hard_limit=None, soft_limit=None, uid=None,
               unix_name=None, win_name=None):
        """
        Creates user_quota on the speficied filesystem or tree quota
        :param file_system_id: This is an optional parameter which if provided
            will create user_quota on the file_system specified. file_system_id
            and tree_quota_id cannot be given together
        :param tree_quota_id: This is an optional parameter which if provided
            will create user_quota on the tree_quota specified. file_system_id
            and tree_quota_id cannot be given together
        :param hard_limit: sets hard_limit  on the file_system for the user
            specified
        :param soft_limit: sets soft_limit  on the file_system for the user
            specified
        :param uid: This is an optional parameter to specify user. Either of
            uid/unix_name/win_name should be provided
        :param unix_name: This is an optional parameter to specify user. Either
            of uid/unix_name/win_name should be provided
        :param win_name:This is an optional parameter to specify user. Either
            of uid/unix_name/win_name should be provided
        :return: created user quota.
        """
        if file_system_id is not None:
            fs_clz = storops.unity.resource.filesystem.UnityFileSystem
            file_system = fs_clz.get(cli, file_system_id).verify()

        if tree_quota_id is not None:
            tquota_clz = storops.unity.resource.tree_quota.UnityTreeQuota
            tree_quota = tquota_clz.get(cli, tree_quota_id).verify()

        user_quota_param = cls.prepare_user_quota_create_parameters(
            file_system, tree_quota, hard_limit, soft_limit, uid,
            unix_name, win_name)
        resp = cli.post(
            cls().resource_class, **user_quota_param)
        resp.raise_if_err()
        return cls(_id=resp.resource_id, cli=cli)

    @classmethod
    def modify(cls, cli, user_quota_id, hard_limit=None, soft_limit=None):
        """
        Modifies user_quota params for the specified user_quota_id
        :param user_quota_id: This is required which speicfies user_quota to
            be modified
        :param hard_limit: modifies hard_limit  on the file_system for the
            user_quota specified
        :param soft_limit: modifies soft_limit  on the file_system for the
            user_quota specified
        :return: created user quota.
        """
        req_body = cli.make_body(
            allow_empty=False,
            hardLimit=hard_limit,
            softLimit=soft_limit
           )
        resp = cli.action(cls().resource_class, user_quota_id,
                          'modify', **req_body)
        resp.raise_if_err()
        return resp

    @staticmethod
    def prepare_user_quota_create_parameters(
            file_system, tree_quota, hard_limit, soft_limit,
            uid, unix_name, win_name):
        """
        Prepare user_quota for the create operation
        :param file_system: This is needed if the user_quota is to be
            created on the file_system
        :param tree_quota: This is needed if the user_quota is to be
            created on the tree_quota
        :param hard_limit: hard_limit for the user_quota
        :param soft_limit: soft_limit for the user_quota
        :return: user_quota_params for create user_quota preparation
        """
        user_quota_param = UnityClient.make_body(
            allow_empty=False,
            filesystem=file_system,
            treeQuota=tree_quota,
            hardLimit=hard_limit,
            softLimit=soft_limit,
            uid=uid,
            unixName=unix_name,
            winName=win_name)
        return user_quota_param


class UnityUserQuotaList(UnityResourceList):
    """
    List representation of user_quota
    """
    def __init__(self, cli=None, **filters):
        super(UnityUserQuotaList, self).__init__(cli, **filters)

    @classmethod
    def get_resource_class(cls):
        return UnityUserQuota
