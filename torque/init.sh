#!/usr/bin/env bash

# first record all available nodes
python /usr/local/bin/detect_nodes.py

# start the torque server to initialize the queue
service torque-server start

# setup the queue
qmgr -c 'create queue default queue_type = execution'
qmgr -c 'set queue default started = True'
qmgr -c 'set queue default enabled = True'
qmgr -c 'set queue default resources_default.nodes = 1'
qmgr -c 'set queue default resources_default.walltime = 1:00:00'
qmgr -c 'set server default_queue = default'
qmgr -c 'set server submit_hosts = torque,jupyter,fireworks'
qmgr -c 'set server allow_node_submit = True'
qmgr -c 'set server disable_server_id_check = True'
qmgr -c 'set server acl_host_enable = False'
qmgr -c 'set server scheduling = True'
qmgr -c 'set server keep_completed = 300'
qmgr -c 'set server mom_job_sync = True'
qmgr -c 'set server auto_node_np = True'

# restart torque server and start scheduler
service torque-server restart
service torque-scheduler start
