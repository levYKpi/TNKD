#######################################################################################################################
############ FUNCTIONS ################################################################################################
############ BINLST = D1, D2, D3, D6, D8, C1, C2, C4, C5, C6, B1, B2, B4, B5, M1, M2, A1, A2, Pr1, Pr2, Pr3, Pr5, Pr6 #
############           0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17   18   19   20   21   22 #
from table import create_table as ct
import numpy


Q = [
    0.000022, 0.000022, 0.000022, 0.000022, 0.000022, 0.000022,
    0.00041, 0.00041, 0.00041, 0.000015, 0.000015,
    0.000015, 0.000015, 0.00036, 0.00036, 0.00041, 0.00041, 0.00012,
    0.00012,  0.00012, 0.00012, 0.00012, 0.00012, 0.00012
]
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


def pick_proc_PR1(Tmax, Tcur, lst):
    Tcurrent = Tcur[:]
    if Tcurrent[2] + 20 <= Tmax[2] and lst[20]:
        Tcurrent[2] += 20
    elif Tcurrent[1] + 10 <= Tmax[1] and Tcurrent[3] + 10 <= Tmax[3] and lst[19] and lst[21]:
        Tcurrent[1] += 10
        Tcurrent[3] += 10
    elif Tcurrent[3] + 10 <= Tmax[3] and Tcurrent[4] + 10 <= Tmax[4] and lst[21] and lst[22]:
        Tcurrent[3] += 10
        Tcurrent[4] += 10
    elif Tcurrent[1] + 10 <= Tmax[1] and Tcurrent[4] + 10 <= Tmax[4] and lst[19] and lst[22]:
        Tcurrent[1] += 10
        Tcurrent[4] += 10
    else:
        Tcurrent[0] *= -1
    return Tcurrent


def pick_proc_PR2(Tmax, Tcur, lst):
    Tcurrent = Tcur[:]
    if Tcurrent[0] + 40 <= Tmax[0] and lst[18]:
        Tcurrent[0] += 40
    elif Tcurrent[2] + 40 <= Tmax[2] and lst[20]:
        Tcurrent[2] += 40
    else:
        Tcurrent[1] *= -1
    return Tcurrent


def pick_proc_PR3(Tmax, Tcur, lst):
    Tcurrent = Tcur[:]
    if Tcurrent[0] + 50 <= Tmax[0] and lst[18]:
        Tcurrent[0] += 50
    elif Tcurrent[1] + 50 <= Tmax[1] and lst[19]:
        Tcurrent[1] += 50
    else:
        Tcurrent[2] *= -1
    return Tcurrent


def pick_proc_PR5(Tmax, Tcur, lst):
    Tcurrent = Tcur[:]
    if Tcurrent[0] + 50 <= Tmax[0] and Tcurrent[1] + 20 <= Tmax[1] and lst[18] and lst[19]:
        Tcurrent[0] += 50
        Tcurrent[1] += 20
    elif Tcurrent[2] + 50 <= Tmax[2] and Tcurrent[1] + 20 <= Tmax[1] and lst[20] and lst[19]:
        Tcurrent[2] += 50
        Tcurrent[1] += 20
    elif Tcurrent[0] + 50 <= Tmax[0] and Tcurrent[4] + 20 <= Tmax[4] and lst[22] and lst[18]:
        Tcurrent[0] += 50
        Tcurrent[4] += 20
    elif Tcurrent[2] + 50 <= Tmax[2] and Tcurrent[4] + 20 <= Tmax[4] and lst[20] and lst[22]:
        Tcurrent[2] += 50
        Tcurrent[4] += 20
    else:
        Tcurrent[3] *= -1
    return Tcurrent


def pick_proc_PR6(Tmax, Tcur, lst):
    Tcurrent = Tcur[:]
    if Tcurrent[1] + 30 <= Tmax[1] and lst[19]:
        Tcurrent[1] += 30
    elif Tcurrent[2] + 30 <= Tmax[2] and lst[20]:
        Tcurrent[2] += 30
    elif Tcurrent[3] + 30 <= Tmax[3] and lst[21]:
        Tcurrent[3] += 30
    else:
        Tcurrent[4] *= -1
    return Tcurrent


