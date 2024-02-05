import logging
from logging.handlers import MemoryHandler
lg = logging.getLogger()
lg.setLevel(logging.INFO)
hnd = logging.FileHandler('simpolism.log',"w")
memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
hnd.setLevel(logging.INFO)
lg.addHandler(hnd)

A = 12384723
ben = list([2,3,5]) + list(range(1 ,A ,6))   
l=ben.copy()
l.reverse()
S = []
while len(l)> 0:
    i = l.pop()
    li = range(i+10,A,i+10)
    Np = filter(lambda N : N in li , l)
    S = S + list(Np)

    if i == 1 : continue

    li = range(i,A,i)
    Np = filter(lambda N : N in li , l)
    S = S + list(Np)

    
R = filter(lambda N : N  not in S , ben)
R1 = list(R)
R = filter(lambda N : N  not in S , ben)
R2 = list([e +10 for e in R if e not in [2,5]])
print('not Prime List = S = {}'.format(list(S)))
print('Prime List = R = {}'.format( list(R1) + list(R2)))
