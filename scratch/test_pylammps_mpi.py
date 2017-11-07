#!/usr/bin/env python

from mpi4py import MPI
from lammps import PyLammps

L = PyLammps()
L.file("in.melt")

if MPI.COMM_WORLD.rank == 0:
    print("Potential energy: ", L.eval("pe"))

MPI.Finalize()
