import sys
def tromino(n, n1 = None):
    b = 'B'
    g = 'G'
    r = 'R'
    x = 'X'
    s = ' '

    if n1 == None:
        n1 = n
    
    if n == 1:
        l1a = [g, x]
        l2a = [g, g]
        l3a = [l1a, l2a]
        for i in l3a:
            l = ""
            for j in i:
                if j != x:
                    l = l + j + s
                else:
                    l = l + j
            print(l)
                
    elif n == 2:
        l1b = [b, b, r, r]
        l2b = [b, g, g, r]
        l3b = [r, g, b, b]
        l4b = [r, r, b, x]

        l5b = [l1b, l2b, l3b, l4b]

        if n1 == n:
                for i in l5b:
                    l = ""
                    for j in i:
                        if j != x:
                            l = l + j + s
                        else:
                            l = l + j
                    print(l)
        return l5b
            
    elif n >= 3:

        table1 = []
        for i in range(2 ** n):
            table1.append([' '] * (2 ** n))

        line = tromino(n - 1, n1)

        line2 = []
        for i in range(2 ** (n - 1)):
            line2.append([' '] * (2 ** (n - 1))) 

        for i in range(0, 2 ** (n - 1)):
            for j in range(0, 2 ** (n - 1)):
                if line[i][j] == b:
                    line2[i][j] = r
                elif line[i][j] == r:
                    line2[i][j] = b
                else:
                    line2[i][j] = line[i][j]

        for i in range(0, 2 ** (n - 1)):
            for j in range(0, 2 ** (n - 1)):
                table1[i][j] = line[i][j]

        for i in range(0, 2 ** (n - 1)):
            for j in range(0, 2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - j][i] = line2[i][j]

        for i in range(0, 2 ** (n - 1)):
            for j in range(0, 2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - j][2 * (2 ** (n - 1)) - 1 - i] = line[i][j]

        for i in range(0, 2 ** (n - 1)):
            for j in range(0, 2 ** (n - 1)):
                table1[j][2 * (2 ** (n - 1)) - 1 - i] = line2[i][j]

        table1[(2 ** n) // 2][(2 ** n) // 2] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = g

        if n1 != n:

            for i in range(0, 2 ** (n - 1)):
                for j in range(0, 2 ** (n - 1)):
                    table1[j + 2 ** (n - 1)][i + 2 ** (n - 1)] = line[i][j]
        
            table1[(2 ** n) // 2 - 1][(2 ** n) // 2 - 1] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = g

        table2 = table1

        if n1 == n:
                for i in table2:
                    l = ""
                    for j in i:
                        if j != i:
                            l = l + j + s
                        else:
                            l = l + j
                    print(l)

        return table2

if __name__ == "__main__":
    n = int(sys.argv[1])
    tromino(n)