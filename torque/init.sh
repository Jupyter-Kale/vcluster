#!/usr/bin/env bash

# first record all available nodes
python /usr/local/bin/detect_nodes.py

# start the torque server to initialize the queue
service torque-server start

# setup the queue
qmgr -c 'set server scheduling = true'
qmgr -c 'set server keep_completed = 300'
qmgr -c 'set server mom_job_sync = true'
qmgr -c 'create queue default'
qmgr -c 'set queue default queue_type = execution'
qmgr -c 'set queue default started = true'
qmgr -c 'set queue default enabled = true'
qmgr -c 'set queue default resources_default.walltime = 1:00:00'
qmgr -c 'set queue default resources_default.nodes = 1'
qmgr -c 'set server default_queue = default'
qmgr -c 'set server submit_hosts = torque'
qmgr -c 'set server submit_hosts += jupyter'
qmgr -c 'set server submit_hosts += fireworks'
qmgr -c 'set server allow_node_submit = true'
qmgr -c 'set server disable_server_id_check = true'

# restart torque server and start scheduler
service torque-server restart
service torque-scheduler start
