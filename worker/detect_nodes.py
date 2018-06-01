#!/usr/bin/env python

import docker

def main():
    cli = docker.from_env()
    id = open('/proc/1/cgroup', 'r').readlines()[0].strip().split('/')[-1]
    all_containers = cli.containers.list()
    this_container = [c for c in all_containers if c.id == id][0]
    project = this_container.labels["com.docker.compose.project"]

    filters = [
        'com.docker.compose.project={}'.format(project),
        'com.docker.compose.service={}'.format('worker')
    ]
    worker_containers = cli.containers.list(filters={'label': filters})

    hostnames = list()
    for c in worker_containers:
        number = c.labels["com.docker.compose.container-number"]
        hostname = "{}_{}_{}".format(project,'worker',number)
        hostnames.append(hostname)

    with open('/etc/opt/hosts', 'w') as mpi_hosts_file:
        for h in hostnames:
            mpi_hosts_file.write("{}\n".format(h))

if __name__ == "__main__":
    main()
