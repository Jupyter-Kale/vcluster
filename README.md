# Kale dev/test docker compose environment

This is a docker compose virtual cluster for Kale dev/test scenarios where we want to simulate an HPC environment.

Containers
- Docker registry for local images
- Jupyter Notebook Server (using Jupyter docker scipy-notebook base image)
- Workers (scale up/down with docker-compose command)
- Torque (MOM daemons run on workers)
- SLURM
- Mongo (using docker mongo base image)
- Fireworks

## Quickstart
### Bringing up the virtual cluster
    # generate the ssh keys used for connecting machines in the cluster
    python gen_sshkeys.py
    # build the docker images
    docker-compose build
    # start the containers
    docker-compose up -d
### Shutting down the virtual cluster
    docker-compose down
### Specifying number of workers (default is 4)
    # shut down before changing number of workers, will not be dynamically detected and handled by the cluster
    docker-compose up --scale worker=4 -d
### Accessing the Jupyter Notebook Server
    http://localhost:18888
### Accessing the Jupyter container directly
    docker-compose exec jupyter bash
### Using local kale development files
    export KALE_SRC=<full_path/to/your/git/clone>
    docker-compose up -d
    docker-compose exec jupyter bash
    
    cd /opt/kale
    pip install -e .
    # OR after each code update
    pip install . -U
### Accessing a worker directly (specify index when multiple workers running)
    docker-compose exec --index=1 worker bash
