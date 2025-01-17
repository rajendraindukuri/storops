StorOps: The Python Library for VNX & Unity
===========================================

.. image:: https://img.shields.io/travis/emc-openstack/storops/master.svg
    :target: https://travis-ci.org/emc-openstack/storops

.. image:: https://img.shields.io/codecov/c/github/emc-openstack/storops/master.svg
    :target: https://codecov.io/gh/emc-openstack/storops

.. image:: https://img.shields.io/appveyor/ci/peter-wangxu/storops/master.svg?label=Windows
       :target: https://ci.appveyor.com/project/peter-wangxu/storops

.. image:: https://img.shields.io/pypi/v/storops.svg
    :target: https://pypi.python.org/pypi/storops

.. image:: https://img.shields.io/pypi/pyversions/storops.svg
    :target: https://pypi.org/project/storops/

.. image:: https://landscape.io/github/emc-openstack/storops/master/landscape.svg?style=flat
    :target: https://landscape.io/github/emc-openstack/storops/

VERSION: 1.2.8

A minimalist Python library to manage VNX/Unity systems.
This document lies in the source code and go with the release.
Check different release branch/tag for matched documents.

License
-------

`Apache License version 2`_

Install via PIP
---------------
You could use "pip" to install "storops".

.. code-block:: bash

    $ pip install storops

Make sure `naviseccli` is installed if you want to manage VNX.
Please contact with Dell/EMC support about installing the `NaviCli-Linux` rpm package.

Optional package requirement
````````````````````````````

#. `paramiko` package

The `paramiko` is required if you need to manage the VNX file related
resources. please follow `install paramiko <http://www.paramiko.org/installing.html>`_ install `paramiko`.

Install via RPM
---------------
There are two RPM packages in each release page.
- `python-storops-<version num>`, install this if you only manage Unity systems.
- `python-storops-vnx-<version num>-x86_64`, a virtual package depends on `python-storops` and `NaviCli-Linux`. Install this if you manage VNX systems or both.

You could download the rpm package from release download page, and install it via:

.. code-block:: bash

    $ rpm -i <python-storops_file>

Please contact with Dell/EMC support about installing the `NaviCli-Linux` rpm package.


Feature List
------------

- Manage VNX System
    - supported resources
        - show system properties
        - list installed features
        - list/create/delete storage pools
        - list/create/delete pool based LUN
        - list/create/delete RAID groups
        - list/create/delete snapshots
        - list/create/delete storage groups
        - list/create/delete consistency groups
        - list/create/delete users
        - list disks
        - list ports
        - list data mover/virtual data mover
        - list NAS storage pool
        - list/create/delete CIFS server
        - list CIFS share
        - list/create/delete file system
        - list/create/delete file system snap
        - list/create/delete NFS share
        - show system domain information
        - list hosts
        - show system capacity
    - supported feature/operations
        - list/start/cancel migration sessions
        - enable/disable LUN deduplication
        - enable/disable LUN compression
        - insert/delete disk simulation
        - create/attach/detach mount points
        - initiator and connection management
        - create/delete mirror view
        - create/delete DNS
    - supported metrics
        - VNXStorageProcessor
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
            - `read_size_kb`/`write_size_kb`: read/write size KB
        - VNXLun
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
                - `read_iops_sp_a`/`write_iops_sp_b`: read/write IOPS of SPA
                - `read_iops_sp_b`/`write_iops_sp_b`: read/write IOPS of SPB
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
                - `read_mbps_sp_a`/`write_mbps_sp_a`: read/write MBPS of SPA
                - `read_mbps_sp_b`/`write_mbps_sp_b`: read/write MBPS of SPB
            - `implicit_trespasses_ps`/`explicit_trespasses_ps`: implicit/explicit trespasses per second
                - `implicit_trespasses_ps_sp_a`/`explicit_trespasses_ps_sp_a`: implicit/explicit trespasses per second of SPA
                - `implicit_trespasses_ps_sp_b`/`explicit_trespasses_ps_sp_b`: implicit/explicit trespasses per second of SPB
            - `utilization`: utilization
                - `utilization_sp_a`: utilization of SPA
                - `utilization_sp_b`: utilization of SPB
            - `read_size_kb`/`write_size_kb`: read/write size KB
        - VNXDisk
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
            - `utilization`: utilization
            - `read_size_kb`/`write_size_kb`: read/write size KB
        - VNXSPPort
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
            - `read_size_kb`/`write_size_kb`: read/write size KB
        - VNXStorageGroup
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
            - `read_size_kb`/`write_size_kb`: read/write size KB
        - VNXStoragePool
            - `read_iops`/`write_iops`/`total_iops`: read/write/total IOPS
            - `read_mbps`/`write_mbps`/`total_mbps`: read/write/total MBPS
            - `read_size_kb`/`write_size_kb`: read/write size KB
