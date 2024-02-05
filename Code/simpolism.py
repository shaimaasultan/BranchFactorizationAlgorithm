
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
def isPrime(N):
    Flg = False
    if N in [2,3,5] : return True
    if N % 2 == 0 or N % 3 ==0 or N % 5 == 0 : 
        return False
    for i in range(1 , N+1, 6):
        if str(i)[-1] == str(5) : continue
        #if Prt == True : print(str(i) + " "+ str(i+10), sep=" ")
        if i > 0 and ( N == i or N == i+10 or (N < i and N % i == 0) or (N < i and N % (i+10) == 0 )):
                Flg = True
                break
        if i > 1 and N > i and N % i == 0 :
            Flg = False
            break
    return Flg
      
def Fact(N):
    Flg = False
    lg.info('2' if N % 2 == 0 else '3' if N % 3 == 0 else '5' if N % 5 == 0 else '')
    for i in range(1 , N+1, 6):
        if i > 1 and N > i and N % i == 0 :
            lg.info(i)
            Flg = True
           
        if  N > (i+10) and (N % (i+10)) == 0 :
            lg.info(i+10)
            Flg = True
    return Flg

def PrimesBefore(N):
    Flg = False
    if math.sqrt(N) in [2,3,5,11]:
        lg.info(int(math.sqrt(N))) 
    elif N in [2,3,5,11]: 
        lg.info(N) 
   
    for i in range(1 , N+1, 6):
        if str(i)[-1] == str(5) : continue
        
        if (( N % i != 0) or N ==i) :
            lg.info(str(i))
        if (( N % (i+10) != 0) or N == (i+10)) :
            lg.info(str(i+10))
    return Flg
def IsPrimeBefore(N):
    Flg = False
    if N in [2,3,5] : 
        lg.info(N) 
        Flg = True
    if N % 2 == 0 or N % 3 ==0 or N % 5 == 0 : 
        Flg = False
    for i in range(1 , N+1, 6):
        if str(i)[-1] == str(5) : 
            Flg=False
            continue
        #if Prt == True : print(str(i) + " "+ str(i+10), sep=" ")
        if i > 0 and ( N == i or N == i+10 or (N < i and N % i == 0) or (N < i and N % (i+10) == 0 )):
                Flg = True
        if i > 1 and N > i and N % i == 0 :
            Flg = False
        if(Flg == False):
            lg.info(' {} {} '.format(i , i+10) )
           
    return Flg
def PrimeStat(N):
    count0 = 0 
    count1 = 0
    
    for k in [1 ,11] :
        for i in range(k, N+1 , 6):
            fact = False
            if str(i)[-1] == str(5) : 
                continue
        
            for j in range(k,N+1 , 6):
                if str(j)[-1] == str(5) : 
                    continue
                if( i> 1 and j > 1 and i != j and ((j % i) == 0 or (i % j) ==0) ) :
                    count1 = count1 + 1
                    lg.info('Composit prime # {} to exclude | {} = {} {} {} ' .format(count1 , i , j , '/' if (i < j) else '*', (j / i) if (j > i) else (i/j)))
                    fact = True

            if (fact == False) : 
                count0 = count0 + 1
                lg.info('ID = {} | Prime Number = {}'.format(count0 , i))
    return

def PrimeAndCompositList(N):
    count0 = 0 
    count1 = 0
    count2 = 0
    count3 = 0
    for k in [1 ,11] :
        for i in range(k, N+1 , 6):
            fact = False
            if str(i)[-1] == str(5) : 
                continue
            count3 = count3+1
            count1 = 0
            count2 = (count2 + 1) 
            for j in range(k,i+6 , 6):
                if str(j)[-1] == str(5) : 
                    continue
                if( i> 1 and j > 1 and i > j and  (i % j) ==0)  :
                    count1 = count1 + 1
                     
                    lg.info('{} Is Composit prime ID = {}, Composite # {} to exclude | {} = {} {} {} ' .format( i,count2-count0 ,count1 , i , j , '*',  (i/j)))
                    fact = True
                
                    

            if (fact == False) : 
                count0 = count0 + 1
                lg.info('ID = {} | Prime Number = {}'.format(count0 , i))
    lg.info('==============================================')
    lg.info('Total of {} Numbers To check'.format(count3))
    lg.info('Total of {} Primes'.format(count0))
    lg.info('% Numbers To Check up to N {} = {}% '.format(N , round((count3 / N) * 100.0 ,2 )))
    lg.info('% Primes up to N {} from {} Numbers To check= {}% '.format(N , count3, round((count0 / count3) * 100.0 ,2 )))
    lg.info('==============================================')

                


