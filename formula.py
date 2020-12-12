import numpy

Q = [0.000022, 0.000022, 0.000022, 0.000022, 0.000022, 0.000022, 0.00041, 0.00041, 0.00041, 0.000015, 0.000015, 0.000015, 0.000015, 0.00036, 0.00036, 0.00041, 0.00041, 0.00012, 0.00012,  0.00012, 0.00012, 0.00012, 0.00012, 0.00012]
lst = [0, 1, 1, 0, 0, 1,0, 1, 0, 1, 1, 1 , 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
BINLST = [
    'D1', 'D2', 'D3', 'D6', 'D8', 'C1', 'C2', 'C4', 'C5', 'C6', 'B1', 'B2', 'B4', 'B5', 'M1', 'M2', 'A1', 'A2',
    'Pr1', 'Pr2', 'Pr3', 'Pr5', 'Pr6'
]
Dlist = dict(zip(BINLST, list(range(23))))
print( lst[Dlist['Pr1']] )
i = 0
for i in range (23):
    P=numpy.prod(lst[i]*Q[i]+(1-lst[i])*(1-Q[i]))
print(P)