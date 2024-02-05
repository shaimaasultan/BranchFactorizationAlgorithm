import logging
from logging.handlers import MemoryHandler
lg = logging.getLogger()
lg.setLevel(logging.INFO)
hnd = logging.FileHandler('simpolism.log',"w")
memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
hnd.setLevel(logging.INFO)
lg.addHandler(hnd)

A = 12345678912333653845632
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('Type of A = {}'.format(type(A)))
lg.info('Type of B = {}'.format(type(A)))
lg.info('(A/2) * 2 = {}'.format((A/2) * 2 ))
lg.info('int value for A != (A/2) * 2 = {}'.format(int((A/2) * 2 )))
lg.info('A = (A * 1) = {}'.format(A * 1))
lg.info('int value for A != A * 1.0 = {}'.format(int(A * 1.0)))
lg.info('Type of A/B = {}'.format(type((A/B))))
lg.info(' A /1 != A/B = {}'.format(A/B))
lg.info('int value for A/B = {}'.format(int(A/B)))
lg.info('float Value for A/B = {}'.format(float(A/B)))
lg.info('str Value for A/B = {}'.format(str(A/B)))
from decimal import *
lg.info('Decimal value for A/B = {}'.format(Decimal(A/B)))
getcontext().prec = 28
lg.info('Decimal value for A/B = {}'.format(Decimal(A/B)))
lg.info('A * 2 = {}'.format(A* 2 ))
lg.info('(A/1 * 2) != (A/B) * 2 = {}'.format((A/B)* 2 ))
lg.info('int value for (A/B) * 2 = {}'.format(int((A/B)* 2 )))
lg.info('round(round(A,0)/B,0) = {:.0f}'.format(round(round(A,0)/B,0)))
lg.info('round(round(A,0)/round(B,0),0) = {:.0f}'.format(round(round(A,0)/round(B,0),0)))
lg.info('int value for (A * B**-1) ={}'.format(int(A * B**-1)))

lg.info('B**-1 ={}'.format(B**-1))


lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

A = 12345678912333653845639
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('(A + 678265) != A = {}'.format(A + 678265))
lg.info('(A - 678265) != A = {}'.format(A - 678265))

A = 12345678912333652
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))


lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info('math.sqrt(A)+1))/2 = {}'.format((((math.sqrt(A)+1))/2)))

lg.info('(((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1))  = {} '.format((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) ))

lg.info('int(math.sqrt(A)*A / math.sqrt(A))) = {}'.format(int(math.sqrt(A)*A / math.sqrt(A))))


A = 12345678912333654
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))

lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))

A = 12345678912333655
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))

A = 12345678912333658
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))


A = 12345678912333656
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))

A = 12345678912333657
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))


A = 12345678912333659
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) )

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))


A = 12345678912333654
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math

lg.info((((math.sqrt(A)+1))/2))

lg.info('D = 2 {}'.format((((math.sqrt(A)+1))/2) - (((A-1)/2) / (math.sqrt(A)+1)) ))

lg.info(int(math.sqrt(A)*A / math.sqrt(A)))

D = math.ceil(math.sqrt(A)/5)
R = (D - 4) /(2 * D)


lg.info((((math.sqrt(A)+1))/D) - (((A-1)/D) / (math.sqrt(A)+1))+R )


A = 12345678912333653845632384283483572489237528348737
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
lg.info('int((A/B) * 1.0) = {}'.format(int((A/B) * 1.0)))
lg.info('A-int((A/B) * 1.0) = {} '.format(A-int((A/B) * 1.0)))

lg.info('int((A/B) * 1.0 + 1) ={}'.format(int((A/B) * 1.0 + 1)))
lg.info('int((A/B) * 1.0 - 1) = {}'.format(int((A/B) * 1.0 - 1)))

lg.info('int((A/B) * 1.0)+ 1.0 = {} '.format(int((A/B) * 1.0)+ 1.0))
lg.info('int((A/B) * 1.0)- 1.0 ={}'.format(int((A/B) * 1.0)- 1.0))

lg.info('int((A/B) * 1.0)+ 5.0 = {} '.format(int((A/B) * 1.0)+ 5.0))
lg.info('int((A/B) * 1.0)- 5.0 = {}'.format(int((A/B) * 1.0)- 5.0))

lg.info('int((A/B) * 1.0)+ 4.0 = {} '.format(int((A/B) * 1.0)+ 4.0))
lg.info('int((A/B) * 1.0)- 4.0 = {}'.format(int((A/B) * 1.0)- 4.0))

lg.info('int((A/B) * 1.0)+ 3.0 = {}' .format(int((A/B) * 1.0)+ 3.0))
lg.info('int((A/B) * 1.0)- 3.0 = {}'.format(int((A/B) * 1.0)- 3.0))

lg.info('int((A/B) * 1.0)+ 6.0 = {} '.format(int((A/B) * 1.0)+ 6.0))
lg.info('int((A/B) * 1.0)- 6.0 = {}'.format(int((A/B) * 1.0)- 6.0))

import math
A = 996576353487258763453463434548237548241123450796857465342335678909776123428790876432147897324167867398675313422354786987563313658796753646374656858973631264357846735241326345847356214352345487356245132364
B = 1
lg.info('A = {}'.format(A))
lg.info('B = {}'.format(B))
sqrtA = math.sqrt(A)
lg.info('((sqrt(A)+1)/2) ={}'.format(((sqrtA+1)/2)))
D =2
lg.info('Equation (1) D = {}  & ((sqrtA+1)/D) - (((A-1)/D) / (sqrtA+1))= {}'.format(D ,((sqrtA+1)/D) - (((A-1)/D) / (sqrtA+1)) ))

lg.info('A != int(sqrtA * A / sqrtA) = {}'.format(int(sqrtA * A / sqrtA)))

N = math.sqrt(A)+1.0
D = math.ceil(math.sqrt(A)/5) 
R =  (D - 4) /(2 * D)
S = (A-1) /D
lg.info('N = math.sqrt(A)+1.0 = {}'.format(N))  
lg.info('D = math.ceil(math.sqrt(A)/5.0)  = {}'.format(D))
lg.info('R = (D - 4) /(2 * D) = {}'.format(R))
lg.info('S = (A-1) /D'.format(S))

lg.info('Equation (2) = ((N/D) - (S /N)+R)) = {}'.format(((N/D) - (S /N)+R)))
lg.info('Equation (2) = round(((N/D) - (S /N)+R)) , 2) = {}'.format(round((N/D) - (S /N)+R,2)))



