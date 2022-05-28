#CodeJam 2022 Round C Problem 2 - Range Partition

# one thing to understand:  sum(subset) + sum(remaining) = sum(totalset)
# also:  to get the ratio x:y, you need at least x+y equal size (in this case size is the sum of the subset) pieces
# so the ratio is possible if the sum(totalset) is divisible by (x+y)
# one caveat:  if the ratio is something dumb, like 100:200, obviously that will throw things off
# to avoid that causing issues, a proper program would use Euclid's (?) Algorithm to check that 
# x:y is irreducible -- that is, that x and y are coprime

# but I decided that they weren't going to be complete jerks with the input so...

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
        
        
