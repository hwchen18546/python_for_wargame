#!/usr/bin/env python 
from z3 import *

# declare
s = []
s.append(Int('s[0]'))
s.append(Int('s[1]'))
s.append(Int('s[2]'))
s.append(Int('s[3]'))
s.append(Int('s[4]'))
s.append(Int('s[5]'))
s.append(Int('s[6]'))
s.append(Int('s[7]'))
s.append(Int('s[8]'))
s.append(Int('s[9]'))
s.append(Int('s[10]'))
s.append(Int('s[11]'))
s.append(Int('s[12]'))
s.append(Int('s[13]'))
s.append(Int('s[14]'))
s.append(Int('s[15]'))
s.append(Int('s[16]'))
s.append(Int('s[17]'))
s.append(Int('s[18]'))
s.append(Int('s[19]'))

solver = Solver()

# add constraint 0~9
for i in range(0, 20):
    solver.add(s[i] >= 0)    
    solver.add(s[i] < 10)

# add challenge constraint
solver.add(s[15] + s[4] == 10)
solver.add(s[1] * s[18] == 2)
solver.add(s[15] / s[9] == 1)
solver.add(s[17] - s[0] == 4)
solver.add(s[5] - s[17] == -1)
solver.add(s[15] - s[1] == 5)
solver.add(s[1] * s[10] == 18)
solver.add(s[8] + s[13] == 14)
solver.add(s[18] * s[8] == 5)
solver.add(s[4] * s[11] == 0)
solver.add(s[8] + s[9] == 12)
solver.add(s[12] - s[19] == 1)
solver.add(s[9] % s[17] == 7)
solver.add(s[14] * s[16] == 40)
solver.add(s[7] - s[4] == 1)
solver.add(s[6] + s[0] == 6)
solver.add(s[2] - s[16] == 0)
solver.add(s[4] - s[6] == 1)
solver.add(s[0] % s[5] == 4)
solver.add(s[5] * s[11] == 0)
solver.add(s[10] % s[15] == 2)
solver.add(s[11] / s[3] == 0)
solver.add(s[3] != 0)
solver.add(s[14] - s[13] == -4)
solver.add(s[18] + s[19] == 3)

print solver.check()
print solver.model()
