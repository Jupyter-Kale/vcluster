#!/usr/bin/env python

import os
import docker

def main():
    cli = docker.Client(base_url='unix://var/run/docker.sock')
    id = open('/proc/1/cgroup', 'r').readlines()[0].strip().split('/')[-1]
    all_containers = cli.containers()
    this_container = [c for c in all_containers if c["Id"] == id][0]
    service = this_container["Labels"]["com.docker.compose.service"]
    project = this_container["Labels"]["com.docker.compose.project"]
    number = this_container["Labels"]["com.docker.compose.container-number"]

    hostnames = []
    hostnames.append("{}_{}_{}".format(project, service, number))
    filters = [
        'com.docker.compose.project={}'.format(project),
        'com.docker.compose.service={}'.format('worker')
    ]
    worker_containers = cli.containers(filters={'label': filters})

    for c in worker_containers:
        project = c["Labels"]["com.docker.compose.project"]
        service = c["Labels"]["com.docker.compose.service"]
        number = c["Labels"]["com.docker.compose.container-number"]
        hostname = "{}_{}_{}".format(project,service,number)
        hostnames.append(hostname)

    with open('/etc/hosts', 'a') as torque_hosts:
        for h in hostnames:
            torque_hosts.write("{}\n".format(h))

    with open('/var/spool/torque/server_priv/nodes', 'w') as torque_nodes_file:
        for h in hostnames[1:]:
            torque_nodes_file.write("{} np=1\n".format(h))

if __name__ == "__main__":
    main()
