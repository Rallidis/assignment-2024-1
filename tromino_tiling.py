import sys

def tromino(n, n1=None):
    colors = {'B': 'B', 'G': 'G', 'R': 'R', 'X': 'X'}
    separator = ' '

    if n1 is None:
        n1 = n
    
    if n == 1:
        l1a = [colors['G'], colors['X']]
        l2a = [colors['G'], colors['G']]
        grid = [l1a, l2a]
        for l in grid:
            print(separator.join(l))
                
    elif n == 2:
        l1b = [colors['B'], colors['B'], colors['R'], colors['R']]
        l2b = [colors['B'], colors['G'], colors['G'], colors['R']]
        l3b = [colors['R'], colors['G'], colors['B'], colors['B']]
        l4b = [colors['R'], colors['R'], colors['B'], colors['X']]
        grid = [l1b, l2b, l3b, l4b]

        if n1 == n:
            for l in grid:
                print(separator.join(l))
        return grid
            
    elif n >= 3:
        table1 = [[' '] * (2 ** n) for _ in range(2 ** n)]

        l = tromino(n - 1, n1)

        table2 = [[' '] * (2 ** n) for _ in range(2 ** n)]

        for a in range(2 ** (n - 1)):
            for b in range(2 ** (n - 1)):
                if l[a][b] == colors['B']:
                    table2[a][b] = colors['R']
                elif l[a][b] == colors['R']:
                    table2[a][b] = colors['B']
                else:
                    table2[a][b] = l[a][b]

        for a in range(2 ** (n - 1)):
            for b in range(2 ** (n - 1)):
                table1[a][b] = l[a][b]

        for a in range(2 ** (n - 1)):
            for b in range(2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - b][a] = table2[a][b]

        for a in range(2 ** (n - 1)):
            for b in range(2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - b][2 * (2 ** (n - 1)) - 1 - a] = l[a][b]

        for a in range(2 ** (n - 1)):
            for b in range(2 ** (n - 1)):
                table1[b][2 * (2 ** (n - 1)) - 1 - a] = table2[a][b]

        table1[(2 ** n) // 2][(2 ** n) // 2] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = colors['G']

        if n1 != n:
            for a in range(2 ** (n - 1)):
                for b in range(2 ** (n - 1)):
                    table1[b + 2 ** (n - 1)][a + 2 ** (n - 1)] = l[a][b]
        
            table1[(2 ** n) // 2 - 1][(2 ** n) // 2 - 1] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = colors['G']

        table2 = table1

        if n1 == n:
            for l in table2:
                print(separator.join(l))

        return table2

if __name__ == "__main__":
    n = int(sys.argv[1])
    tromino(n)