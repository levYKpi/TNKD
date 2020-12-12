#######################################################################################################################
############ FUNCTIONS ################################################################################################
############ BINLST = D1, D2, D3, D6, D8, C1, C2, C4, C5, C6, B1, B2, B4, B5, M1, M2, A1, A2, Pr1, Pr2, Pr3, Pr5, Pr6 #
############           0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17   18   19   20   21   22 #
from table import create_table as ct

BINLST = [
    'D1', 'D2', 'D3', 'D6', 'D8', 'C1', 'C2', 'C4', 'C5', 'C6', 'B1', 'B2', 'B4', 'B5', 'M1', 'M2', 'A1', 'A2',
    'PR1', 'PR2', 'PR3', 'PR5', 'PR6'
]
Dlist = dict(zip(BINLST, list(range(23))))
Table = ct()

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


def Funk(lst):
    ret = aFun(lst) * bFun(lst) * cFun(lst) * dFun(lst)
    return ret


def vectorGenerator(target, zeros, result = None):
    pack = []

    def subPackGenerator(target, result):
        used = []
        for i, item in enumerate(target):
            if item != 0 and i not in used:
                newPack = target.copy()
                newPack[i] = 0
                if newPack not in result:
                    result.append(newPack)
                used.append(i)

    if result:
        for subPack in result:
            subPackGenerator(subPack, pack)
    else:
        subPackGenerator(target, pack)

    return pack if zeros == 1 else vectorGenerator(target, zeros-1, pack)


def pick_proc_PR1(Tmax, Tcurrent):
    if Tcurrent[2] + 20 <= Tmax[2]:
        Tcurrent[2] += 20
    elif Tcurrent[1] + 10 <= Tmax[1] and Tcurrent[3] + 10 <= Tmax[3]:
        Tcurrent[1] += 10
        Tcurrent[3] += 10
    elif Tcurrent[3] + 10 <= Tmax[3] and Tcurrent[4] + 10 <= Tmax[4]:
        Tcurrent[3] += 10
        Tcurrent[4] += 10
    elif Tcurrent[1] + 10 <= Tmax[1] and Tcurrent[4] + 10 <= Tmax[4]:
        Tcurrent[1] += 10
        Tcurrent[4] += 10
    else:
        Tcurrent[0] *= -1
    return Tcurrent


def pick_proc_PR2(Tmax, Tcurrent):
    if Tcurrent[0] + 40 <= Tmax[0]:
        Tcurrent[0] += 40
    elif Tcurrent[2] + 40 <= Tmax[2]:
        Tcurrent[2] += 40
    else:
        Tcurrent[1] *= -1
    return Tcurrent


def pick_proc_PR3(Tmax, Tcurrent):
    if Tcurrent[0] + 50 <= Tmax[0]:
        Tcurrent[0] += 50
    elif Tcurrent[1] + 50 <= Tmax[1]:
        Tcurrent[1] += 50
    else:
        Tcurrent[2] *= -1
    return Tcurrent

def pick_proc_PR5(Tmax, Tcurrent):
    if Tcurrent[0] + 50 <= Tmax[0] and Tcurrent[1] + 20 <= Tmax[1]:
        Tcurrent[0] += 50
        Tcurrent[1] += 20
    elif Tcurrent[2] + 50 <= Tmax[2] and Tcurrent[1] + 20 <= Tmax[1]:
        Tcurrent[2] += 50
        Tcurrent[1] += 20
    elif Tcurrent[0] + 50 <= Tmax[0] and Tcurrent[4] + 20 <= Tmax[4]:
        Tcurrent[0] += 50
        Tcurrent[4] += 20
    elif Tcurrent[2] + 50 <= Tmax[2] and Tcurrent[4] + 20 <= Tmax[4]:
        Tcurrent[2] += 50
        Tcurrent[4] += 20
    else:
        Tcurrent[3] *= -1
    return Tcurrent


def pick_proc_PR6(Tmax, Tcurrent):
    if Tcurrent[1] + 30 <= Tmax[1]:
        Tcurrent[1] += 30
    elif Tcurrent[2] + 30 <= Tmax[1]:
        Tcurrent[2] += 30
    elif Tcurrent[3] + 30 <= Tmax[3]:
        Tcurrent[3] += 30
    else:
        Tcurrent[4] *= -1
    return Tcurrent


def distribute(lst1):
    working = sum(lst1)
    Tmax = [70, 100, 100, 90, 50]
    Tcurrent = [20, 40, 50, 70, 30]
    if working == 22:
        if not lst1[Dlist['PR1']]:
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
        if not lst1[Dlist['PR2']]:
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
        if not lst1[Dlist['PR3']]:
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
        if not lst1[Dlist['PR5']]:
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if not lst1[Dlist['PR6']]:
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
    if working == 21:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
    if working == 20:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
    if working == 19:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']])\
            and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) \
            and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)

        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent)
            # it is the end of the world as we know it
    pr_lst = all([Tcurrent[i] < 0 for i in range(5)])
    if pr_lst:
        print("getting worse")
    else:
        print("better or same")
        print(lst1[-6:-1])
        print(Tcurrent)
    lst2 = lst1[:]
    # lst2[]
    return lst2


def Pfunk(lst):
    return None


def workable(lst1):
    lst2 = distribute(lst1)
    ret2 = Funk(lst2)
    w1 = PFunk(lst1)
    return None

if __name__ == "__main__":
    lst = [1 for i in range(23)]
    lst[-3] = 0
    workable(lst)
