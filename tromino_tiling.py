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
        for line in grid:
            print(separator.join(line))
                
    elif n == 2:
        l1b = [colors['B'], colors['B'], colors['R'], colors['R']]
        l2b = [colors['B'], colors['G'], colors['G'], colors['R']]
        l3b = [colors['R'], colors['G'], colors['B'], colors['B']]
        l4b = [colors['R'], colors['R'], colors['B'], colors['X']]
        grid = [l1b, l2b, l3b, l4b]

        if n1 == n:
            for line in grid:
                print(separator.join(line))
        return grid
            
    elif n >= 3:
        table1 = [[' '] * (2 ** n) for _ in range(2 ** n)]

        line = tromino(n - 1, n1)

        table2 = [[' '] * (2 ** n) for _ in range(2 ** n)]

        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                if line[i][j] == colors['B']:
                    table2[i][j] = colors['R']
                elif line[i][j] == colors['R']:
                    table2[i][j] = colors['B']
                else:
                    table2[i][j] = line[i][j]

        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                table1[i][j] = line[i][j]

        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - j][i] = table2[i][j]

        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                table1[2 * (2 ** (n - 1)) - 1 - j][2 * (2 ** (n - 1)) - 1 - i] = line[i][j]

        for i in range(2 ** (n - 1)):
            for j in range(2 ** (n - 1)):
                table1[j][2 * (2 ** (n - 1)) - 1 - i] = table2[i][j]

        table1[(2 ** n) // 2][(2 ** n) // 2] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = colors['G']

        if n1 != n:
            for i in range(2 ** (n - 1)):
                for j in range(2 ** (n - 1)):
                    table1[j + 2 ** (n - 1)][i + 2 ** (n - 1)] = line[i][j]
        
            table1[(2 ** n) // 2 - 1][(2 ** n) // 2 - 1] = table1[((2 ** n) // 2) - 1][(2 ** n) // 2] = table1[(2 ** n) // 2][((2 ** n) // 2) - 1] = colors['G']

        table2 = table1

        if n1 == n:
            for line in table2:
                print(separator.join(line))

        return table2

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tromino_tiling.py n")
        sys.exit(1)

    n = int(sys.argv[1])
    tromino(n)