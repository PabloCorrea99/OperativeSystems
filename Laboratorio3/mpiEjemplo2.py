from mpi4py import MPI                                         
import numpy as np                                             
                                                               
comm = MPI.COMM_WORLD                                          
rank = comm.Get_rank()                                         
size = comm.Get_size()                                         
                                                               
if rank == 0:                                                                       
    for i in range(0,10):
        comm.isend(i, dest=1, tag=11)                           
        print("process {} immediate send {}...".format(rank, i))
else:                                                          
    data = comm.recv(source=0, tag=11)                         
    print("process {} recv {}...".format(rank, data)) 
    
MPI.Finalize()
