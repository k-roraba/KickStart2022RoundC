#CodeJam 2022 Round C Problem 2 - Range Partition

cases = int(input())
output = []

for i in range(cases):

    n, x, y = [int(x) for x in input().split()]
    subset = []

    #find sum of all
    sumAll = n * (n+1) / 2
    sumRat = x + y  #here we assume simplest form

    if not sumAll % sumRat == 0:
        string = "Case #" + str(i+1) + ": IMPOSSIBLE"
        output.append(string)

    else:

        string = "Case #" + str(i+1) + ": POSSIBLE\n"
        want = int(sumAll / sumRat * x)

        while want > n:
            subset.append(n)
            want -= n
            n -= 1
        
        subset.append(want)
        string += str(len(subset))
        string += "\n"
        for j in subset:
            string += str(j)
            string += " "
        output.append(string)

for i in range(cases):
    print(output[i])
        
        