- Manage Unity System
    - supported resources
        - show system properties
        - show system capacity
        - list/create/delete storage pools
        - list/create/delete remote hosts
        - list/create/delete host initiator
        - list/create/delete luns
        - list/create/delete file systems
        - list/create/delete snapshots
        - list/create/delete NAS servers
        - list/create/delete CIFS servers
        - list/create/delete CIFS shares
        - list/create/delete NFS servers
        - list/create/delete NFS shares
        - list/create/delete DNS servers
        - list ip ports
        - list sas ports
        - list/create/delete iSCSI portals
        - list/create/delete link aggregations
        - list/create/delete Consistency Groups
        - list/create/modify/cancel move sessions
        - list/create/delete metric real time query
        - list metrics query result
        - list disks
        - list disk groups
        - list/create/delete tenants
        - list batteries
        - list daes
        - list fans
        - list memory modules
        - list management interfaces
        - list power supplies
        - list ssds
        - list remote interfaces
        - list/create/modify/verify/delete remote systems
        - list/create/modify/delete replication interfaces
        - list/create/modify/delete replication sessions
        - failover/failback/pause/resume/sync replication sessions
        - list/create/modify/delete block import sessions
        - pause/resume/cutover/commit/cancel block import sessions
        - discover migration objects
        - list/create/modify/delete snapshot schedule
    - supported feature/operations
        - CIFS share access control
        - NFS share access control
        - Remote hosts access
        - Persist historical metric data to csv files
        - Upload license
        - enable/disable LUN data reduction
        - LUN migration
        - LUN replication
        - CG replication
    - supported metrics
        - UnitySystem
            - read_iops
            - write_iops
            - total_iops
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate
        - UnityDisk
            - read_iops
            - write_iops
            - total_iops
            - read_mbps
            - write_mbps
            - utilization
            - response_time
            - queue_length
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate
        - UnityLun
            - read_iops
            - write_iops
            - total_iops
            - read_mbps
            - write_mbps
            - utilization
            - response_time
            - queue_length
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate
        - UnityFileSystem
            - read_iops
            - write_iops
            - read_mbps
            - write_mbps
        - UnityStorageProcessor
            - net_in_mbps
            - net_out_mbps
            - block_read_iops
            - block_write_iops
            - block_total_iops
            - block_read_mbps
            - block_write_mbps
            - cifs_read_iops
            - cifs_write_iops
            - cifs_read_mbps
            - cifs_write_mbps
            - nfs_read_iops
            - nfs_write_iops
            - nfs_read_mbps
            - nfs_write_mbps
            - utilization
            - block_cache_read_hit_ratio
            - block_cache_write_hit_ratio
            - temperature
            - core_count
            - block_cache_dirty_size
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate
            - fast_cache_read_hits
            - fast_cache_write_hits
            - fast_cache_read_hit_rate
            - fast_cache_write_hit_rate
        - UnityFcPort
            - read_iops
            - write_iops
            - total_iops
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate
        - UnityIscsiNode
            - read_iops
            - write_iops
            - total_iops
            - read_byte_rate
            - write_byte_rate
            - total_byte_rate

Tutorial
--------

User may reference three kinds of classes directly.
All of them are available under the storops module.

- system classes: like VNXSystem and UnitySystem
- exceptions: like UnityException, VNXException, etc.
- enums: like VNXProvisionEnum, NFSTypeEnum, etc.