def PrimeList(N):
    count0 = 0 
    count3 = 0
    for k in [1 ,11] :
        for i in range(k, N+1 , 6):
            fact = False
            if str(i)[-1] == str(5) : 
                continue
            count3 = count3+1
            for j in range(k,N+1 , 6):
                if str(j)[-1] == str(5) : 
                    continue
                if( i> 1 and j > 1 and i > j and  (i % j) ==0)  :
                    fact = True
          
            if (fact == False) : 
                count0 = count0 + 1
                lg.info('ID = {} | Prime Number = {}'.format(count0 , i))

    lg.info('==============================================')
    lg.info('Total of {} Numbers To check'.format(count3))
    lg.info('Total of {} Primes'.format(count0))
    lg.info('% Numbers To Check up to N {} = {}% '.format(N , round((count3 / N) * 100.0 ,2 )))
    lg.info('% Primes up to N {} from {} Numbers To check= {}% '.format(N , count3, round((count0 / count3) * 100.0 ,2 )))
    lg.info('==============================================')
        
    return

def Prime(N, L = True):
    count0 = 0 
    count1 =0
    count2 =0
    count3 = 0
    if N in [2,3,5] : return True
    if N % 2 == 0 or N % 3 ==0 or N % 5 == 0 : 
        return False
    for k in [1 ,11] :
        for i in range(k, N+1 , 6):
            fact = False
            if str(N)[-1] == str(5) : 
                return False 
            if str(i)[-1] == str(5) : 
                continue 
            count3 = count3+1
            count1 = 0
            count2 = (count2 + 1) 
            for j in range(k,i+6, 6):
                if str(j)[-1] == str(5) : 
                    continue
                if(i> 1 and j > 1 and (i> j and i % j==0) ):
                    fact = True
                if(i> 1 and j > 1 and( (N> i and N % i==0) or (N>j and N % j ==0) )):
                    fact = True
                    lg.info('{} Is Composit prime ID = {}, Composite # {} to exclude | {} = {} {} {} ' .format( N,count2-count0 ,count1 , N , i , '*',  (N/i)))
                    return False
          
            if (fact == False and L == True) : 
                count0 = count0 + 1
                lg.info('ID = {} | Prime Number = {}'.format(count0 , i))
            
    return True


def Factor(N):
    f = [N]
    for j in [2,3,5]:
         if(j in f) : break
         if ((N%j) == 0) :
                lg.info('{} | {} = {} {} {} ' .format( N, N , j , '*',(N/j)))
                f.append(j)
                f.append((N/j))
    for k in [1,11]:
        i = k
        end = int(math.sqrt(N))
        while (i <= end):
            if((i%5 != 0) and  (N % i) == 0):
                lg.info('{} | {} = {} {} {} ' .format( N, N , i , '*',(N/i)))
                f.append(i)
                f.append((N/i))
            '''if((i%3) == 0):
                lg.info('{} | {} = {} {} {} ' .format( N, N , i , '*',(i/3)))
                f.append(i)
                f.append((i/3))
            '''
            i = i + 6     
            #if( i in f) :  break 
    
    for i in f:
        for j in f:
            if (i != j and (N % (i/j)) == 0 and (i/j) not in f) :
                f.append(((i / j)))
                lg.info('{} | {} = {} {} {} ' .format( N, j , i , '*',i/j))
    lg.info(f)
    '''for i in range(k, M+1 , 6):
                if(i == 1): continue
                if(i in f) : break
                if((N%i) == 0) :
                    lg.info('{} | {} = {} {} {} ' .format( N, N , i , '*',(N/i)))
                    f.append(i)
                    f.append((N/i))
                    M = int(N/i)
                lg.info(i)
    '''
    




'''
Function Call
'''
N = 123456789123  #12345678907 #123456781 #12345678910987654321 #123456789123 #20209 #123456781 #123456691 #94 #125379
lg.info('==============================================')
lg.info('Check if N = {},  Is  Prime and its factors.'.format(N))
lg.info('==============================================')
start_T = time.time()
lg.info('Start Time {} {}'.format(start_T,datetime.now()))
lg.info('==============================================')
#lg.info(' Is {} Prime ? {}'.format(N,'YES' if (Prime(N)) else 'NO' ))
#PrimeList(N)
Factor(N)
#PrimeAndCompositList(N)
#lg.info(' Is {} Prime ? {}'.format(N,'YES' if (IsPrimeBefore(N)) else 'NO' ))
#lg.info(' Is {} Prime ? {}'.format(N,'YES' if (isPrime(N)) else 'NO' ))
lg.info('==============================================')
lg.info(' Factors of {}'.format(N))
lg.info('==============================================')
#Factors = Fact(N)
lg.info('==============================================')
#lg.info(' Primes Up Until {} {}'.format(N , Factors))
lg.info('==============================================')
#if (Factors == False) : PrimesBefore(N)
End_T = time.time()
lg.info('End Time {} {} ; Duration in sec {} ; Duration in minutes {}'.format(End_T,datetime.now() , End_T - start_T , (End_T - start_T)/60.0 ))
hnd.close()

