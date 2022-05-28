#CodeJam 2022 Round C Problem 1 - New Password

# this could've taken me 30 minutes, if I hadn't used '==' when I meant '='.  
# Something about fiddling with booleans makes me want to use the '=='.
# Took me about 20 minutes to realize what I had done.

cases = int(input())
output = []

for i in range(cases):
    n = int(input())
    pwd = input()

    containsInt = False
    containsSpecial = False
    containsUpper = False
    containsLower = False   

    for j in pwd:
        #check if 1 digit; can I turn this off once found?
        if not containsInt and j.isdigit():
            #print(j + " is digit")
            containsInt = True
            # I tried a break statement here, but that made the thing quit way too soon;
            # I never truly learned what 'break' does in a nested loop situation   

        #check if one uppercase
        if not containsUpper and j.isupper():
            #print(j + " is uppercase") -- was using this when the break statement was skipping stuff
            containsUpper = True 

        #check if one lowercase
        if not containsLower and j.islower():
            #print(j + " is lowercase")
            containsLower = True

        #check if special char # @ * and & 
        if not containsSpecial:
            if j == '#' or j == '@' or j == '*' or j == '&':
                containsSpecial = True
    
    if not containsSpecial:
        pwd += "@"
        n += 1

    if not containsLower:
        pwd += "a"
        n += 1

    if not containsUpper:
        pwd += "A"
        n += 1

    if not containsInt:
        pwd += "1"
        n += 1

    if n < 7:
        for j in range(7 - n):
            pwd += "1"
    
    output.append(pwd)

for i in range(cases):
    print("Case #{}:".format(i+1), output[i])
            
        
