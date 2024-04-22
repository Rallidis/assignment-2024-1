#----------------------------------------
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

        if n3 == n:
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