def F1(x, y):
    global M
    for z in M:
        if (x - z) * (y - z) < 0:
            return 1
    return 0


def F2(x, y):
    global M
    x = [int(i) for i in str(x)]
    y = [int(i) for i in str(y)]
    for i in range(len(x)):
        if x[i]<y[i]:
            return 0
    return 1



def F3(x, y):
    global M
    if (x / 5)//1 == (y / 5)//1:
        return 1
    return 0


def F4(x, y):
    global M
    if (x ** 2 - y ** 3) % 2 == 0:
        return 0
    return 1


def F5(x, y):
    if abs(x - y) < 10:
        return 1
    return 0


def refl_check(funct):
    global M
    for x in M:
        if funct(x, x) == 0:
            print(f"{funct.__name__} Не рефлекcивно. Контрпример : {x}")
            return 0
    print(f"{funct.__name__} Рефлекcивно")
    return 1


def Arefl_check(funct):
    global M
    for x in M:
        if funct(x, x) == 1:
            print(f"{funct.__name__} Не Арефлекcивно. Контрпример : {x}")
            return 0
    print(f"{funct.__name__} Арефлекcивно")
    return 1


def symmetric_check(funct):
    global M
    for x in M:
        for y in M:
            if funct(x, y) != funct(y, x):
                print(f"{funct.__name__} не симметрично. Контрпример {x, y}")
                return 0
    print(f"{funct.__name__} симметрично")
    return 1


def antisymmetric_check(funct):
    global M
    for x in M:
        for y in M:
            if funct(x, y) == 1 and funct(y, x) == 1:
                if x != y:
                    print(f"{funct.__name__} не АНТИсимметрично. Контрпример {x, y}")
                    return 0
    print(f"{funct.__name__} АНТИсимметрично.")
    return 1


def asymmetric_check(funct):
    """ Бинарное отношение асимметрично тогда и только тогда,
     когда оно антисимметрично и антирефлексивно """
    global M
    for x in M:
        for y in M:
            if funct(x, y) == 1 and funct(x, y) == 1:
                print(f"{funct.__name__} не Асимметрично. Контрпример {x, y}")
                return 0
    print(f"{funct.__name__} Асимметрично.")
    return 1


def tranz_check(func):
    global M
    for a in M:
        for b in M:
            for c in M:
                if func(a, b) == 1 and func(b, c) == 1 and func(a, c) == 0 and a!=c:#ПОПРОБУЙТЕ УДАЛИТЬ a!=c если ТРАНЗИТИВНО ПОКАЖЕТ
                    print(f"{func.__name__}  не транзитивно. Контрпример {a, b, c}")
                    return 0
    print(f"{func.__name__} транзитивно")
    return 1


def get_matrix(func):
    global M
    matrix = [[i for i in range(len(M) + 1)] for _ in range(len(M) + 1)]
    for i in range(len(M)):
        for j in range(len(M)):
            matrix[i + 1][j + 1] = func(M[i], M[j])
    for i in range(1, len(M) + 1):
        matrix[0][i] = M[i - 1]
    for i in range(1, len(M) + 1):
        matrix[i][0] = M[i - 1]
    for i in matrix:
        form = '{:5}' * (len(M)+1)
        print(form.format(*i))


def getresult(func):
    refl_check(func)
    Arefl_check(func)
    symmetric_check(func)
    antisymmetric_check(func)
    asymmetric_check(func)
    tranz_check(func)
    get_matrix(func)
    print("\n")


M = (97, 15, 17, 20, 56, 88, 61, 30)
functions = [F1, F2, F3, F4, F5]
for i in functions:
    getresult(i)
