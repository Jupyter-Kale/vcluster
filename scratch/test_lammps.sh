#!/usr/bin/env bash

mpirun.openmpi -n 4 lammps < /tmp/scratch/lammps_lj.txt
mpirun.openmpi -n 4 lammps < /tmp/scratch/lammps_eam.txt
mpirun.openmpi -n 4 lammps < /tmp/scratch/lammps_chain.txt
