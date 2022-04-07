from mpi4py import MPI
import sys

a = 5.0
b = 2.0
comm =  MPI.COMM_WORLD
rank = comm.Get_rank()
n_ranks = comm.Get_size()


if n_ranks != 3:
    print('This program only works with 3 ranks')
    sys.exit(1)

if rank == 0:
    prev_result = comm.recv(source=1)
    result = prev_result - a - b
    print(f'prev_result - a - b= {result} using rank:{rank}')
if rank == 1:
    prev_result = comm.recv(source=2)
    result =  a + b + prev_result
    comm.isend(result, dest=0)
    print(f'a + b + prev_result = {result} using rank:{rank}')
if rank == 2:
    result = a*b
    comm.isend(result, dest=1)
    print(f'a * b = {a*b} using rank:{rank}')