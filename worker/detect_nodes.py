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

    hostnames = list()

    if service == 'master':
        hostnames.append("{}_{}_{}".format(project, service, number))
    else:
        filters = [
            'com.docker.compose.project={}'.format(project),
            'com.docker.compose.service={}'.format('master')
        ]
        master_container = cli.containers(filters={'label': filters})[0]
        service = master_container["Labels"]["com.docker.compose.service"]
        project = master_container["Labels"]["com.docker.compose.project"]
        number = master_container["Labels"]["com.docker.compose.container-number"]
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

    with open('/etc/opt/hosts', 'w') as mpi_hosts_file:
        for h in hostnames:
            mpi_hosts_file.write("{}\n".format(h))

if __name__ == "__main__":
    main()
