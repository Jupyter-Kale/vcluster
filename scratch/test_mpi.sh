#!/usr/bin/env bash

#PBS -l ncpus=2
#PBS -l walltime=00:01:00
#PBS -N testmpi
#PBS -V
cd $PBS_O_WORKDIR

mpicc /tmp/scratch/mpi_hello.c
mpirun /tmp/scratch/mpi_hello >> /tmp/scratch/test_mpi.out

