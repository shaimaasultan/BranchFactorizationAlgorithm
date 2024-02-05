import logging
from logging.handlers import MemoryHandler
lg = logging.getLogger()
lg.setLevel(logging.INFO)
hnd = logging.FileHandler('simpolism.log',"w")
memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
hnd.setLevel(logging.INFO)
lg.addHandler(hnd)
import math
import  time
from datetime import datetime

def breakAt(A):
    if len(str(A)) < 3: 
        breakat = 100 * math.sqrt(A)
    elif len(str(A)) <= 16:
        breakat= A**(1/2)
    elif len(str(A)) <= 32:
        breakat= int(A**(1/3))
    else:
        breakat= A**(1/4)
    return breakat

'''
Get prime and composite primes between two numbers 
From : Start Number 
To : End Number
IncludNonePrime : flag to print None Primes in between the two numbers or not.
'''
def getPrimeAndCoPrime(From ,To , IncludNonePrime = False):
    for i in range(From , To) :
        b7 = (int(i)-1)/6
        b11 = (int(i)-5)/6
        if (str(int(b11))+'.0' == str(b11)):
            lg.info(' Prime or composite: A = {} in branch 11 at location {} '.format(i , b11))
        elif (str(int(b7))+'.0' == str(b7)):
            lg.info(' Prime or composite: A = {} in branch 7 at location = {}'.format(i , b7))
        elif IncludNonePrime :
            lg.info(' A = {} Is not Prime'.format(i))

'''
Get Prime Factors for Number A
'''
def getPrimeFactorsChain(A, l=[]):
    #lg.info(l)
    if A in l : return l
    for i in [2,3,5,7]:
        r = (A/i)
        if A%i == 0 : 
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i , r , A))
            if r not in l:
                l.append(r)
    i = 7
    breakat = breakAt(A)
    while i <= breakat > 0:
        i = i + 4
        r = (A/i)
        if (A%int(i) == 0 ):
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i, r  , A))
            if r not in l : 
                l.append(r)
            l = getPrimeFactorsChain(r, l)
        r = (A/(i+2))
        if (A%int(i+2) == 0 ):
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i+2, r  , A))
            if r not in l : 
                l.append(r)
            l = getPrimeFactorsChain(r , l)
        i = i + 2
        #if i <= 100 * math.sqrt(A) : break
    return l

'''
Get Prime First Factor for Number A for big number of digits
'''
def getFirstPrimeFactor(A):
    for i in [2,3,5,7]:
        if A%i == 0 : 
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i , (A/i) , A))
            return i
    i = 7
    
    if len(str(A)) < 3: 
        breakat = 100 * math.sqrt(A)
    else:
        breakat= A**(1/len(str(A)))
    lg.info(breakat)
    while i <= breakat  > 0:
        i = i + 4
        if (A%int(i) == 0 ):
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i, (A/i)  , A))
            return i
        if (A%int(i+2) == 0 ):
            lg.info('Factor {} = {} * {:.0f} = {}'.format(A ,i+2, (A/(i+2))  , A))
            return i
        i = i + 2
        #if i <= 100 * math.sqrt(A) : break
    return i

'''
Check if number Is Prime or Co Prime 
print the branch of the Prime 
print the position of the prime in the branch 
'''
def IsPrimOrCompositePrime(A):
    branch = 0
    b7 = (A-1)/6
    b11 = (A-5)/6
    lg.info('A = {}'.format(A))
    lg.info('b7 = {:.0f}'.format(b7))
    lg.info('b11 = {:.0f}'.format(b11))
    if ((A-5)%6 ==0):
        lg.info(' Prime or composite: A in branch 11 at location {:.0f} '.format(b11))
        branch = 11
    elif ((A-1)%6 == 0):
        branch = 7
        lg.info(' Prime or composite: A in branch 7 at location = {:.0f}'.format(b7))
    elif A%2 ==0 :
         lg.info(' multiplier of 2 : 2 * A = 2 * {:.0f} '.format((A/2) ))
    elif A%3 ==0 :
         lg.info(' multiplier of 3 : 3 * A = 3 * {:.0f} '.format((A/3) ))
    elif A%5 ==0 :
         lg.info(' multiplier of 5 : 5 * A = 5 * {:.0f} '.format((A/5) ))
    else:
        lg.info('Not in both branches (not in 7 and not in 11); not prime or composite prime; i.e. do not have at least one factor as (prime * prime)')

lg.info('==============================================')
start_T = time.time()
lg.info('Start Time {} {}'.format(start_T,datetime.now()))
lg.info('==============================================')
A = 7823748432522345
A = 1234567317729846283471394659252003451
A = 12345678910987654321
A = 12345678912333653845631
A = 7777777777772777777777777
#A = 2147375693
#A = 1234567891234
#A= 50922911074367
#A= 1234567940365983465019865019745216348999999913459182341878392721
#A= 12345679403659834650198655878392721
#A=6172836588649231
#A = 5844506355371
#A = 38164626500109928347598750814109268340817254817520856109465521348687151
lg.info('==============================================')
lg.info('Check if A = {} is a Prime or Composite Prime'.format(A))
lg.info('==============================================')
IsPrimOrCompositePrime(A)
#lg.info('==============================================')
#From = int(A-16)
#To = A
#IncludNonePrime = True
#lg.info('Get primes between A = {} & B = {}'.format(From , To))
#lg.info('==============================================')

#getPrimeAndCoPrime(From , To ,IncludNonePrime)
lg.info('==============================================')
Cutoff = 64
lg.info('A is number with {} Digits'.format(len(str(A))))
lg.info('Search for Factors up untill {}'.format(int(breakAt(A))))
if len(str(A)) <= Cutoff :
    lg.info('Get Factor Chain for A = {}'.format(A))
else:
    lg.info('Get First Factor for A = {}'.format(A))
lg.info('==============================================')

if len(str(A)) <=  Cutoff :
    getPrimeFactorsChain(A)
else:
    getFirstPrimeFactor(A)

lg.info('==============================================')
lg.info('{:.0f}'.format(2**30 * 3373243))
lg.info('{:.0f}'.format(2**30 * 2147375693))
lg.info('{:.0f}'.format(2**30 * 3373243 * 2147375693))
lg.info('{}'.format(1073741824 * 3373243 * 2147375693))
lg.info('{}'.format(A/2147375693))
lg.info('{}'.format((A/2147375693)/3373243))
lg.info('{}'.format((A/2147375693)/3373243/1073741824))
lg.info('{}'.format((A/3373243)))
lg.info('{}'.format((A/3373243)/2147375693))
lg.info('{}'.format((A/3373243)/2147375693/1073741824))
End_T = time.time()
lg.info('End Time {} {} ; Duration in sec {} ; Duration in minutes {}'.format(End_T,datetime.now() , End_T - start_T , (End_T - start_T)/60.0 ))
hnd.close()
