import logging
from logging.handlers import MemoryHandler
lg = logging.getLogger()
lg.setLevel(logging.INFO)
hnd = logging.FileHandler('simpolism.log',"w")
memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
hnd.setLevel(logging.INFO)
lg.addHandler(hnd)
import math
#A = 214032465024074496126442307283933356300861471514475501779775492088141802344714013664334551909580467961099285187247091458768739626192155736304745477052080511905693106687691590019759405693457452230589325976697471681738069364894699871578494975937497937
A = 1234567

b7 = (A-1)/6
b11 = (A-5)/6
lg.info('A = {}'.format(A))
lg.info(math.sqrt(A))
if (str(int(b11))+'.0' == str(b11)):
    lg.info(' Prime or composite: A in 11 branch at location {} '.format(b11))
elif (str(int(b7))+'.0' == str(b7)):
    lg.info(' Prime or composite: A in 7 branch at location = {}'.format(b7))
else:
    lg.info(' A Is not Prime')
lg.info('A % 3 = {}'.format(A%3))
lg.info('A % 5 = {}'.format(A%5))
lg.info('A % 2 = {}'.format(A%2))
lg.info(' A / b7 = {}'.format(A/b7))
lg.info(' A / b11 = {}'.format(A/b11))
lg.info(' b7 = {}'.format((b7-5)/6))

i = 7
while A%i > 0:
    i = i + 6
    #lg.info(i)
lg.info('First factor = {} * {} = {}'.format(i , int(A/i) , i * int(A/i)))

