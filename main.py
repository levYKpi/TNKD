#######################################################################################################################
############ FUNCTIONS ################################################################################################
############ BINLST = D1, D2, D3, D6, D8, C1, C2, C4, C5, C6, B1, B2, B4, B5, M1, M2, A1, A2, Pr1, Pr2, Pr3, Pr5, Pr6 #
############           0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17   18   19   20   21   22 #

def aFun(binLst):
    D6 = binLst[3]
    C4 = binLst[7]
    B2 = binLst[11]
    Pr2, Pr3 = binLst[19], binLst[20]
    result = D6 and C4 and B2 and (Pr2 or Pr3)
    return result


def bFun(binLst):
    D8 = binLst[4]
    C5, C6 = binLst[8], binLst[9]
    B1, B2, B4 = binLst[10], binLst[11], binLst[12]
    M1, M2 = binLst[14], binLst[15]
    A1, A2 = binLst[16], binLst[17]
    Pr1, Pr5, Pr6 = binLst[18], binLst[21], binLst[22]
    result = D8 and (C5 or C6) and B4 and (Pr5 or Pr6 or A2 and (M1 or M2) and A1 and (B1 or B2) and Pr1)
    return result


def cFun(binLst):
    D1, D2 = binLst[0], binLst[1]
    C1 = binLst[5]
    B1, B2 = binLst[10], binLst[11]
    Pr1, Pr2 = binLst[18], binLst[19]
    result = D1 and D2 and C1 and (B1 or B2) and (Pr1 or Pr2)
    return result


def dFun(binLst):
    D2, D3 = binLst[1], binLst[2]
    C2 = binLst[6]
    B1, B2 = binLst[10], binLst[11]
    Pr1, Pr2, Pr3 = binLst[18], binLst[19], binLst[20]
    result = D2 and D3 and C2 and (B1 or B2) and (Pr1 or Pr2 or Pr3)
    return result