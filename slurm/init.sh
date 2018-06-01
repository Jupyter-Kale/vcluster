#!/usr/bin/env bash

# first record all available nodes
python /usr/local/bin/detect_nodes.py

# start slurm and munge
service slurmctld start
service slurmdbd start
