
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

def Factor(N , f):
    for j in [2,3,5]:
         if(j in f) : break
         if ( (N%j) == 0 and int(N/j) not in f) :
                lg.info('{} | {} = {} {} {} ' .format( N, N , j , '*',int(N/j)))
                f.append(j)
                f.append(int(N/j))
    for k in [1,11]:
        i = k
        end = int(math.sqrt(N))
        while (i <= end):
            if((i%5 != 0) and i > 1 and  (N % i) == 0 and  int(N/i) not in f ):
                lg.info('{} | {} = {} {} {} || Ratio = {} ' .format( N, N , i , '*',int(N/i), int((N/i)/i)))
                f.append(i)
                f.append(int(N/i))
            i = i + 6   
            if(int(N/i) <=  100 * end) :  break 
        
    
    for i in f:
        for j in f:
            if (j in [2,3,5]) : continue
            if (i != j and i/j > 1 and (N % (i/j)) == 0  and int(i/j) not in f) :
                f.append((int(i / j)))
                lg.info('{} | {} = {} {} {}' .format( i, i , j , '*',int(i/j)))
    
    
    return f

'''
Function Call
'''
N = 123456789123336538456318 #316169745218939 #50922911074367 #316169745218939 #12345678912333653845631 #123456789123379313  #12345678907 #123456781 #12345678910987654321 #123456789123 #20209 #123456781 #123456691 #94 #125379
lg.info('==============================================')
lg.info('Check if N = {},  Is  Prime and its factors.'.format(N))
lg.info('==============================================')
start_T = time.time()
lg.info('Start Time {} {}'.format(start_T,datetime.now()))
lg.info('==============================================')
lg.info(' Factors of {} ; for number with {} digits'.format(N , len(str(N))))
lg.info('==============================================')
#lg.info('{} {}'.format(int(math.sqrt(N)) , 100 * int(math.sqrt(N)) ))
f =[]
f = Factor(N ,f)
lg.info(f)
r= f.copy()
while len(f) > 0 :
    p = f.pop()
    if p not in r: 
        r.append(p)
    if (str(p)[-1]== '1' or str(p)[-1]== '3' or str(p)[-1]== '7' or str(p)[-1]== '9' ) : 
        f = Factor(p,f)
    if p in f :
        f.remove(p)
lg.info(r)
lg.info('==============================================')

End_T = time.time()
lg.info('End Time {} {} ; Duration in sec {} ; Duration in minutes {}'.format(End_T,datetime.now() , End_T - start_T , (End_T - start_T)/60.0 ))
hnd.close()


    
