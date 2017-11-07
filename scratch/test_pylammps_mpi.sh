#!/usr/bin/env bash

#PBS -l ncpus=4
#PBS -l walltime=00:01:00
#PBS -N testmpi
#PBS -V
cd $PBS_O_WORKDIR

mpirun -np 4 python /tmp/scratch/test_pylammps_mpi.py

