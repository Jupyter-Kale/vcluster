#!/usr/bin/env python

import socket
import docker

def main():
    cli = docker.from_env()
    id = open('/proc/1/cgroup', 'r').readlines()[0].strip().split('/')[-1]
    all_containers = cli.containers.list()
    this_container = [c for c in all_containers if c.id == id][0]
    service = this_container.labels["com.docker.compose.service"]
    project = this_container.labels["com.docker.compose.project"]
    number = this_container.labels["com.docker.compose.container-number"]

    # get torque hostname
    hostnames = []
    hostnames.append("{}_{}_{}".format(project, service, number))
    filters = [
        'com.docker.compose.project={}'.format(project),
        'com.docker.compose.service={}'.format('worker')
    ]
    worker_containers = cli.containers.list(filters={'label': filters})

    for c in worker_containers:
        number = c.labels["com.docker.compose.container-number"]
        hostname = "{}_{}_{}".format(project,'worker',number)
        hostnames.append(hostname)

    #with open('/etc/hosts', 'a') as torque_hosts:
    #    for h in hostnames:
    #        torque_hosts.write("{}\t{}.vcluster_default\n".format(socket.gethostbyname(h),h))

    with open('/var/spool/torque/server_priv/nodes', 'w') as torque_nodes_file:
        for h in hostnames[1:]:
            torque_nodes_file.write("{} np=1\n".format(h))

if __name__ == "__main__":
    main()
