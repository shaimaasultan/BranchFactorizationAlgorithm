
'''
    Print all Prime number up untill N if N is prime.
    if N is not prime print "False Prime" and print its factors.
    Parameters:
        N = Natural number, to check if prime or not
        Prt = True or Flase, to print all prime numbers before N.
'''
import logging
from logging.handlers import MemoryHandler
import time
import math 
from datetime import datetime
lg = logging.getLogger()
lg.setLevel(logging.INFO)
hnd = logging.FileHandler('simpolism.log',"w")
memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
hnd.setLevel(logging.INFO)
lg.addHandler(hnd)


def sixlist (N):
    for i in range(1,N,3):
        lg.info('i = {} ; i/6 ={} ; {}'.format(i , i/6, 'i/6 - 1/6 =' +str(i/6 -1/6) if (i% 2 == 0) 
                                                             else 'i/6 +1/2 - 1/6 = i/6 + 2/6 = i/6 +1/3 ='+str(i/6 +1/3) ))

def halflist (N):
    for i in range(3,N,3):
        lg.info('i = {} ; i/6 ={}; {}'.format(i , i/6, 'i/6 - 1/2 =' +str(i/6 -1/2) if (i% 2 == 0) 
                                                             else ''))


def oneover12list (N):
    for i in range(2,N,3):
        lg.info('i = {} ; i/6 ={}; {}'.format(i , i/6, 'i/6 - 1/2 + 1/6 = i/6 - 2/6 = i/6 -1/3 =' +str(i/6 - 2/6) if (i% 2 != 0) 
                                                             else 'i/6 + 1/6 =' +str(i/6 +1/6) ))


'''
Function Call
'''
N = 130 #123456789123  #12345678907 #123456781 #12345678910987654321 #123456789123 #20209 #123456781 #123456691 #94 #125379
lg.info('==============================================')
lg.info('1 /6 List ')
lg.info('==============================================')
start_T = time.time()
lg.info('Start Time {} {}'.format(start_T,datetime.now()))
lg.info('==============================================')
sixlist(N)
lg.info('==============================================')
lg.info('1 /2 List ')
lg.info('==============================================')
halflist(N)
lg.info('==============================================')
lg.info('1 /2 List ')
lg.info('==============================================')
oneover12list(N)
End_T = time.time()
lg.info('End Time {} {} ; Duration in sec {} ; Duration in minutes {}'.format(End_T,datetime.now() , End_T - start_T , (End_T - start_T)/60.0 ))
hnd.close()

