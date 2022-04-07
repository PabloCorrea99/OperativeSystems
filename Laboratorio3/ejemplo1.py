from mpi4py import MPI
import sys

a = 5.0
b = 2.0

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

if n_ranks != 3:
    print('This program only works with 3 ranks')
    sys.exit(1)

if rank == 0:
    print(f'a = {a}, b = {b}')
    print(f'a - b = {a-b}')
if rank == 1:
    print(f'a + b = {a+b}')
if rank == 2:
    print(f'a * b = {a*b}')