def BinSearch(a, b, target, parity):
    #Standard binary search w/ recursion
    if b <= a:
        return None
    n = a + ((b - a)/2)
    n += parity != n & 1
    S = Scan(n)
    if S == target:
        return n
    if S > target:
        b = n - 1
    else:
        a = n + 1
    return BinSearch(a, b, target, parity)

dic = {}

def Scan(n):
    if n < 3:
        return [1 ,1, 2][n]
    h = n/2
    if n & 1:
        dic[n] = Scan(h) + Scan(h - 1) + 1
    else:
        dic[n] = Scan(h) + Scan(h + 1) + h
    set(dic)
    return dic[n]

def answer(str_S):
    str_S = int(str_S)
    return BinSearch(0, str_S, str_S, 1) or BinSearch(0, str_S, str_S, 0)

print answer(7)