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

lg.info('==============================================')
start_T = time.time()
lg.info('Start Time {} {}'.format(start_T,datetime.now()))
lg.info('==============================================')
#A = 214032465024074496126442307283933356300861471514475501779775492088141802344714013664334551909580467961099285187247091458768739626192155736304745477052080511905693106687691590019759405693457452230589325976697471681738069364894699871578494975937497937
A = 1234567940365983465019865019745216348999999913459182341878392721
#A = 1331
#A = 12345673177298462  
#A = 12345673177298462 -3
#A = 12345673177298462 -1
#A = 12345673939932462364578187
branch = 0
b7 = (A-1)/6
b11 = (A-5)/6
lg.info('A = {}'.format(A))
lg.info('{:.8f}'.format(math.sqrt(A)))
if (str(int(b11))+'.0' == str(b11)):
    lg.info(' Prime or composite: A in branch 11 at location {} '.format(b11))
    branch = 11
elif (str(int(b7))+'.0' == str(b7)):
    branch = 7
    lg.info(' Prime or composite: A in branch 7 at location = {}'.format(b7))
else:
    lg.info(' i Is not Prime')
lg.info('==============================================')
'''for i in range(1 , A):
    b7 = (int(i)-1)/6
    b11 = (int(i)-5)/6
    #lg.info('i = {}'.format(i))
    #lg.info(math.sqrt(i))
    if (str(int(b11))+'.0' == str(b11)):
        lg.info(' Prime or composite: A = {} in 11 branch at location {} '.format(i , b11))
        #branch = 11
    elif (str(int(b7))+'.0' == str(b7)):
        #branch = 7
        lg.info(' Prime or composite: A = {} in 7 branch at location = {}'.format(i , b7))
    #else:
    #    lg.info(' i Is not Prime')
'''
lg.info('==============================================')
lg.info('A % 3 = {}'.format(A%3))
lg.info('A % 5 = {}'.format(A%5))
lg.info('A % 2 = {}'.format(A%2))
lg.info(' A / b7 = {}'.format(A/b7))
lg.info(' A / b11 = {}'.format(A/b11))
lg.info(' b7 = {}'.format(b7))
lg.info(' b11 = {}'.format(b11))
lg.info('branch = {}'.format(branch))
#lg.info(A/3)


for i in [2,3,5]:
    if A%i == 0 : 
        lg.info('First factor = {} * {:.0f} = {}'.format(i , (A/i) , A))
    
i=7
if branch in [11,7]: 
    while A%int(i) > 0:
        i = i + 4
        if (A%int(i) == 0): break
        i = i + 2
    #lg.info(i)

if  i * int(A/i) == A : 
    lg.info('First factor = {} * {:.0f} = {}'.format(i , (A/i) , A))

lg.info('==============================================')

End_T = time.time()
lg.info('End Time {} {} ; Duration in sec {} ; Duration in minutes {}'.format(End_T,datetime.now() , End_T - start_T , (End_T - start_T)/60.0 ))
hnd.close()