def distribute(lst1):
    working = sum(lst1[18:])
    Tmax = [70, 100, 100, 90, 50]
    Tcurrent = [20, 40, 50, 70, 30]
    if working == 4:
        if not lst1[Dlist['PR1']]:
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
        if not lst1[Dlist['PR2']]:
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
        if not lst1[Dlist['PR3']]:
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
        if not lst1[Dlist['PR5']]:
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if not lst1[Dlist['PR6']]:
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
    if working == 3:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
    if working == 2:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
        if (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
    if working == 1:
        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']])\
            and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR5']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) \
            and (not lst1[Dlist['PR3']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR2']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)

        if (not lst1[Dlist['PR1']]) and (not lst1[Dlist['PR3']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR1(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)

        if (not lst1[Dlist['PR2']]) and (not lst1[Dlist['PR3']]) \
            and (not lst1[Dlist['PR5']]) and (not lst1[Dlist['PR6']]):
            Tcurrent = pick_proc_PR2(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR3(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR5(Tmax, Tcurrent, lst1)
            Tcurrent = pick_proc_PR6(Tmax, Tcurrent, lst1)
            # it is the end of the world as we know it
    pr_lst = any([Tcurrent[i] < 0 for i in range(5)])
    lst2 = lst1[:]
    if pr_lst:
        for i in range(18, 23, 1):
            if lst2[i]:
                lst2[i] *= -1
        print("getting worse")
        print("PR:  1,  2,  3,  4,  5")
        print("   %3d,%3d,%3d,%3d,%3d" % (lst2[18], lst2[19], lst2[20], lst2[21], lst2[22]))
        print("   %3d,%3d,%3d,%3d,%3d" % (
            Tcurrent[0] * lst2[18], Tcurrent[1] * lst2[19], Tcurrent[2] * lst2[20],
            Tcurrent[3] * lst2[21], Tcurrent[4] * lst2[22]
        ))
        print("system is not working")
    # elif all([Tmax[i] == Tcurrent[i] for i in range(5)]):
    #     print("same")
    #     print("PR:  1,  2,  3,  4,  5")
    #     print("   %3d,%3d,%3d,%3d,%3d" % (lst[18], lst[19], lst[20], lst[21], lst[22]))
    else:
        for i in range(18, 23, 1):
            if not lst2[i]:
                lst2[i] = -1
        print("better")
        print("PR:  1,  2,  3,  4,  5")
        print("   %3d,%3d,%3d,%3d,%3d"%(lst2[18], lst2[19], lst2[20], lst2[21], lst2[22]))
        print("   %3d,%3d,%3d,%3d,%3d"%(
            Tcurrent[0] * lst2[18], Tcurrent[1] * lst2[19], Tcurrent[2] * lst2[20],
            Tcurrent[3] * lst2[21], Tcurrent[4] * lst2[22]
        ))
    # lst2[]
    return lst2


def PFunk(lst):
    values = []
    for i in range(23):
        values.append(lst[i] * (1 - Q[i]) + (1 - lst[i]) * (Q[i]))
    P = numpy.prod(values)
    return P

lst_stat = [0 for _ in range(23)]

def workable(lst1):
    print("--------------------------------------------------------------------------------------------")
    print(lst1)
    was_working = Funk(lst1)
    if was_working:
        print("system was working by Function")
    else:
        print("system was not working")
        for i in range(23):
            lst_stat[i] += lst1[i]
    if_all_proc = lst1[0:18]
    for i in range(5):
        if_all_proc.append(1)
    if_all_proc = Funk(if_all_proc)
    if if_all_proc and not all(lst1[18:]):
        lst2 = distribute(lst1)
        # ret2 = Funk(numpy.abs(lst2))
        # if ret2:
        #     print("system is working")
    w1 = PFunk(lst1)
    print(w1)
    return w1


def one_exception():
    exceptions = vectorGenerator([1 for _ in range(23)], 1)
    results = [workable(exception) for exception in exceptions]
    return results


def two_exception():
    exceptions = vectorGenerator([1 for _ in range(23)], 2)
    results = [workable(exception) for exception in exceptions]
    return results


def tree_exception():
    exceptions = vectorGenerator([1 for _ in range(23)], 3)
    results = []
    for i in range(1, len(exceptions), 2):
        # print(i)
        results.append(workable(exceptions[i]))
    return results


def four_exception():
    exceptions = vectorGenerator([1 for _ in range(23)], 4)
    results = []
    for i in range(0, len(exceptions), 10):
        results.append(workable(exceptions[i]))
    return results


if __name__ == "__main__":
    # lst = [1 for i in range(23)]
    # lst[-1] = 0
    # lst[-2] = 0
    # lst[-3] = 0
    # lst[-4] = 0
    # # lst[-5] = 0
    # workable(lst)
    res1 = numpy.array(one_exception())
    res2 = numpy.array(two_exception())
    res3 = numpy.array(tree_exception())*2
    res4 = numpy.array(four_exception())*10
    print("statistic")
    stat_dict = {}
    for key, val in Dlist.items():
        stat_dict[key] = lst_stat[val]
        # print((key, val))
    for i in range(100000):
        for key, val in stat_dict.items():
            if i == val:
                print((key, "->", val))
    print("P_res:")
    print(numpy.sum(res1) + numpy.sum(res2) + numpy.sum(res3) + numpy.sum(res4))
