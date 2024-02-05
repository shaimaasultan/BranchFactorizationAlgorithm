
import sys
from decimal import *
print(getcontext())
print(sys.float_info)
print(Decimal(-7).remainder_near(Decimal(4)))