We recommend to try the library with IPython notebook or shell.

All operation/resource are accessed from the system instance.

Here are some examples of the typical usage:

Get the VNX System Instance
```````````````````````````
Use the vnx instance to access all sorts of resource and features.

.. code-block:: python

    # initialize the VNX system instance
    >>> from storops import VNXSystem
    >>> vnx = VNXSystem('10.1.1.1', 'sysadmin', 'password')
    >>> vnx
    {
        "VNXSystem": {
            "existed": true,
            "hash": 5339308,
            "name": "K10",
            "agent_rev": "7.33.8 (2.97)",
            "model_type": "Rackmount",
            "model": "VNX5800",
            "serial": "APM00123456789",
            "revision": "05.33.008.3.297"
        }
    }

Get the Unity System Instance
`````````````````````````````

.. code-block:: python

    from storops import UnitySystem
    unity = UnitySystem('<management ip>', '<user>', '<password>')

Get Resources from System or Other Resources
````````````````````````````````````````````

.. code-block:: python

    # get all pools
    >>> pools = vnx.get_pool()
    {
    "VNXPoolList": [
        {
            "VNXPool": {
                "luns": [
                    1,
                    0
                ],
                "status": "OK(0x0)",
                "current_operation_status": "N/A",
                ...
                "disks": {
                    "VNXDiskList": [
                        {
                            "VNXDisk": {
                                "private": {},
                                "clariion_tla_part_number": "005050344PWR",
                                "prct_bound": {},
    ...

Get a Resource
``````````````

Attention: you could still initialize the python object even
if the resource doesn't exists on array.
You could use the "existed" property to check the existance of the
resource.

.. code-block:: python

    # get a existing LUN
    >>> lun = vnx.get_lun(lun_id=1)
    >>> lun
    {
        "VNXLun": {
            "status": "OK(0x0)",
            "existed": true,
            ...
            "default_owner": "VNXSPEnum.SP_B",
            "name": "l0"
        }
    }

    # get a non-existing lun
    >>> vnx.get_lun(name='hello')
    {
        "VNXLun": {
            "existed": false,
            "hash": 5699430
        }
    }


Access Resource Properties
``````````````````````````
Each properties printed in the json output could be accessed directly.

.. code-block:: python

    # access resource properties
    >>> lun.status
    u'OK(0x0)'


Update the Resource Property
````````````````````````````

All properties of a resource will be updated if any of them is accessed.
For performance concern, the lib won't send query to array once properties
are initialized.
Explicitly call the *"update()"* function if you need a refresh.

.. code-block:: python

    >>> vnx = VNXSystem('10.1.1.3')     # no query to the system
    >>> vnx.model
    u'VNX5800'                          # send query, initialize all properties
    >>> vnx.name
    u'k10'                              # no query
    >>> vnx.update()                    # send query, update all properties


Executing Operations
````````````````````
Most of the create/modify operations can be found on the instance.
Call these instance methods to execute the operation.

.. code-block:: python

    # create lun
    >>> pool = pools[0]
    >>> lun1 = pool.create_lun('lun1', size_gb=2)

Remove a Resource
`````````````````

.. code-block:: python

    # delete a resource
    >>> lun1.delete()

Getting metrics
```````````````
- VNX

.. code-block:: python

    >>> from storops import VNXSystem
    >>> vnx = VNXSystem('<management ip>', '<user>', '<password>')
    # Enable metric query
    >>> vnx.enable_perf_stats()
    # Get iops for Storage Processor
    >>> sp = vnx.get_sp()[0] 
    >>> sp.read_iops
    0.0
    >>> sp.write_iops
    0.6666666666666666
    >>> sp.read_size_kb
    0.0
    >>> sp.write_size_kb
    4.2250000000000005

    
- Unity

.. code-block:: python

    >>> from storops import UnitySystem
    >>> unity = UnitySystem('<management ip>', '<user>', '<password>')
    # Enable metric query
    >>> unity.enable_perf_stats()
    # Once metric query enabled, storops will pull the realtime metric info
    # from Unity periodically and calculate them, the default interval is
    # 60s, so suggest to wait more than 60s for the first time calculation
    >>> import time; time.sleep(60)
    # Get iops, bandwidth for lun
    >>> lun1 = unity.get_lun()[0]
    >>> lun1.read_iops
    0.05
    >>> lun1.total_iops
    0.05
    >>> lun1.write_iops
    0
    >>> lun1.read_byte_rate
    25.6
    >>> lun1.write_byte_rate
    0
    >>> lun1.total_byte_rate
    25.6

Getting Help
````````````

- If you are using IPython, use "?" to check the document and
  method signature.

.. code-block::

    >>> pool.create_lun?
    Signature: pool.create_lun(lun_name=None, size_gb=1, lun_id=None,
               provision=None, tier=None, ignore_thresholds=None)
    Docstring: Create a pool LUN in the pool.
    File:      c:\work\python\storops\storops\vnx\resource\block_pool.py
    Type:      instancemethod

-  In IPython, use tab to check all extrinsic methods/properties
   of the resource.  Print the resource to check all intrinsic properties.

.. code-block::

    >>> vnx.
    vnx.control_station_ip           vnx.get_property_key             vnx.parse_all
    vnx.create_cg                    vnx.get_property_label           vnx.parsed_resource
    vnx.create_pool                  vnx.get_rg                       vnx.poll
    vnx.create_rg                    vnx.get_sg                       vnx.property_names
    vnx.create_sg                    vnx.get_snap                     vnx.delete_cg
    vnx.domain                       vnx.get_sp_port                  vnx.delete_disk
    vnx.existed                      vnx.heartbeat                    vnx.delete_pool
    vnx.get_available_disks          vnx.install_disk                 vnx.delete_rg
    vnx.get_cg                       vnx.is_auto_tiering_enabled      vnx.delete_sg
    vnx.get_connection_port          vnx.is_compression_enabled       vnx.delete_snap
    vnx.get_dict_repr                vnx.is_dedup_enabled             vnx.set_block_credential
    vnx.get_disk                     vnx.is_fast_cache_enabled        vnx.set_cli
    vnx.get_fc_port                  vnx.is_mirror_view_async_enabled vnx.set_naviseccli
    vnx.get_fcoe_port                vnx.is_mirror_view_enabled       vnx.spa_ip
    vnx.get_index                    vnx.is_mirror_view_sync_enabled  vnx.spb_ip
    vnx.get_iscsi_port               vnx.is_sancopy_enabled           vnx.stop_heart_beat
    vnx.get_lun                      vnx.is_snap_enabled              vnx.update
    vnx.get_migration_session        vnx.is_thin_enabled              vnx.update_nodes_ip
    vnx.get_ndu                      vnx.is_valid                     vnx.with_no_poll
    vnx.get_pool                     vnx.json                         vnx.with_poll
    vnx.get_pool_feature             vnx.parse

How to Run Unittests
--------------------

Unittests are included in the `storops_test` package.

Use following command to install test dependencies.

.. code-block:: bash

    $ pip install -r test-requirements.txt

Use `pytest` to run the tests.

.. code-block:: bash

    $ pytest storops_test

Or you could use `tox` to run the tests.

.. code-block:: bash

    $ tox -e py36


How to Contribute
-----------------

#. Open an issue at the `GitHub storops project`_.
#. Fork the repository on GitHub and make changes on your branch.
#. Add tests to cover your change.
#. Send a pull request.
#. Make sure to add yourself to "Contributors" listed below.

Contributors
------------

EMC Contributors
````````````````

- Ryan Liang <ryan.liang@dell.com>
- Yong Huang <yong.huang@dell.com>
- Dong Ding <dong.ding@dell.com>

Community Contributors
``````````````````````

- Cedric Zhuang
- Jay Xu
- Ray Chen
- Tina Tang
- Peter Wang
- Paulo Matias <matias@ufscar.br>

Patches and Suggestions
```````````````````````


.. _GitHub storops project: https://github.com/emc-openstack/storops
.. _Apache License version 2: LICENSE.txt
