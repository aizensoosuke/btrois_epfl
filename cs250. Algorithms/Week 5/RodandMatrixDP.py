import math

''' FIBONACCI '''

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def Memoized_Fib(n):
    r = [-1] * (n+1) # Create an array
    return Memoized_Fib_Aux(n,r)

def Memoized_Fib_Aux(n,r):
    if r[n] >= 0:
        return r[n]

    if n == 0 or n==1:
        ans = 1
    else:
        ans = Memoized_Fib_Aux(n-1, r) + Memoized_Fib_Aux(n-2,r)
    
    r[n] = ans
    return r[n]


def bottom_up_fib(n):
    r = [-1] * (n+1)
    r[0] = 1
    r[1] = 1
    for i in range(2, n+1):
        r[i] = r[i-1] + r[i-2]


    return r[n]


''' ROD CUTTING '''


def naive_rod_cutting(p, n):
    if n == 0:
        return 0
    else:
        best = -1
        for i in range(1,n+1):
            best = max(best, p[i] + naive_rod_cutting(p, n-i))
        return best


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n] #Return directly if we already calculated the value
    best = -1
    if n == 0:
        best = 0
    else:
        for i in range(1, n+1):
            best = max(best, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = best
    return r[n]


def memoized_cut_rod(p, n):
    r = [-1]*(n+1) #Create an array r[0...n]
    return memoized_cut_rod_aux(p, n, r)


def bottom_up_cut_rod(p, n):
    r = [0] * (n+1)
    for j in range(1, n+1):
        best = -1
        for i in range(1,j+1):
            best = max(best, p[i] + r[j-i])
        r[j] = best
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for j in range(1, n+1):
        best = -1
        for i in range(1,j+1):
            if best < p[i] + r[j-i]:
                best = p[i] + r[j-i]
                s[j] = i
        r[j] = best
    return r, s


def print_cut_rod_solution(p, n):
    (rm, sm) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(sm[n], end=", ")
        n -= sm[n]


''' MATRIX MULTIPLICATION '''


def naive_matrix_chain(i, j, p):
    if i == j:
        return 0
    else:
        best =  10000000
        for k in range(i, j):
            best = min(best, naive_matrix_chain(i,k, p) + naive_matrix_chain(k+1, j, p) + p[i-1]*p[k]* p[j])
        return best


def memoized_matrix_chain_aux(i, j, p, m):
    if m[i][j] >= 0:
        return m[i][j]
    best = 1000000
    if i == j:
        best = 0
    else:
        for k in range(i, j):
            best = min(best, memoized_matrix_chain_aux(i, k, p, m) + memoized_matrix_chain_aux(k+1, j, p, m) + p[i-1]*p[k]*p[j] )
    m[i][j] = best
    return m[i][j]

def memoized_matrix_chain(i, j, p):
    mem = [[-1 for x in range(j+1)] for x in range(j+1)] #create 2dimensional array as memory
    return memoized_matrix_chain_aux(i, j, p, mem)


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in range(n+1)]  for x in range(n+1)]
    s = [[0 for x in range(n+1)]  for x in range(n+1)]
    for i in range(1,n+1):
        m[i][i] = 0
    for l in range(2, n+1):
        for i  in range(1, n- l + 2):
            j = i + l - 1
            m[i][j] = 10000000
            for k in range(i, j):
                tmp = m[i][k] + m[k+1][j] + p[i-1]*p[k]* p[j]
                if tmp < m[i][j]:
                    m[i][j] = tmp
                    s[i][j] = k
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A_", i,  end="", sep="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")


if __name__ == "__main__":
     price = ['N/A', 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
     nm = 4 
     print('The value is', naive_rod_cutting(price, nm))
     print('The value is', memoized_cut_rod(price, nm))
     print('The value is', bottom_up_cut_rod(price, nm))
     print('The solution is ', end="")
     print_cut_rod_solution(price, nm)
 #   print(fib(40))
    #print(Memoized_Fib(4000))
 #   print(bottom_up_fib(4000))

   ##  pmat = [30, 35, 15, 5, 10, 20, 25]
   ##  print('Number of multiplications is', naive_matrix_chain(1, 6, pmat))
   ##  print('Number of multiplications is', memoized_matrix_chain(1, 6, pmat))
   ##  (mm, sm) = matrix_chain_order(pmat)
   ##  print('Number of multiploications is', mm[1][len(pmat)-1])
   ##  print_optimal_parens(sm, 1, len(pmat)-1)

    # pmat = [30] * 16
    # print('Number of multiplications is', naive_matrix_chain(1, 15, pmat))
    # print('Number of multiplications is', memoized_matrix_chain(1, 15, pmat))




