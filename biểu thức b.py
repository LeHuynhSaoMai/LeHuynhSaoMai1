# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:19:43 2024

@author: User
"""

import math
a = float(input("Số thực a = "))
b = float(input("Số thực b = "))
print("A = ", round(32**0.2-(1/64)**(-0.25)+(8/27)**(1/3),4))
x = (math.sqrt(a)-math.sqrt(b))/(math.sqrt(math.sqrt(a))-math.sqrt(math.sqrt(b)))
y = (math.sqrt(a) + math.sqrt(math.sqrt(a*b)))/(math.sqrt(math.sqrt(a))+math.sqrt(math.sqrt(b)))
print("Gía trị biểu thức: ",round(x-y,0))